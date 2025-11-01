# SureFinSync

`surefinsync` is a Python utility designed to be an helper tool. If you love ~~Maybe~~ [Sure](https://github.com/we-promise/sure) as your personal finance application and it currently does not supports your banking transactions syncing though Plaid or SimpleFin then this can be a solution for you. 

The current workflow for importing multiple transactions for multiple accounts is one on one or merging it in a single output file manually keeping track of account names which can be prone to erros which I personally have done many times. So I just developed this cli application which can save your precious time and effort. Currently it can merge transaction files from multiple accounts into a standardised output. It is built to integrate smoothly into a data pipeline or financial workflow of Sure, and runs reliably in Docker.

> Note: At this stage the tool supports only the --merge operation. The --post (post transaction without importing), --categorise (auto categorise using llm) and --sync are planned for future releases.

###Features
- Merges multiple CSV transaction files into a single file (--merge).
- Maps account names to files via configuration.
- Customises transaction columns (order and naming).
- Handles files with or without a header row.
- Fully container‑ready via Docker for consistent deployment.

### Installation & Setup
#### Using Docker (recommended)
1. Clone the repository
```bash
git clone https://github.com/shrestha-bishal/surefinsync.git
cd surefinsync
```

2. Rename the .env.example to .env
```bash
mv .env.example .env
```

3. Configure .env
```bash
# Input folder containing transaction files
TRANSACTIONS_DIR=/path/to/transactions

# Output folder for merged transaction files
MERGED_TRANSACTIONS_DIR=/path/to/merged

# Account to file mapping (comma‑separated; format: AccountName:FileName)
ACCOUNT_FILE_MAPPING=Account1:file1.csv,Account2:file2.csv,Account3:file3.csv

# Transaction columns (all files should share this format)
TRANSACTION_COLUMNS=date,amount,description,balance

# Do files have header? (true/false)
HAS_HEADER=false
```

3. Build the container
```bash
docker compose build
```

4. Run the operation
```bash
docker compose run surefinsync --merge --sync
```

This mounts your input folder, processes the mapping and schema, and writes the merged output into your configured output folder.

#### Running without Docker
1. Ensure you have Python 3.12 installed.
2. Install dependencies:
```bash
pip install --no‑cache‑dir ‑r requirements.txt
```
3. Run the CLI:
```bash
python ‑m src.cli --merge
```

### Configuration Details

| Variable                  | Description                                                        |
|---------------------------|--------------------------------------------------------------------|
| `TRANSACTIONS_DIR`        | Path to folder containing all input transaction CSVs.              |
| `MERGED_TRANSACTIONS_DIR` | Path where the merged output CSV will be stored.                   |
| `ACCOUNT_FILE_MAPPING`    | Comma‑separated list of `AccountName:FileName` pairs.              |
| `TRANSACTION_COLUMNS`     | Comma‑separated list of column names (in exact order as .csv which will also be used as header).             |
| `HAS_HEADER`              | `true` if the input files include a header row, else `false`.      |


### Planned Features
`--post`: After merging, push the result into Sure.
`--categorise`: Automatically categorise transactions through LLM.
`--sync`: Maybe `--sync` or `--post`

These will be introduced in upcoming versions — please watch the repository for updates.

### Contribution
Contributions are welcome. If you find bugs, want to propose improvements, or add new features (such as --post or --categorise), please open an issue or submit a pull request. Code style aims for clarity and maintainability.

### License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for full details.

## Author

**Bishal Shrestha**  
[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?logo=github)](https://github.com/shrestha-bishal)  

© 2025 Bishal Shrestha, All rights reserved  