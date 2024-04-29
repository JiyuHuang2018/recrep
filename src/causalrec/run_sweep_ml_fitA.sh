#!/bin/bash
#

python -u src/causalrec/wg_fitA_py2.py -ddir "dat/proc/ml_wg/" -odir "out/ml_wg_Afit"

python -u src/causalrec/sg_fitA_py2.py -ddir "dat/proc/ml_sg/" -odir "out/ml_sg_Afit"
