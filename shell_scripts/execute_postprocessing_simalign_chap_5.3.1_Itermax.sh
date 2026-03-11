#!/bin/bash
#SBATCH --job-name=PaSeMiLL_PostProcess
#SBATCH --output=slurm_postprocess_%j.out
#SBATCH --error=slurm_postprocess_%j.err
#SBATCH --time=10:00:00         
#SBATCH --gres=gpu:1             
#SBATCH --partition=lrz-hgx-a100-80x4

echo "Job started on partition: $(hostname)"
echo "start-time: $(date)"

eval "$(/dss/dsshome1/0F/ge87fen2/miniconda3/bin/conda shell.bash hook)"
conda activate pasemill_env
echo "Conda environment 'pasemill_env' activated."

jupyter nbconvert --to notebook --execute ../execution_notebooks/execute_postprocessing_simalign_chap_5.3.1_Itermax.ipynb --output ../execution_notebooks/execute_postprocessing_simalign_chap_5.3.1_Itermax_output.ipynb

echo "end-time: $(date)"