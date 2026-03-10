#!/bin/bash
#SBATCH --job-name=PaSeMiLL_PostProcess
#SBATCH --output=slurm_postprocess_%j.out
#SBATCH --error=slurm_postprocess_%j.err
#SBATCH --time=06:00:00         
#SBATCH --gres=gpu:1             
#SBATCH --partition=lrz-hgx-a100-80x4

echo "Job gestartet auf Knoten: $(hostname)"
echo "Startzeit: $(date)"

eval "$(/dss/dsshome1/0F/ge87fen2/miniconda3/bin/conda shell.bash hook)"
conda activate pasemill_env
echo "Conda environment 'pasemill_env' activated."

echo "Starte Ausführung des Post-Processing Notebooks..."
jupyter nbconvert --to notebook --execute ../execution_notebooks/execute_postprocessing_simalign.ipynb --output ../execution_notebooks/execute_postprocessing_simalign_output.ipynb

echo "Notebook Ausführung beendet."
echo "Endzeit: $(date)"