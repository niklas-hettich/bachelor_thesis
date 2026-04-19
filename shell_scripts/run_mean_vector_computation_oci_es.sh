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
DATA_DIR="../data/bucc_style_data/oci-es"

OCI_TRAIN="$DATA_DIR/oci-es.train.oci"
ES_TRAIN="$DATA_DIR/oci-es.train.es"

OCI_OUT="../mean_vectors/mean_vector_oci.txt"
ES_OUT="../mean_vectors/mean_vector_es.txt"

MODEL="cis-lmu/glot500-base"
# MODEL="xlm-roberta-base"


echo "start mean vector computation for OCI"
python "$SCRIPT_PATH" \
  --input_file_path "$OCI_TRAIN" \
  --output_file_path "$OCI_OUT" \
  --model_name "$MODEL"

echo "start mean vector computation for ES"
python "$SCRIPT_PATH" \
  --input_file_path "$ES_TRAIN" \
  --output_file_path "$ES_OUT" \
  --model_name "$MODEL"

echo "end-time: $(date)"
