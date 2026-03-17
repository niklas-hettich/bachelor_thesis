#!/bin/bash
#SBATCH --job-name=PaSeMiLL_PostProcess
#SBATCH --output=slurm_postprocess_%j.out
#SBATCH --error=slurm_postprocess_%j.err
#SBATCH --time=10:00:00         
#SBATCH --gres=gpu:1             
#SBATCH --partition=lrz-hgx-a100-80x4

echo "Job started on partition: $(hostname)"
echo "start-time: $(date)"

source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate bachelor_thesis_env
echo "Conda environment 'bachelor_thesis_env' activated."

jupyter nbconvert --to notebook --execute ../execution_notebooks/execute_postprocessing_simalign_chap_5.5.3_excl_punctuation.ipynb --output ../execution_notebooks/execute_postprocessing_simalign_chap_5.5.3_excl_punctuation_output.ipynb

echo "end-time: $(date)"