#!/bin/bash
#SBATCH --job-name=PaSeMiLL_no_CBIE
#SBATCH --output=slurm_notebook_%j.out
#SBATCH --error=slurm_notebook_%j.err
#SBATCH --time=03:00:00          
#SBATCH --gres=gpu:1
#SBATCH --partition=lrz-hgx-a100-80x4
#SBATCH --mem=32G

echo "Job started on node: $(hostname)"
echo "start-time: $(date)"

source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate bachelor_thesis_env
echo "Conda environment 'bachelor_thesis_env' activated."

jupyter nbconvert --to notebook --execute ../execution_notebooks/execute_PaSeMiLL_no_CBIE.ipynb --output ../execution_notebooks/execute_PaSeMiLL_no_CBIE_output.ipynb

echo "end-time: $(date)"