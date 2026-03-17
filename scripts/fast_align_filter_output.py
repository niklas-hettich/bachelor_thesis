import argparse
from typing import Tuple, List, Dict

# NOTE: execute this script for src->trg and for trg->src

# parses the sentences to words for src and trg sentence pair (out of corpus.txt)
def get_words(sentence_pair: str) -> Tuple[List[str], List[str]]:
    curr_src_sentence, curr_trg_sentence = [s.strip() for s in sentence_pair.split("|||")]
    curr_src_sentence_words = curr_src_sentence.split()
    curr_trg_sentence_words = curr_trg_sentence.split()
    return (curr_src_sentence_words, curr_trg_sentence_words)

# parses the alignments
def get_alignments(alignments_fast_align: str) -> List[Tuple[int,int]]:
    alignment_list_temp = alignments_fast_align.strip().split()
    res_list = []
    for alignment in alignment_list_temp:
        left, right = alignment.split("-")
        res_list.append((int(left), int(right)))
    return res_list

# inplace update of word counts for a sentence (src or trg)
def update_word_count(sentence_words: List[str], word_count_dict: Dict):
    for word in sentence_words:
        word_count_dict[word] = word_count_dict.get(word, 0) + 1

# inplace update of alignment counts for a sentence pair
def update_alignment_count(src_sentence_words: List[str], trg_sentence_words: List[str], alignment_list: List[Tuple[int,int]], mapping_count_dict: Dict):
    for (src_id, trg_id) in alignment_list:
        if src_id >= len(src_sentence_words) or trg_id >= len(trg_sentence_words):
            continue
        src_word = src_sentence_words[src_id]
        trg_word = trg_sentence_words[trg_id]
        word_pair_key = (src_word, trg_word)
        mapping_count_dict[word_pair_key] = mapping_count_dict.get(word_pair_key, 0) + 1
    return

def get_dice_coefficient(src_word_count_dict: Dict, trg_word_count_dict: Dict, mapping_count_dict: Dict, src_word: str, trg_word: str) -> float:
    mapping_key = (src_word, trg_word)
    pair_count = mapping_count_dict.get(mapping_key, 0)
    src_count = src_word_count_dict.get(src_word, 0)
    trg_count = trg_word_count_dict.get(trg_word, 0)
    
    denom = src_count + trg_count
    if denom == 0:
        return 0.0
        
    return (2.0 * pair_count) / denom

def keep_alignment(mapping_count_dict: Dict, src_word: str, trg_word: str) -> bool :
    mapping_key = (src_word, trg_word)
    pair_count = mapping_count_dict.get(mapping_key, 0)
    return (pair_count >= 3)

def main(corpus_path: str = "corpus.txt", alignments_path: str = "output.align", output_path: str = "output_filtered_src_to_trg.align", dice_threshold_value: float = 0.1):

    with open(corpus_path, "r", encoding='utf-8') as file:
        corpus_lines = file.readlines()

    with open(alignments_path, "r", encoding='utf-8') as file:
        alignments_lines = file.readlines()

    if len(corpus_lines) == 0:
        print("ERROR: reading lines of corpus.txt failed!!")
        exit()
    if len(alignments_lines) == 0:
        print("ERROR: reading lines of output.align failed!!")
        exit()    
    if len(corpus_lines) != len(alignments_lines):
        print("ERROR: corpus_lines and alignments_lines have different lengths --> lists should have the same length")
        exit()


    src_word_count_dict = {}
    trg_word_count_dict = {}
    mapping_count_dict = {}
    
    for i, (sentence_pair, alignments_fast_align) in enumerate(zip(corpus_lines, alignments_lines)):
        src_sentence_words, trg_sentence_words = get_words(sentence_pair)
        alignment_list = get_alignments(alignments_fast_align)

        update_word_count(src_sentence_words, src_word_count_dict)
        update_word_count(trg_sentence_words, trg_word_count_dict)

        update_alignment_count(src_sentence_words, trg_sentence_words, alignment_list, mapping_count_dict)


    res_line_list = []

    for i, (sentence_pair, alignments_fast_align) in enumerate(zip(corpus_lines, alignments_lines)):
        src_sentence_words, trg_sentence_words = get_words(sentence_pair)
        alignments_for_sent_pair = get_alignments(alignments_fast_align)

        current_line_output_list = []
        for i, (src_id, trg_id) in enumerate(alignments_for_sent_pair):

            dice_value = get_dice_coefficient(src_word_count_dict, trg_word_count_dict, mapping_count_dict, src_sentence_words[src_id], trg_sentence_words[trg_id])
            if dice_value >= dice_threshold_value:
                current_line_output_list.append(f"{src_id}-{trg_id}")

            # if keep_alignment(mapping_count_dict, src_sentence_words[src_id], trg_sentence_words[trg_id]):
            #     current_line_output_list.append(f"{src_id}-{trg_id}")

        final_line = " ".join(current_line_output_list) + "\n"
        res_line_list.append(final_line)


    with open(output_path, "w", encoding='utf-8') as file:
        file.writelines(res_line_list)



def parse_args():
    parser = argparse.ArgumentParser(description="Filter fast_align alignments based on Dice Coefficient.")
    parser.add_argument("--corpus", type=str, default="corpus.txt", help="Path to corpus file")
    parser.add_argument("--alignments", type=str, default="output.align", help="Path to fast_align output")
    parser.add_argument("--output", type=str, default="output_filtered.align", help="Output file path")
    parser.add_argument("--threshold", type=float, default=0.01, help="Dice threshold (0.0 - 1.0)")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    main(args.corpus, args.alignments, args.output, args.threshold)
