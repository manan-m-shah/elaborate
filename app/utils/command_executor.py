import os

def clone(url, temp_folder):
    clone_command = " ".join(["git", "clone", url, temp_folder])
    os.system(clone_command)
