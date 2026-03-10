#!/bin/bash
#SBATCH --job-name=PaSeMiLL_with_CBIE
#SBATCH --output=slurm_notebook_%j.out
#SBATCH --error=slurm_notebook_%j.err
#SBATCH --time=03:00:00          
#SBATCH --gres=gpu:1
#SBATCH --partition=lrz-hgx-a100-80x4
#SBATCH --mem=32G

echo "Job gestartet auf Knoten: $(hostname)"
echo "Startzeit: $(date)"

eval "$(/dss/dsshome1/0F/ge87fen2/miniconda3/bin/conda shell.bash hook)"
conda activate pasemill_env
echo "Conda environment 'pasemill_env' activated."

echo "Starte Ausführung des Notebooks..."
/dss/dsshome1/0F/ge87fen2/miniconda3/envs/pasemill_env/bin/jupyter nbconvert --to notebook --execute ../execution_notebooks/execute_PaSeMiLL_with_CBIE.ipynb --output ../execution_notebooks/execute_PaSeMiLL_with_CBIE_output.ipynb

echo "Notebook Ausführung beendet."
echo "Endzeit: $(date)"