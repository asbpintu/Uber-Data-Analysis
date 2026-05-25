import os
import re

def create_directories():
    os.makedirs("data", exist_ok=True)
    os.makedirs("logs", exist_ok=True)


def read_sql_file(filepath):
    with open(filepath, "r") as f:
        content = f.read()

    queries = content.split(";")
    parsed = []

    for q in queries:
        q = q.strip()
        if not q:
            continue

        lines = q.split("\n")
        name = "output"

        if lines[0].startswith("--"):
            name = lines[0].replace("--", "").strip()
            query = "\n".join(lines[1:])
        else:
            query = q

        parsed.append((name, query))

    return parsed


def extract_table_name(query):
    pattern = re.compile(r"from\s+([\[\]\.\w]+)", re.IGNORECASE)
    match = pattern.search(query)

    if match:
        return match.group(1).strip().strip("[]").split(".")[-1]

    return None