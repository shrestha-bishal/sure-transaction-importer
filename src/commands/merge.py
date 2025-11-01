import os
import pandas as pd

def run_merge():
    input_dir = os.getenv("TRANSACTIONS_DIR")
    output_dir = os.getenv("MERGED_TRANSACTIONS_DIR")
    mapping_str = os.getenv("ACCOUNT_FILE_MAPPING")
    