# CHART 1: COVID-themed cyber indicators (Jan–Apr 2020)
# Using dataset: data/Dataset1_INTERPOL.csv
# Origin/source: INTERPOL — "COVID-19 Cybercrime Analysis Report" (Aug 2020)
# Goal: Bar chart of early-pandemic indicators (spam, malware incidents, malicious URLs)
# Output file: figures/chart1_interpol_counts.png

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

data_path = Path("data") / "Dataset1_INTERPOL.csv"
df = pd.read_csv(data_path)

print(df.head())
print("rows:", len(df))

expected = {"Spam messages (COVID-related)",
            "Malware incidents (COVID-related)",
            "Malicious URLs (COVID-related)"}
have = set(df["Metric"].tolist())
missing = expected - have
if missing:
    print("Warning: missing expected metrics:", missing)


plt.figure()
plt.bar(df["Metric"], df["Value"])

plt.title("COVID-themed Cyber Indicators (Jan–Apr 2020, INTERPOL partner)")
plt.ylabel("Count")
plt.xticks(rotation=15, ha="right")

for x, v in zip(df["Metric"], df["Value"]):
    plt.text(x, v, f"{v:,}", ha="center", va="bottom", fontsize=9)

out_dir = Path("figures")
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / "chart1_interpol_counts.png"
plt.savefig(out_path, bbox_inches="tight")
plt.close()

print(f"Saved Chart 1 to: {out_path}")