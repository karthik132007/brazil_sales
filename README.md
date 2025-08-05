

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

📊 Phase 2: Data Visualization – Olist E-commerce Dataset
🎯 Objective
To explore insights and uncover patterns in the cleaned Olist dataset using various types of visualizations. This helps in understanding customer behavior, product dynamics, and overall e-commerce performance in Brazil.

🔍 Steps Performed
Library Imports
Imported essential Python libraries:

pandas for data manipulation

matplotlib and seaborn for visualizations

(Include any others if used like plotly, numpy, datetime, etc.)

Exploratory Plots

Created different plots to analyze trends and relationships across key features:

📦 Top Selling Product Categories

Bar plot showing top categories by number of orders.

🌍 Orders by Customer State

Bar chart mapping customer states to total orders.

💸 Payment Type Distribution

Pie or bar chart showing proportion of payment methods.

🕒 Monthly Order Volume

Time-series line plot of orders over months or years.

⚖️ Price vs Freight Value

Scatter plot to see correlation between product price and freight value.

🛍️ Top Sellers by Order Count

Bar plot of sellers with highest number of orders.

📏 Product Volume vs Review Score

Box plot to analyze if bulky items get lower/higher review scores.

⭐ Review Score Distribution

Histogram of review scores to check overall customer satisfaction.

Advanced Groupings and Aggregations

Grouped data by customer_state, product_category, review_category, etc. for insightful summaries.

Aggregated key metrics like average payment_value, freight_value, and review_score.

Plot Styling & Customizations

Applied consistent color palettes, titles, axis labels, and rotated tick labels for readability.

Used tight layouts and legends where necessary for presentation-ready output.

📌 Insights Gained
Certain product categories dominate sales.

Some states have significantly more customer activity.

“Credit card” is the overwhelmingly popular payment method.

There is a visible seasonality or growth trend in order volume over time.

Freight value increases with product price—but not always proportionally.

Some sellers consistently generate high order volumes (ideal for marketing focus).

Low product review scores can correlate with larger/heavier items, possibly due to delivery issues.
