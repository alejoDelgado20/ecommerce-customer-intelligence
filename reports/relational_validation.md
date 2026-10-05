# Relational Validation Report

## Objective
Validate referential integrity between the main Olist tables.

## Results

### Orders → Customers
- Unmatched keys: 0
- Status: Valid

### Order Items → Orders
- Unmatched keys: 0
- Status: Valid

### Order Items → Products
- Unmatched keys: 0
- Status: Valid

### Order Items → Sellers
- Unmatched keys: 0
- Status: Valid

### Payments → Orders
- Unmatched keys: 0
- Status: Valid

### Reviews → Orders
- Unmatched keys: 0
- Status: Valid

## Conclusion
No orphaned foreign keys were found in the main relational structure.

Some related tables contain fewer unique order IDs than the orders table.
This indicates that not every order necessarily has an associated item,
payment, or review record and should be considered during analysis.
