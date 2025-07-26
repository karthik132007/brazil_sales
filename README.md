

# Phase 1: Data Cleaning – Olist E-commerce Dataset

## Objective

Prepare a clean, structured dataset from the raw Olist Brazilian e-commerce data for analysis and visualization.


## Steps Performed

### 1. **Data Loading**

* Loaded all required CSV files:

  * Orders, Customers, Order Items, Payments, Products, Sellers, and Reviews.
* Merged them into a single `master` DataFrame using appropriate keys (`order_id`, `customer_id`, etc.).

### 2. **Column Selection**

* Extracted only necessary columns for analysis:

  ```
  order_id, order_purchase_timestamp, price, freight_value,
  payment_value, payment_type, customer_state, seller_state,
  product_category_name, product_weight_g, product_length_cm,
  product_height_cm, product_width_cm, review_score
  ```

### 3. **Missing Value Handling**

* **Numeric columns** (`price`, `freight_value`, `payment_value`, product dimensions, weights):

  * Filled missing values with column mean.
* **Categorical columns**:

  * `product_category_name`: replaced `NaN` → `"Others"`.
  * `seller_state`: replaced `NaN` → `"Others"`.
  * `payment_type`: (if missing) handled later with mode.

### 4. **Feature Engineering**

* Created **`product_volume`**:

  ```
  product_volume = length_cm × width_cm × height_cm
  ```
* Dropped the original dimension columns (`length`, `width`, `height`) after creating volume.

### 5. **State Mapping**

* Converted Brazilian state abbreviations (`SP`, `RJ`, etc.) to full names using a dictionary.
* Preserved `"Others"` as a placeholder for unknown/missing sellers.

### 6. **Review Score Processing**

* Filled missing review scores.
* Converted `review_score` to integers.
* Created a new column `review_category`:

  * `0–2 → Bad`
  * `3 → Average`
  * `4–5 → Good`

---

## ⚠️ Notes

* After merging, the dataset is **large**; aggregation may be needed in later phases.
* `seller_state` mapping can generate `NaN` if unexpected codes exist; handled by fallback fill.
* Non-integer review scores were rounded before converting to `int`.

---


