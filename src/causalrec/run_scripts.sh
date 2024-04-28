#!/bin/bash

#SBATCH --account=sml
#SBATCH -c 4
#SBATCH --time=11:00:00
#SBATCH --mem-per-cpu=32gb

source /c/Users/huang/anaconda3/etc/profile.d/conda.sh
conda activate python36

python -u src/causalrec/${MODELCODEPY} -ddir ${DATADIR} -cdir ${LOCALFITDIR} -odir ${OUTDIR} -odim ${OUTDIM} -cdim ${CAUDIM} -th ${THOLD} -M ${BATCHSIZE} -nitr ${NITER} -pU ${PRIORU} -pV ${PRIORV} -alpha ${ALPHA} -binary ${BINARY}