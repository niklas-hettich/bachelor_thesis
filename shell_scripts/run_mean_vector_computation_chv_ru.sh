#!/bin/bash
#SBATCH --job-name=MeanVecCalc
#SBATCH --output=slurm_meanvec_%j.out
#SBATCH --error=slurm_meanvec_%j.err
#SBATCH --time=00:30:00
#SBATCH --gres=gpu:1
#SBATCH --partition=lrz-hgx-a100-80x4

echo "Job started on partition: $(hostname)"
echo "start-time: $(date)"

source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate bachelor_thesis_env
echo "Conda environment 'bachelor_thesis_env' activated."

SCRIPT_PATH="../mean_vectors/create_mean_vector.py"
DATA_DIR="../data/bucc_style_data/chv-ru"

CHV_TRAIN="$DATA_DIR/chv-ru.train.chv"
RU_TRAIN="$DATA_DIR/chv-ru.train.ru"

CHV_OUT="../mean_vectors/mean_vector_chv.txt"
RU_OUT="../mean_vectors/mean_vector_ru.txt"

MODEL="cis-lmu/glot500-base"
# MODEL="xlm-roberta-base"


echo "start mean vector computation for CHV"
python "$SCRIPT_PATH" \
  --input_file_path "$CHV_TRAIN" \
  --output_file_path "$CHV_OUT" \
  --model_name "$MODEL"

echo "start mean vector computation for RU"
python "$SCRIPT_PATH" \
  --input_file_path "$RU_TRAIN" \
  --output_file_path "$RU_OUT" \
  --model_name "$MODEL"

echo "end-time: $(date)"
