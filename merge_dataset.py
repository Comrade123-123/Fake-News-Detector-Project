import pandas as pd

# Load both datasets
fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

# Add a new column "label"
fake["label"] = "FAKE"
true["label"] = "REAL"

# Combine datasets
df = pd.concat([fake, true], axis=0)

# Save merged dataset
df.to_csv("fake_news.csv", index=False)

print("✅ fake_news.csv created successfully!")
print(df.head())
