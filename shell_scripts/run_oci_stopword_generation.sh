#!/bin/bash
#SBATCH --job-name=OCI_Stopwords
#SBATCH --output=slurm_stopwords_%j.out
#SBATCH --error=slurm_stopwords_%j.err
#SBATCH --time=00:10:00
#SBATCH --gres=gpu:1
#SBATCH --partition=lrz-hgx-a100-80x4

echo "Job started on pertition: $(hostname)"
echo "start-time: $(date)"

source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate bachelor_thesis_env
echo "Conda environment 'bachelor_thesis_env' activated."

BASE_DIR="../data/bucc_style_data/oci-es"
TRAIN_FILE="$BASE_DIR/oci-es.train.oci"
TEST_FILE="$BASE_DIR/oci-es.test.oci"
OUTPUT_FILE="../stop-words/oci_generated_stopwords_unfiltered.txt"

python ../stop-words/generate_stopwords.py \
  --input_files "$TRAIN_FILE" "$TEST_FILE" \
  --output_file "$OUTPUT_FILE" \
  --top_n 300

echo "end-time: $(date)"