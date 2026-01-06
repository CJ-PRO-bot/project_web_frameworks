import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///data_prep/Titanic.db")
df = pd.read_sql("SELECT * FROM titanic_passengers", con=engine)

print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nMissing values (top):\n", df.isna().sum().sort_values(ascending=False).head(10))

print("\nSurvival rate:", df["survived"].mean())
print("\nSurvival by sex:\n", df.groupby("sex")["survived"].mean())
print("\nSurvival by class:\n", df.groupby("class")["survived"].mean())

print("\nFirst 5 rows:\n", df.head())
