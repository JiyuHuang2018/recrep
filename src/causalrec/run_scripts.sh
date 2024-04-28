#!/bin/bash

#SBATCH --account=sml
#SBATCH -c 4
#SBATCH --time=11:00:00
#SBATCH --mem-per-cpu=32gb
export PYTHONIOENCODING=utf8
source /c/Users/huang/anaconda3/etc/profile.d/conda.sh
conda activate python36
echo "${MODELCODEPY}"
echo "${DATADIR} "
echo "${LOCALFITDIR}"
echo "odir ${OUTDIR}"
echo "odim ${OUTDIM}"
echo "-cdim ${CAUDIM} "
echo "th ${THOLD}"
echo "-M ${BATCHSIZE}"
echo "-nitr ${NITER}"
echo "pU ${PRIORU}"
echo "pV ${PRIORV}"
echo "alpha ${ALPHA}"
echo "-binary ${BINARY}"

python -u src/causalrec/${MODELCODEPY} -ddir ${DATADIR} -cdir ${LOCALFITDIR} -odir ${OUTDIR} -odim ${OUTDIM} -cdim ${CAUDIM} -th ${THOLD} -M ${BATCHSIZE} -nitr ${NITER} -pU ${PRIORU} -pV ${PRIORV} -alpha ${ALPHA} -binary ${BINARY}