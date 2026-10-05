# Data Quality Report

## Dataset
Brazilian E-Commerce Public Dataset by Olist

## Objective
Evaluate the raw data before analysis and modeling.

## Initial Checks
The project includes 9 CSV files containing customers, orders, products,
payments, reviews, sellers, geolocation and order items.

## Findings

### Geolocation
- Rows: 1,000,163
- Duplicate rows: 261,831
- Missing values: 0

Observation:
The geolocation table contains a high number of duplicate rows and will
require deduplication before use.

### Order Reviews
- Rows: 99,224
- Missing values: 145,903

Observation:
The review dataset contains a significant amount of missing data.
The missingness will be analyzed by column before deciding whether to
impute, keep or remove values.

### Orders
- Rows: 99,441
- Missing values: 4,908

Observation:
Missing values are likely related to delivery or approval timestamps
and should not be removed without understanding the order lifecycle.

### Products
- Rows: 32,951
- Missing values: 2,448

Observation:
Product attributes contain missing values that may affect feature
engineering.

## Next Steps
- Analyze missing values by column
- Validate primary and foreign keys
- Deduplicate geolocation data
- Inspect date columns
- Check data types
- Build relational model
