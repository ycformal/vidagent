#!/bin/bash
#SBATCH -J vidagent             # Job name
#SBATCH -N 1                            # Number of nodes
#SBATCH -N1 --gres=gpu:1 -C H200            # Request 1 GPU
#SBATCH --mem=200G                      # Increase memory
#SBATCH -t 960                          # Duration of the job
#SBATCH -o vidagent_gpt_vote-%j.out                # Combined output and error messages file

cd $SLURM_SUBMIT_DIR                    # Correctly change to the submit directory

module load anaconda3
conda activate py39

export HF_HOME="/home/hice1/yxu846/scratch/models"

srun python main_mult_vote.py
