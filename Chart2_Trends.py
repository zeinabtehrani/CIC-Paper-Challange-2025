# CHART 2: Healthcare cyberattack trend index before/during/after COVID (2019–2024)
# Using dataset: data/Trend_AttackIndex_2019_2024.csv
# Sources informing index:
#  - WHO news release (Apr 23, 2020): ~5x increase in attacks during early COVID.
#  - The Lancet editorial (May 25, 2024): ERCI 32 events (2022) → 121 (2023).
#  - WHO DG remarks to UN Security Council (Nov 8, 2024): sustained high threat to health sector in 2024.
# NOTE: This is an INDEX (2019 baseline = 1), not raw global counts.

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

data_path = Path("data") / "Trend_AttackIndex_2019_2024.csv"
df = pd.read_csv(data_path)

print("Preview of Chart 2 dataset:")
print(df)

plt.figure(figsize=(8,5))
plt.plot(df["Year"], df["AttackIndex"], marker="o", linestyle="-", color="tab:blue")

plt.title("Healthcare Cyberattack Trend Index (2019–2024)")
plt.xlabel("Year")
plt.ylabel("Attack Index (2019 = 1)")
plt.grid(True)

for x, y in zip(df["Year"], df["AttackIndex"]):
    plt.text(x, y+0.1, str(y), ha="center", fontsize=9)

out_path = Path("chart2_trend_index.png")
plt.savefig(out_path, dpi=300, bbox_inches="tight")
plt.show()
print(f"Chart saved to {out_path.resolve()}")

