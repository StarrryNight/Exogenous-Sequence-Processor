import os
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
    return {"fwd_npz": fwd,
            "rev_npz": rev,
            "fa": fa},




