# Uber Data Analysis

Comprehensive analysis of Uber trip data. Data for this project was collected from a SQL Server instance and analyzed with Python and Power BI to produce interactive dashboards and visualizations.

Power BI Dashboard: [Power BI Link Updated](https://app.powerbi.com/view?r=eyJrIjoiNGEyNzQ0ODgtMzg4Ni00ZWZjLThmZjQtMjI2ZmRhYWVmNTI5IiwidCI6ImJjMmRjNzNhLWZhM2QtNGNiZS1iZGM4LWI0NjhjNDY0NjM2ZiJ9)

## Project Overview

- **Goal:** Explore and visualize Uber trip patterns, demand hotspots, temporal trends, and driver/ride-level metrics to inform business insights.
- **Scope:** ETL from SQL Server, data cleaning, exploratory analysis, feature engineering, and interactive reporting with Power BI.

## Data Source

- **Origin:** Extracted from an internal SQL Server database (production/development) using authenticated connections.
- **Extraction:** SQL queries are stored in `SQLQuery1.sql` and other query files. Data was exported to CSV/Parquet when needed for repeatable analysis.
- **Note:** Do NOT commit credentials. Use environment variables or OS-authenticated connections for production use.

## Dataset & Schema (summary)

- Typical tables used:
	- `trips` — ride-level records (pickup_datetime, dropoff_datetime, pickup_location_id, dropoff_location_id, fare, tip, distance)
	- `drivers` — driver metadata (driver_id, start_date, rating)
	- `zones` — geographic reference (location_id, borough, zone_name, lat, lon)

- If you need the exact schema, run the provided SQL queries in `SQLQuery1.sql` against your database.

## Key Analysis Steps

1. Connect to SQL Server and extract required tables using parameterized queries.
2. Perform data cleaning: handle missing timestamps, normalize timezones, filter test rows, and cast data types.
3. Feature engineering: derive trip duration, surge flags, hour-of-day, weekday, and geospatial joins to `zones`.
4. Aggregate and visualize: time series of demand, heatmaps of pickup density, cohort analyses, and revenue breakdowns.

## Reproducibility / How to Run

1. Create a Python environment (recommended: venv or conda) and install requirements:

```bash
python -m venv .venv
source .venv/Scripts/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

2. Provide SQL Server connection details via environment variables (recommended):

- `SQL_SERVER` — hostname or IP
- `SQL_DATABASE` — database name
- `SQL_USER` — username (omit if using integrated auth)
- `SQL_PASSWORD` — password (omit if using integrated auth)
- Or use a DSN / trusted connection. Example connection strings are shown in notebooks but contain no secrets.

3. Run extraction script or Jupyter notebook to pull data from SQL Server:

```bash
python scripts/extract_from_sql.py    # or open notebooks/Extraction.ipynb
jupyter notebook                     # run notebooks interactively
```

4. Open `notebooks/Analysis.ipynb` to reproduce the analysis and regenerate figures and aggregated datasets used by Power BI.

## Requirements

- Python 3.9+ (recommended)
- Key packages: `pandas`, `numpy`, `sqlalchemy`, `pyodbc` (or `pymssql`), `matplotlib`, `seaborn`, `jupyter`.
- See `requirements.txt` for the full pinned list.

## File Structure

- `SQLQuery1.sql` — primary SQL extraction queries
- `notebooks/` — exploratory notebooks (Extraction.ipynb, Analysis.ipynb)
- `scripts/` — utility scripts for extraction, cleaning, and export
- `Images/` — static images used in this repo and report
- `README.md` — this file

If you add notebooks or scripts, please update this list accordingly.

## Findings (high-level)

- Peak demand occurs during weekday rush hours and weekend evenings in downtown zones.
- Average trip duration and fare vary significantly by zone and hour-of-day.
- Visualizations and drill-downs are available in the Power BI dashboard linked above.

## Privacy & Security

- This repository does not include production credentials or PII. When sharing derived datasets, ensure they are anonymized and aggregated to prevent leakage of sensitive user information.

## Next Steps

- Add `requirements.txt` with pinned package versions.
- Add `scripts/extract_from_sql.py` and `notebooks/Extraction.ipynb` if not present.
- Add a short CONTRIBUTING guide for dataset updates and refresh cadence.

## License & Contact

This repository follows the license defined in `LICENSE` at the project root. For questions or access requests, contact the project owner.

---

If you'd like, I can also:
- add a `requirements.txt` and an `extract_from_sql.py` template that uses environment variables, or
- create a reproducible Jupyter notebook that demonstrates the full extraction → cleaning → analysis workflow.
