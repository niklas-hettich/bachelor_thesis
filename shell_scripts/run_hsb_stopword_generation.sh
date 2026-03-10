#!/bin/bash
#SBATCH --job-name=HSB_Stopwords
#SBATCH --output=slurm_stopwords_%j.out
#SBATCH --error=slurm_stopwords_%j.err
#SBATCH --time=10:00:00
#SBATCH --gres=gpu:1
#SBATCH --partition=lrz-hgx-a100-80x4

echo "job started on pertition: $(hostname)"
echo "start-time: $(date)"

eval "$(/dss/dsshome1/0F/ge87fen2/miniconda3/bin/conda shell.bash hook)"
conda activate pasemill_env
echo "Conda environment 'pasemill_env' activated."

BASE_DIR="../data/bucc_style_data/hsb-de"
TRAIN_FILE="$BASE_DIR/hsb-de.train.hsb"
TEST_FILE="$BASE_DIR/hsb-de.test.hsb"
OUTPUT_FILE="../stop-words/hsb_generated_stopwords_unfiltered.txt"

python ../generate_hsb_stopwords.py \
  --input_files "$TRAIN_FILE" "$TEST_FILE" \
  --output_file "$OUTPUT_FILE" \
  --top_n 150

echo "end-time: $(date)"