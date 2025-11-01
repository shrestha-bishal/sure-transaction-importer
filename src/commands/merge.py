import os
import pandas as pd
from datetime import datetime

def run_merge():
    input_dir = os.getenv("TRANSACTIONS_DIR")
    output_dir = os.getenv("MERGED_TRANSACTIONS_DIR")
    mapping_str = os.getenv("ACCOUNT_FILE_MAPPING")
    columns_str = os.getenv("TRANSACTION_COLUMS")
    has_header_str = os.getenv("HAS_HEADER", "true").lower()

    has_header = has_header_str == "true"

    if not input_dir:
        print("Error: TRANSACTIONS_DIR is not set in the .env")
        return
    if not output_dir:
        print("Error: MERGED_TRANSACTIONS_DIR is not set in the .env")
        return
    if not columns_str:
        print("Error: TRANSACTION_COLUMNS not set in .env")
        return
    
    # parse account-to-file mapping
    account_mapping = {}
    for pair in mapping_str.split(","):
        if ":" in pair:
            account, filename = pair.split(":")
            account_mapping[account.strip()] = filename.strip()

    if not account_mapping:
        print("Error: ACCOUNT_FILE_MAPPINGS is empty or invalid in .env")
        return
    
    # parse transaction columns
    transaction_columns = [c.strip() for c in columns_str.split(",")]

    merged = pd.DataFrame(columns=transaction_columns + ["account_name"])

    for account, filename in account_mapping.items():
        file_path = os.path.join(input_dir, filename)

        # checking if the file exists
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue

        try:
            # read the file depending on type and header setting
            if file_path.endswith(".csv"):
                df = pd.read_csv(file_path, skiprows=1 if has_header else 0, header=None)
            elif file_path.endswith(".xlsx"):
                df = pd.read_excel(file_path, skiprows=1 if has_header else 0, header=None)
            else: 
                print(f"Unsupported file type: {filename}")
                continue

            df.columns = transaction_columns
            df["account_name"] = account

            merged = pd.contact([merged, df], ignore_index=True)

        except Exception as e:
            print(f"Error reading file {filename}: {e}")

    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    output_filename = f"merged_transactions_{timestamp}.csv"
    output_file = os.path.join(output_dir, output_filename)
    merged.to_csv(output_file, index=False)
    print(f"Merged file saved to {output_file}")