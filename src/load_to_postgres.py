from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

RAW_DATA_DIR = Path("data/raw")

DATABASE_URL = "postgresql+psycopg2://alejandro@localhost:5432/olist_ecommerce"

TABLES = {
    "olist_customers_dataset.csv": "customers",
    "olist_geolocation_dataset.csv": "geolocation",
    "olist_order_items_dataset.csv": "order_items",
    "olist_order_payments_dataset.csv": "order_payments",
    "olist_order_reviews_dataset.csv": "order_reviews",
    "olist_orders_dataset.csv": "orders",
    "olist_products_dataset.csv": "products",
    "olist_sellers_dataset.csv": "sellers",
    "product_category_name_translation.csv": "product_category_translation",
}


def main():
    engine = create_engine(DATABASE_URL)

    for file_name, table_name in TABLES.items():
        file_path = RAW_DATA_DIR / file_name

        print(f"Loading {file_name} -> {table_name}")

        df = pd.read_csv(file_path)

        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False,
            chunksize=5000
        )

        print(f"Loaded {len(df):,} rows into {table_name}")

    print("\nAll tables loaded successfully.")


if __name__ == "__main__":
    main()