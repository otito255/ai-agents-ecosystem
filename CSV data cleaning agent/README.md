# CSV Data Cleaning Pipeline

A simple Python tool to clean CSV files by removing duplicates, fixing dates, and validating data ranges.

## What It Does

- Removes duplicate rows
- Detects missing values
- Fixes date formatting
- Validates age (0-120 years)
- Creates a quality report

## Installation

```bash
pip install pandas openai
```

## Usage

1. Place your CSV file named `raw_data.csv` in the same folder as the script
2. Run the script:
   ```bash
   python script.py
   ```
3. Get two output files:
   - `cleaned_data.csv` — your cleaned data
   - `data_quality_report.json` — what issues were found

## Input File Format

Your CSV needs these columns:
- `signup_date` — any date format (e.g., 2024-01-15, 01/15/2024)
- `age` — number between 0-120
- Other columns — anything you want

**Example:**
```csv
id,name,age,signup_date,email
1,Alice,28,2023-03-15,alice@example.com
2,Bob,-5,2023-05-20,bob@example.com
3,Alice,28,2023-03-15,alice@example.com
```

## Output Files

### cleaned_data.csv
Your data after cleaning. Invalid ages become blank, bad dates become `NaT`.

```csv
id,name,age,signup_date,email
1,Alice,28.0,2023-03-15,alice@example.com
2,Bob,,2023-05-20,bob@example.com
3,Alice,28.0,2023-03-15,alice@example.com
```

### data_quality_report.json
A summary of what was cleaned:
```json
{
  "date": "2024-01-14",
  "issues_detected": [
    {
      "missing_values": {
        "age": 1,
        "signup_date": 0
      }
    },
    {
      "duplicates_removed": 1
    },
    {
      "invalid_age_rows": [1]
    }
  ]
}
```

## How to Customize

### Change age range
Edit line in `clean_data()`:
```python
# Default: 0-120
invalid_age = df[(df["age"] < 0) | (df["age"] > 120)]

# Change to: 18-65
invalid_age = df[(df["age"] < 18) | (df["age"] > 65)]
```

### Change input/output filenames
Edit the `main()` function:
```python
df = load_csv(path="my_data.csv")  # Change input file
```

## Common Issues

| Problem | Solution |
|---------|----------|
| `FileNotFoundError` | Put CSV file in same folder as script |
| `KeyError: 'age'` | Your CSV must have an `age` column |
| `KeyError: 'signup_date'` | Your CSV must have a `signup_date` column |
| Can't write files | Check folder permissions |

## Example: Process Multiple Files

```python
import os
from script import load_csv, clean_data, save_outputs

for filename in os.listdir("raw_data"):
    if filename.endswith(".csv"):
        df = load_csv(f"raw_data/{filename}")
        cleaned_df, issues = clean_data(df)
        save_outputs(cleaned_df, issues)
        print(f"✓ {filename} done")
```

## Functions

**`load_csv(path)`** — Load a CSV file  
**`clean_data(df)`** — Clean the data, return (cleaned_df, issues)  
**`save_outputs(df, issues)`** — Save cleaned data and report  
**`main()`** — Run the full pipeline  

## Tips

- Always backup your original CSV first
- Check `data_quality_report.json` to see what changed
- Test on a small sample before cleaning large files
- Review the cleaned data before using it