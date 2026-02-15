"""
Simple evaluation script for LLM prompt outputs.

This script demonstrates how quantitative evaluation
could be applied to LLM responses in a reproducible way.
"""

import pandas as pd

# Sample test data
data = [
    {
        "resume": "Data analyst with Python, SQL, Tableau",
        "job": "Junior data analyst role requiring Python and SQL",
        "model_output_score": 85
    },
    {
        "resume": "Marketing specialist with SEO experience",
        "job": "Data analyst with Python and statistics",
        "model_output_score": 30
    }
]

df = pd.DataFrame(data)

# Simple quantitative analysis
average_score = df["model_output_score"].mean()
std_dev_score = df["model_output_score"].std()

print("Evaluation Results")
print("------------------")
print(df)
print("\nAverage relevance score:", round(average_score, 2))
print("Score standard deviation:", round(std_dev_score, 2))
