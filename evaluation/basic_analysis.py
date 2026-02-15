import pandas as pd

# Simulated LLM evaluation results
results = [
    {"model": "gpt-4o-mini", "relevance_score": 82},
    {"model": "gpt-4o-mini", "relevance_score": 85},
    {"model": "gpt-4o-mini", "relevance_score": 80},
]

df = pd.DataFrame(results)

print("Evaluation Results:")
print(df)

print("\nAverage relevance score:", df["relevance_score"].mean())
print("Standard deviation:", df["relevance_score"].std())
