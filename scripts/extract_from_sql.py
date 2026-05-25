import os
import re
import sys
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

# Local SQL Server defaults. Override with environment variables if needed.
SQL_SERVER = os.getenv("SQL_SERVER")
SQL_DATABASE = os.getenv("SQL_DATABASE")
SQL_USER = os.getenv("SQL_USER")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")
DRIVER = os.getenv("SQL_DRIVER", "ODBC Driver 18 for SQL Server")
TRUSTED = os.getenv("SQL_TRUSTED", "True").lower() in ("1", "true", "yes")

if not SQL_DATABASE:
    print("Error: SQL_DATABASE is required for the local SQL Server connection.")
    print("Set SQL_DATABASE in your environment or .env file to the target database name.")
    sys.exit(1)

OUT_DIR = Path("data")
OUT_DIR.mkdir(exist_ok=True)

QUERY_FILE = Path("SQLQuery1.sql")
if not QUERY_FILE.exists():
    print(f"Query file {QUERY_FILE} not found. Please create or update it.")
    sys.exit(1)

raw_sql = QUERY_FILE.read_text()
statements = [stmt.strip() for stmt in raw_sql.split(";") if stmt.strip()]
select_statements = [stmt for stmt in statements if stmt.lower().startswith("select")]

if not select_statements:
    print("No SELECT statements found in SQLQuery1.sql. Please add one or more queries to extract tables.")
    sys.exit(1)

if TRUSTED or (not SQL_USER and not SQL_PASSWORD):
    connect_str = (
        f"mssql+pyodbc://{SQL_SERVER}/{SQL_DATABASE}"
        f"?driver={DRIVER.replace(' ', '+')};trusted_connection=yes"
    )
else:
    connect_str = (
        f"mssql+pyodbc://{SQL_USER}:{SQL_PASSWORD}@{SQL_SERVER}/{SQL_DATABASE}"
        f"?driver={DRIVER.replace(' ', '+')}"
    )

print(f"Connecting to local SQL Server at {SQL_SERVER}")
engine = create_engine(connect_str, fast_executemany=True)

pattern = re.compile(r"from\s+([\[\]\.\w]+)", flags=re.IGNORECASE)

with engine.connect() as conn:
    for index, statement in enumerate(select_statements, start=1):
        table_name = None
        match = pattern.search(statement)
        if match:
            table_name = match.group(1).strip().strip("[]").split(".")[-1]

        output_base = f"extracted_{table_name or index}"
        print(f"Running query {index}: saving data to {output_base}.csv / parquet")

        df = pd.read_sql_query(statement, conn)
        csv_path = OUT_DIR / f"{output_base}.csv"
        parquet_path = OUT_DIR / f"{output_base}.parquet"

        df.to_csv(csv_path, index=False)
        try:
            df.to_parquet(parquet_path, engine="pyarrow", index=False)
        except Exception:
            df.to_parquet(parquet_path, engine="fastparquet", index=False)

        print(f"Saved {len(df)} rows for {output_base}")

print("Extraction complete.")
