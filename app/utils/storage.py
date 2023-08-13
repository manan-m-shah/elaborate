import os
import tempfile

def get_new_temp_dir():
    return tempfile.mkdtemp()