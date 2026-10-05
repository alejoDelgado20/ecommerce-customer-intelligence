from pathlib import Path
import pandas as pd

RAW_DATA_DIR = Path("data/raw")


def inspect_csv(file_path: Path) -> dict:
    df = pd.read_csv(file_path)

    return {
        "file": file_path.name,
        "rows": len(df),
        "columns": len(df.columns),
        "duplicates": df.duplicated().sum(),
        "missing_values": int(df.isna().sum().sum()),
    }


def main():
    csv_files = sorted(RAW_DATA_DIR.glob("*.csv"))

    if not csv_files:
        print("No CSV files found in data/raw/")
        return

    results = [inspect_csv(file) for file in csv_files]

    summary = pd.DataFrame(results)

    print("\nDATA QUALITY SUMMARY\n")
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
    