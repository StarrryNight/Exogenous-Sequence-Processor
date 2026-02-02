import numpy as np
import os
import argparse
from data_utils import *

def parse_args():
    parser = argparse.ArgumentParser(description = "train")

    #parse arguments
    parser.add_argument("--name", type=str, default="data1")
    parser.add_argument("--chrom", type=str, required=True)
    parser.add_argument("--folder", type=str)
    parser.add_argument("--npz-fwd", type=str)
    parser.add_argument("--npz-rev", type=str)
    parser.add_argument("--fasta", type=str)
    parser.add_argument("--target-windows", type=int, default=10_000)

    return parser.parse_args()


def main():
    args = parse_args()
    if args.folder:
        res = parse_folder(args.folder)
        print(res)

if __name__ == "__main__":
    main()