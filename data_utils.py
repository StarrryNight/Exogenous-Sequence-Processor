import os
import numpy as np
from dataclasses import dataclass


# --- Data Classes ---
@dataclass
class Source:
    name: str
    npz_fwd: str
    npz_rev: str
    chrom: str
    fa_path: str
    cov_fwd: np.ndarray = None
    cov_rev: np.ndarray = None
    seq: str = None
    start0: int = 0
    end0: int = 0
    X_fwd: np.ndarray = None
    X_rc: np.ndarray = None

def parse_folder(path: str):
    files = os.listdir(path) 
    if (len(files) == 3):
        for file in files:
            if "fwd" in file:
                fwd = path + f"/{file}"
            elif "rev" in file:
                rev = path + f"/{file}"
            elif ".fa" in file:
                fa = path + f"/{file}"
            else:
                raise "Parse folder failed! Please use file args"
    return {"npz_fwd": fwd,
            "npz_rev": rev,
            "fa": fa}

def check_numpy_validity(path: str, chrom:str):
    file = np.load(path)
    if chrom not in file:
        raise KeyError(f"invalid file {path} or chromosome {chrom}")

def check_validity(source):
    check_numpy_validity(source.npz_fwd, source.chrom)
    check_numpy_validity(source.npz_rev, source.chrom)






