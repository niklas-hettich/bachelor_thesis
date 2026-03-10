import argparse
import re
from collections import Counter
import sys

def get_sentences_and_count_words(file_paths, output_path, top_n):
    word_counts = Counter()
    word_pattern = re.compile(r'\w+')
    total_lines = 0
    
    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    
                    parts = line.split('\t', 1)
                    if len(parts) == 2:
                        sentence = parts[1]
                        words = word_pattern.findall(sentence.lower())
                        word_counts.update(words)
                        total_lines += 1
        except FileNotFoundError:
            print(f"WARNING: file '{file_path}' not found")
            continue
    # print(f"finished analysis. {total_lines} line processed")
    # print(f"number of unique words found: {len(word_counts)}")
    
    if len(word_counts) == 0:
        print("ERROR: no words found")
        sys.exit(1)

    with open(output_path, 'w', encoding='utf-8') as out:
        out.write(f"rank\tword\tcount\n")
        for rank, (word, count) in enumerate(word_counts.most_common(top_n), 1):
            out.write(f"{rank}\t{word}\t{count}\n")
            
    print("finished computation")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generates a word frequency list for Sorbian from multiple files.")
    parser.add_argument("--input_files", type=str, nargs='+', required=True, help="List of the .hsb files (e.g., file1.hsb file2.hsb).")
    parser.add_argument("--output_file", type=str, required=True, help="Path for the output file.")
    parser.add_argument("--top_n", type=int, default=200, help="Number of words to be stored in the output.")
    
    args = parser.parse_args()
    
    get_sentences_and_count_words(args.input_files, args.output_file, args.top_n)