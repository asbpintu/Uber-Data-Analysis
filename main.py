import pandas as pd
from pathlib import Path
from src.db_engine import get_engine
from src.utils import create_directories, read_sql_file, extract_table_name
from src.logger import setup_logger

def main():
    logger = setup_logger()
    logger.info("🚀 Extraction Process Started")

    try:
        # Step 1: Setup folders
        create_directories()
        OUT_DIR = Path("data")

        # Step 2: Connect DB
        engine = get_engine()
        logger.info("✅ Successfully Connected to SQL Server")

        # Step 3: Read SQL
        queries = read_sql_file("sql/SQLQuery.sql")
        logger.info(f"📜 Found {len(queries)} queries")

        # Step 4: Execute
        with engine.connect() as conn:
            for i, (name, query) in enumerate(queries, start=1):

                try:
                    table_name = extract_table_name(query)
                    output_name = name or table_name or f"query_{i}"

                    logger.info(f"⏳ Running query {i}: {output_name}")

                    df = pd.read_sql_query(query, conn)

                    csv_path = OUT_DIR / f"{output_name}.csv"
                    parquet_path = OUT_DIR / f"{output_name}.parquet"

                    df.to_csv(csv_path, index=False)

                    # try:
                    #     df.to_parquet(parquet_path, engine="pyarrow", index=False)
                    # except Exception:
                    #     df.to_parquet(parquet_path, engine="fastparquet", index=False)

                    logger.info(f"✅ Saved {len(df)} rows → {output_name}")

                except Exception as e:
                    logger.error(f"❌ Query {i} failed: {str(e)}")

        logger.info("🎉 Extraction Completed Successfully")

    except Exception as e:
        logger.critical(f"🔥 Fatal Error: {str(e)}")


if __name__ == "__main__":
    main()