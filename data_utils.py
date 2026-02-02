import os
import numpy as np
from dataclasses import dataclass
from Bio import SeqIO

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
    rev_seq: str = None
    length: int = 0
    start0: int = 0
    end0: int = 0

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

def extract_individual_coverage(path: str, chrom:str):
    file = np.load(path)
    return file[chrom]

def extract_coverages(source):
    source.cov_fwd = extract_individual_coverage(source.npz_fwd, source.chrom)
    source.cov_rev = extract_individual_coverage(source.npz_rev, source.chrom)
    source.length = source.cov_fwd.shape[0]
    
def extract_chr_seq(source):
    with open(source.fa_path, "rt") as fh:
        for rec in SeqIO.parse(fh, "fasta"):
            if rec.id == source.chrom:
                source.seq= str(rec.seq).upper()
                return
    raise KeyError(f"Chromosome '{source.chrom}' not found in {source.fa_path}")

def extract_rev_seq(source):
    source.rev_seq = source.seq[:-1]





