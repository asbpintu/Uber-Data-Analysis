import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from urllib.parse import quote_plus

load_dotenv()

def get_engine():
    SQL_DRIVER = os.getenv("SQL_DRIVER")
    SQL_SERVER = os.getenv("SQL_SERVER")
    SQL_DATABASE = os.getenv("SQL_DATABASE")
    SQL_TRUSTED = os.getenv("SQL_TRUSTED")
    SQL_USER = os.getenv("SQL_USER")
    SQL_PASSWORD = os.getenv("SQL_PASSWORD")

    if SQL_TRUSTED or (not SQL_USER and not SQL_PASSWORD):
        odbc_str = (
            f"DRIVER={{{SQL_DRIVER}}};"
            f"SERVER={SQL_SERVER};"
            f"DATABASE={SQL_DATABASE};"
            f"Trusted_Connection=yes;"
            f"Encrypt=no;"
            f"TrustServerCertificate=yes;"
        )
    else:
        odbc_str = (
            f"DRIVER={{{SQL_DRIVER}}};"
            f"SERVER={SQL_SERVER};"
            f"DATABASE={SQL_DATABASE};"
            f"UID={SQL_USER};"
            f"PWD={SQL_PASSWORD};"
            f"Encrypt=no;"
            f"TrustServerCertificate=yes;"
        )

    connect_str = f"mssql+pyodbc:///?odbc_connect={quote_plus(odbc_str)}"

    engine = create_engine(connect_str, fast_executemany=True)

    return engine