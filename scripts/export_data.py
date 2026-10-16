import os, json, pymssql

conn = pymssql.connect(
    server=os.environ["SQL_SERVER"],
    user=os.environ["SQL_USER"],
    password=os.environ["SQL_PASSWORD"],
    database=os.environ["SQL_DB"],
)
cur = conn.cursor(as_dict=True)
cur.execute("SELECT * FROM dbo.azureKnowledgeQuery")
rows = cur.fetchall()
conn.close()

os.makedirs("data", exist_ok=True)
with open("data/chart.json", "w") as f:
    json.dump(rows, f, default=float)
