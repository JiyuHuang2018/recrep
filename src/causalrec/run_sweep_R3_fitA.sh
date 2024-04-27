#!/bin/bash
#
echo "Current directory: $(pwd)"
python -u src/causalrec/wg_fitA_py2.py -ddir "dat/proc/R3_wg/" -odir "out/R3_wg_Afit"

python -u src/causalrec/sg_fitA_py2.py -ddir "dat/proc/R3_sg/" -odir "out/R3_sg_Afit"
