from typing import Dict, List, Tuple
from transformers import AutoTokenizer

import argparse
import string

PUNCTUATION_SET = set(string.punctuation)
NEW_WORD_PREFIX = "\u2581" #NOTE: maybe different for other language models


class LanguageModelClass:
    def __init__(self, model_path: str):
        self.tokenizer = AutoTokenizer.from_pretrained(model_path) # load tokenizer

    def get_tokens_for_sentence(self, sentence: str) -> List[str]:
        return self.tokenizer.tokenize(sentence)

# this function processes the sentence mapping file (output) from the pipeline
def getMappedNumbers(file_path: str) -> List[Tuple[int, int]]:
    res = list()
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if not line.strip():
                continue
            parts = line.split('\t', 1)
            if len(parts) == 2:
                id_src, id_trg = parts
                key_src_str = id_src.split('-')[1]
                key_trg_str = id_trg.strip().split('-')[1]
                res.append((int(key_src_str), int(key_trg_str)))
    return res

# function extracts training/ test data from file and returns dictionary
def getSentencesFromFile(file_path: str) -> Dict[int,str]:
    res = dict()
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if not line.strip():
                continue
            parts = line.split('\t', 1)
            if len(parts) == 2:
                id_part, sentence = parts
                key_str = id_part.split('-')[1]
                key = int(key_str)
                value = sentence.strip()
                res[key] = value
    return res

# TODO: refactor this fanction and extract repeating logic into a helper function
# NOTE: the extended version of this function has the assumption that as soon as a punctuation mark is within a token, the next token should be a new word
# this function transfers the embedding from token level to word level
def transfer_tkn_level_to_word_level(sentence_tkns: List[str]) -> List[str]:
    res_word_list = []
    temp_concat_tokens_str = ""
    for i, tkn_temp in enumerate(sentence_tkns):
        if any(char in PUNCTUATION_SET for char in tkn_temp):
            if len(temp_concat_tokens_str) > 0:
                res_word_list.append(temp_concat_tokens_str)
                temp_concat_tokens_str = ""
            if tkn_temp.startswith(NEW_WORD_PREFIX):
                tkn_temp = tkn_temp[1:]
            res_word_list.append(tkn_temp)
        elif tkn_temp.startswith(NEW_WORD_PREFIX):
            if len(temp_concat_tokens_str) > 0:
                res_word_list.append(temp_concat_tokens_str)
            temp_concat_tokens_str = tkn_temp[1:]
        else:
            temp_concat_tokens_str += tkn_temp
    if len(temp_concat_tokens_str) > 0:
        res_word_list.append(temp_concat_tokens_str)
    return res_word_list

def create_input_file_for_fast_align(mapping_list: List[Tuple[int,int]], src_sentences_dict: Dict[int,str], trg_sentences_dict: Dict[int,str], fast_align_input_filename: str, embedding_helper):
    with open(fast_align_input_filename,'a',encoding='utf-8') as file:
        for i, (src_num, trg_num) in enumerate(mapping_list):
            src_sentence = src_sentences_dict[src_num]
            trg_sentence = trg_sentences_dict[trg_num]
            src_sentence_tkns = embedding_helper.get_tokens_for_sentence(src_sentence)
            trg_sentence_tkns = embedding_helper.get_tokens_for_sentence(trg_sentence) 
            src_sentence_words = transfer_tkn_level_to_word_level(src_sentence_tkns)
            trg_sentence_words = transfer_tkn_level_to_word_level(trg_sentence_tkns)
            fast_align_src_str = " ".join(src_sentence_words)
            fast_align_trg_str = " ".join(trg_sentence_words)
            file.write(f"{fast_align_src_str} ||| {fast_align_trg_str}\n")


def main(mapping_file_name_train: str, mapping_file_name_test: str, src_file_name_train: str, trg_file_name_train: str, src_file_name_test: str, trg_file_name_test: str, model_path: str, fast_align_input_filename: str = 'input_fast_align.txt'):
    embedding_helper = LanguageModelClass(model_path=model_path)
    mapping_list_train = getMappedNumbers(mapping_file_name_train) #mappings from PaSeMiLL
    mapping_list_test = getMappedNumbers(mapping_file_name_test) #mappings from PaSeMiLL
    src_sentences_train_dict = getSentencesFromFile(src_file_name_train) #dict contains the sentence number (key) and the sentence (value) from the BUCC-style data files
    trg_sentences_train_dict = getSentencesFromFile(trg_file_name_train)
    src_sentences_test_dict = getSentencesFromFile(src_file_name_test)
    trg_sentences_test_dict = getSentencesFromFile(trg_file_name_test)

    open(fast_align_input_filename, 'w').close()
    create_input_file_for_fast_align(mapping_list_train, src_sentences_train_dict, trg_sentences_train_dict, fast_align_input_filename, embedding_helper=embedding_helper)
    create_input_file_for_fast_align(mapping_list_test, src_sentences_test_dict, trg_sentences_test_dict, fast_align_input_filename, embedding_helper=embedding_helper)


def parse_args():
    parser = argparse.ArgumentParser(description="Erstellt eine Input-Datei für fast_align basierend auf Sentence-Mappings.")
    parser.add_argument("--mapping-train", type=str, required=True, help="Pfad zur Mapping-Datei (Training)")
    parser.add_argument("--src-train", type=str, required=True, help="Pfad zur Quellsprachen-Datei (Training)")
    parser.add_argument("--trg-train", type=str, required=True, help="Pfad zur Zielsprachen-Datei (Training)")
    parser.add_argument("--mapping-test", type=str, required=True, help="Pfad zur Mapping-Datei (Test)")
    parser.add_argument("--src-test", type=str, required=True, help="Pfad zur Quellsprachen-Datei (Test)")
    parser.add_argument("--trg-test", type=str, required=True, help="Pfad zur Zielsprachen-Datei (Test)")
    parser.add_argument("--model-path", type=str, required=True, help="Pfad oder Name des HuggingFace Modells")
    parser.add_argument("--output", type=str, default="input_fast_align.txt", help="Name der Ausgabedatei (Standard: input_fast_align.txt)")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    main(
        mapping_file_name_train=args.mapping_train,
        mapping_file_name_test=args.mapping_test,
        src_file_name_train=args.src_train,
        trg_file_name_train=args.trg_train,
        src_file_name_test=args.src_test,
        trg_file_name_test=args.trg_test,
        model_path=args.model_path,
        fast_align_input_filename=args.output
    )

"""
execute script with in terminal:

python fast_align_create_input.py \
  --mapping-train "/dss/dsshome1/0F/ge87fen2/PaSeMiLL/all_executions/execution_Belopsem_glot500_no_pretraining_v11_CBIE_adjusted/results_full_glot500/mining/bucc2017/hsb-de/glot500.hsb-de.train.sim.pred" \
  --src-train "/dss/dsshome1/0F/ge87fen2/PaSeMiLL/data/bucc_style_data/hsb-de/hsb-de.train.hsb" \
  --trg-train "/dss/dsshome1/0F/ge87fen2/PaSeMiLL/data/bucc_style_data/hsb-de/hsb-de.train.de" \
  --mapping-test "/dss/dsshome1/0F/ge87fen2/PaSeMiLL/all_executions/execution_Belopsem_glot500_no_pretraining_v11_CBIE_adjusted/results_full_glot500/mining/bucc2017/hsb-de/glot500.hsb-de.test.sim.pred" \
  --src-test "/dss/dsshome1/0F/ge87fen2/PaSeMiLL/data/bucc_style_data/hsb-de/hsb-de.test.hsb" \
  --trg-test "/dss/dsshome1/0F/ge87fen2/PaSeMiLL/data/bucc_style_data/hsb-de/hsb-de.test.de" \
  --model-path "cis-lmu/glot500-base" \
  --output "/dss/dsshome1/0F/ge87fen2/PaSeMiLL/fast_align_input_output/hsb-de/input_fast_align.txt"

"""

# NOTE: this file prepares the required input file for the fast_align tool based on the predictions made by the PaSeMiLL pipeline
# File content format: src_sentence ||| trg_sentence
# NOTE: both sentences need to be separated into words and punctuations separated by whitespace