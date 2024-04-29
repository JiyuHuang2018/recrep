import os
import threading
import subprocess
from queue import Queue
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
#"sg_wmf_obs", "sg_wmf_cau_ips", "sg_wmf_cau_const_add", "sg_wmf_cau_user_add", "sg_pmf_obs", "sg_pmf_cau_ips", "sg_pmf_cau_const_add", "sg_pmf_cau_user_add", "sg_pf_obs",
MODELCODEPY_SWEEP=["sg_pf_cau_ips", "sg_pf_cau_const_add", "sg_pf_cau_user_add"]
DIR_PREFIX = "dat/proc/"
DATADIR_SWEEP = ["R3_sg/"]
ODIR_PREFIX = "out/"
LOCALFITDIR_SWEEP = ["R3_sg_Afit/"]
OUTDIR_SWEEP = ["R3_sg_Yfit/"]
OUTDIM_SWEEP = [20]
CAUDIM_SWEEP = [20]
THOLD_SWEEP = [2]
BATCHSIZE_SWEEP = [100]
NITER_SWEEP = [500]
PRIORU_SWEEP = [1, 10]
PRIORV_SWEEP = [1, 10]
ALPHA_SWEEP = [40]
BINARY_SWEEP = [0]

SUFFIX = ".py"
DATA = "R3"


print_lock = threading.Lock()

def safe_print(*args, **kwargs):
    with print_lock:
        print(*args, **kwargs)
        sys.stdout.flush()

# Worker function for threads
def thread_worker():
    while True:
        parameters = q.get()
        if parameters is None:
            break  # No more work to do

        safe_print("Task started with parameters:", parameters)
        run_script(*parameters)
        q.task_done()
        safe_print("Task completed with parameters:", parameters)
        
# Define the function to run the script
def run_script(MODELCODEPYi, DATADIRi, LOCALFITDIRi, OUTDIRi, OUTDIMi, CAUDIMi, THOLDi, BATCHSIZEi, NITERi, PRIORUi, PRIORVi, ALPHAi, BINARYi):
    NAME = f"data_{DATADIRi}_model_{MODELCODEPYi}_odim_{OUTDIMi}_cdim_{CAUDIMi}_th_{THOLDi}_M_{BATCHSIZEi}_nitr_{NITERi}_pU_{PRIORUi}_pV_{PRIORVi}_alpha_{ALPHAi}_binary_{BINARYi}"
    print(NAME)
    # Execute the script here using subprocess or os.system
    try:
        result = subprocess.run([
            "python", "-u",
            f"src/causalrec/{MODELCODEPYi}{SUFFIX}",
            "-ddir", f"{DIR_PREFIX}{DATADIRi}/",
            "-cdir", f"{ODIR_PREFIX}{LOCALFITDIRi}",
            "-odir", f"{ODIR_PREFIX}{OUTDIRi}",
            "-odim", str(OUTDIMi),
            "-cdim", str(CAUDIMi),
            "-th", str(THOLDi),
            "-M", str(BATCHSIZEi),
            "-nitr", str(NITERi),
            "-pU", str(PRIORUi),
            "-pV", str(PRIORVi),
            "-alpha", str(ALPHAi),
            "-binary", str(BINARYi)
        ], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        
        # Print the stdout of the script
        safe_print(f"Output of {NAME}:\n{result.stdout}")
        
    except subprocess.CalledProcessError as e:
        # Print the error message from the script
        safe_print(f"Error in {NAME}: {e.stderr}")
q = Queue()

# Launch a pool of threads, and pass them queue instance
for _ in range(10):  # Adjust the number of concurrent threads
    t = threading.Thread(target=thread_worker)
    t.start() 
# Create threads for each combination of parameters

for MODELCODEPYi in MODELCODEPY_SWEEP:
    for DATADIRi in DATADIR_SWEEP:
        for LOCALFITDIRi in LOCALFITDIR_SWEEP:
            for OUTDIRi in OUTDIR_SWEEP:
                for OUTDIMi in OUTDIM_SWEEP:
                    for CAUDIMi in CAUDIM_SWEEP:
                        for THOLDi in THOLD_SWEEP:
                            for BATCHSIZEi in BATCHSIZE_SWEEP:
                                for NITERi in NITER_SWEEP:
                                    for PRIORUi in PRIORU_SWEEP:
                                        for PRIORVi in PRIORV_SWEEP:
                                            for ALPHAi in ALPHA_SWEEP:
                                                for BINARYi in BINARY_SWEEP:
                                                    q.put((MODELCODEPYi, DATADIRi, LOCALFITDIRi, OUTDIRi, OUTDIMi, CAUDIMi, THOLDi, BATCHSIZEi, NITERi, PRIORUi, PRIORVi, ALPHAi, BINARYi))

q.join()                                               
for _ in range(10):  # Adjust the number of concurrent threads
    q.put(None)