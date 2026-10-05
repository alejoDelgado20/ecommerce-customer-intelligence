from pathlib import Path
import pandas as pd

RAW_DATA_DIR = Path("data/raw")


def load_csv(filename: str) -> pd.DataFrame:
    return pd.read_csv(RAW_DATA_DIR / filename)


def check_relationship(
    left_df,
    left_key,
    right_df,
    right_key,
    relationship_name
):
    left_values = set(left_df[left_key].dropna().unique())
    right_values = set(right_df[right_key].dropna().unique())

    missing_in_right = left_values - right_values

    print(f"\n{relationship_name}")
    print("-" * len(relationship_name))
    print(f"Unique values in left table:  {len(left_values):,}")
    print(f"Unique values in right table: {len(right_values):,}")
    print(f"Values with no match:          {len(missing_in_right):,}")

    if missing_in_right:
        print("Sample unmatched values:")
        print(list(missing_in_right)[:5])
    else:
        print("All values have a matching record.")


def main():
    customers = load_csv("olist_customers_dataset.csv")
    orders = load_csv("olist_orders_dataset.csv")
    order_items = load_csv("olist_order_items_dataset.csv")
    products = load_csv("olist_products_dataset.csv")
    sellers = load_csv("olist_sellers_dataset.csv")
    payments = load_csv("olist_order_payments_dataset.csv")
    reviews = load_csv("olist_order_reviews_dataset.csv")

    check_relationship(
        orders,
        "customer_id",
        customers,
        "customer_id",
        "Orders → Customers"
    )

    check_relationship(
        order_items,
        "order_id",
        orders,
        "order_id",
        "Order Items → Orders"
    )

    check_relationship(
        order_items,
        "product_id",
        products,
        "product_id",
        "Order Items → Products"
    )

    check_relationship(
        order_items,
        "seller_id",
        sellers,
        "seller_id",
        "Order Items → Sellers"
    )

    check_relationship(
        payments,
        "order_id",
        orders,
        "order_id",
        "Payments → Orders"
    )

    check_relationship(
        reviews,
        "order_id",
        orders,
        "order_id",
        "Reviews → Orders"
    )


if __name__ == "__main__":
    main()