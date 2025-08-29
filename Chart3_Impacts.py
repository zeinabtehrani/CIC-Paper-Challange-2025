# CHART 3: Impact profile of major healthcare cyberattacks (2020–2024)
# Using dataset: Data/CaseImpacts_2020_2024.csv
# Flags encoded per case: Disruption, DataExfiltration, RansomPaidReported, NationalScale
# Sources (see paper refs): ICRC blog (Brno), WIRED (Düsseldorf), WHO DG to UN SC (HSE),
# The Lancet editorial (Change Healthcare), Sangfor blog (Lurie, Ascension, Synnovis)

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

data_path = Path("Data") / "CaseImpacts_2020_2024.csv"   
df = pd.read_csv(data_path)

print("Preview:")
print(df)

df = df.sort_values(["Year", "Case"]).reset_index(drop=True)

flags = ["Disruption", "DataExfiltration", "RansomPaidReported", "NationalScale"]

flag_colors = {
    "Disruption":           "#1f77b4",  # blue
    "DataExfiltration":     "#ff7f0e",  # orange
    "RansomPaidReported":   "#2ca02c",  # green
    "NationalScale":        "#d62728",  # red
}


fig, ax = plt.subplots(figsize=(9, 5.5))

y_positions = range(len(df))
ax.set_yticks(list(y_positions))
ax.set_yticklabels(df["Case"])

for i, row in df.iterrows():
    left = 0  
    for f in flags:
        val = int(row[f])  
        if val == 1:
            ax.barh(i, 1, left=left, color=flag_colors[f], edgecolor="white")
            
            ax.text(left + 0.5, i, f, va="center", ha="center", fontsize=8, color="white", weight="bold")
            left += 1
        else:
            pass


ax.set_xlabel("Impact score (count of present flags)")
ax.set_xlim(0, 4)  
ax.grid(axis="x", linestyle=":", alpha=0.4)
ax.invert_yaxis()  

handles = [plt.Line2D([0],[0], color=flag_colors[f], lw=10) for f in flags]
ax.legend(handles, flags, title="Impact flags", loc="upper right", frameon=False)


ax.set_title("Impact Profile of Major Healthcare Cyberattacks (2020–2024)")


foot = (
    "Dataset: Data/CaseImpacts_2020_2024.csv | Flags: Disruption, DataExfiltration, RansomPaidReported, NationalScale\n"
    "Sources: ICRC (Brno), WIRED (Düsseldorf), WHO DG to UN Security Council (HSE), The Lancet (Change Healthcare), "
    "Sangfor (Lurie, Ascension, Synnovis)."
)
plt.figtext(0.01, -0.02, foot, ha="left", va="top", fontsize=8)


out_path = Path("chart3_case_impacts.png")
plt.tight_layout()
plt.savefig(out_path, dpi=300, bbox_inches="tight")
plt.show()
print(f"Chart saved to {out_path.resolve()}")

