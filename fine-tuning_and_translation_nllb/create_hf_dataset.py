import json
import os

mapping_file = "../all_executions/re-computation_folder/results_full_glot500_hsb-de/mining/bucc2017/hsb-de/glot500.hsb-de.test.sim.pred.postprocessing_5.1_s01A0"
src_file = "../data/bucc_style_data/hsb-de/hsb-de.test.hsb"
trg_file = "../data/bucc_style_data/hsb-de/hsb-de.test.de"

output_file = "data/stage3_train_data.jsonl"

src_dict = {}
with open(src_file, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split("\t", 1)
        if len(parts) == 2:
            src_dict[parts[0]] = parts[1]

trg_dict = {}
with open(trg_file, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split("\t", 1)
        if len(parts) == 2:
            trg_dict[parts[0]] = parts[1]

matched_count = 0
missing_count = 0

with open(mapping_file, "r", encoding="utf-8") as f_in, open(output_file, "w", encoding="utf-8") as f_out:
    for line in f_in:
        parts = line.strip().split("\t")
        if len(parts) >= 2:
            src_id = parts[0]
            trg_id = parts[1]
            
            if src_id in src_dict and trg_id in trg_dict:
                json_line = {
                    "translation": {
                        "hsb": src_dict[src_id],
                        "de": trg_dict[trg_id]
                    }
                }
                f_out.write(json.dumps(json_line, ensure_ascii=False) + "\n")
                matched_count += 1
            else:
                missing_count += 1

print("Dataset creation finished successfully!")
if missing_count > 0:
    print(f"Warning: {missing_count} IDs could not be found in the source or target files.")