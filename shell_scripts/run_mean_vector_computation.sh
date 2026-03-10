#!/bin/bash
#SBATCH --job-name=MeanVecCalc
#SBATCH --output=slurm_meanvec_%j.out
#SBATCH --error=slurm_meanvec_%j.err
#SBATCH --time=00:30:00
#SBATCH --gres=gpu:1
#SBATCH --partition=lrz-hgx-a100-80x4

echo "Job started on partition: $(hostname)"
echo "start-time: $(date)"

eval "$(/dss/dsshome1/0F/ge87fen2/miniconda3/bin/conda shell.bash hook)"
conda activate pasemill_env
echo "Conda environment 'pasemill_env' activated."

SCRIPT_PATH="../mean_vectors/create_mean_vector.py"
DATA_DIR="../data/bucc_style_data/hsb-de"

HSB_TRAIN="$DATA_DIR/hsb-de.train.hsb"
DE_TRAIN="$DATA_DIR/hsb-de.train.de"

HSB_OUT="../mean_vectors/mean_vector_hsb.txt"
DE_OUT="../mean_vectors/mean_vector_de.txt"

MODEL="cis-lmu/glot500-base"
# MODEL="xlm-roberta-base"


echo "start mean vector computation for HSB"
python "$SCRIPT_PATH" \
  --input_file_path "$HSB_TRAIN" \
  --output_file_path "$HSB_OUT" \
  --model_name "$MODEL"

echo "start mean vector computation for DE"
python "$SCRIPT_PATH" \
  --input_file_path "$DE_TRAIN" \
  --output_file_path "$DE_OUT" \
  --model_name "$MODEL"

echo "computation finished."
echo "end-time: $(date)"
