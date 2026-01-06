from sqlalchemy import create_engine
import seaborn as sns

def main():
    df = sns.load_dataset("titanic")

    engine = create_engine("sqlite:///data_prep/Titanic.db")
    df.to_sql("titanic_passengers", con=engine, if_exists="replace", index=False)

    print("✅ Database created: data_prep/Titanic.db")
    print("✅ Table created: titanic_passengers")
    print("✅ Rows loaded:", len(df))
    print(df.head())

if __name__ == "__main__":
    main()
