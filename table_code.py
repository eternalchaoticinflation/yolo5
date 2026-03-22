# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 22:48:56 2026

@author: nothi
"""

import pandas as pd
import matplotlib.pyplot as plt

# 1) Put your lab results into a table
df = pd.DataFrame([
    {
        "Setting": "Pretrained, no training",
        "Init": "yolov8n.pt",
        "Epochs": 0,
        "P": 0.0004,
        "R": 0.0266,
        "mAP50": 0.000226,
        "mAP50-95": 0.0000826,
    },
    {
        "Setting": "Pretrained + fine-tuning",
        "Init": "yolov8n.pt",
        "Epochs": 5,
        "P": 0.938,
        "R": 0.889,
        "mAP50": 0.928,
        "mAP50-95": 0.773,
    },
    {
        "Setting": "Scratch5",
        "Init": "yolov8n.yaml",
        "Epochs": 5,
        "P": 0.695,
        "R": 0.327,
        "mAP50": 0.363,
        "mAP50-95": 0.217,
    },
    {
        "Setting": "Scratch15",
        "Init": "yolov8n.yaml",
        "Epochs": 15,
        "P": 0.746,
        "R": 0.599,
        "mAP50": 0.663,
        "mAP50-95": 0.500,
    },
])

# 2) Print it in the console
print(df.to_string(index=False))

# 3) Make a picture of the table
fig, ax = plt.subplots(figsize=(12, 2.8))
ax.axis("off")

table = ax.table(
    cellText=df.values,
    colLabels=df.columns,
    loc="center",
    cellLoc="center",
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.6)

plt.tight_layout()

# 4) Save the table picture
plt.savefig("performance_table.png", dpi=300, bbox_inches="tight")
plt.show()