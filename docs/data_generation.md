# Python Logic Breakdown (Data Generation)

This document provides a technical explanation of the logic used in the `data_generator.py` script. The script's primary purpose is to create a clean, relational dataset that mirrors real-world e-commerce dynamics.

## 1. Library Selection
*   **Pandas:** Used for data structuring into DataFrames and exporting to CSV.
*   **NumPy:** Leveraged for its statistical capabilities, specifically for generating values within a normal distribution.
*   **Random/Datetime:** Used to inject variability and time-series elements into the data.

---

## 2. Structural Logic

### A. Marketing Campaign Setup
The script initializes a fixed dictionary for the `campaigns` table. This acts as the "Source of Truth" for marketing spend. 
*   **Metric Logic:** The `spend` values are hardcoded to match specific budget allocations for the four primary channels (TikTok, Google, Email, Facebook).

### B. Weighted Customer Acquisition
To simulate a successful marketing strategy, the script uses a **Weighted Random Choice** algorithm:
*   **The Logic:** Instead of assigning channels equally, specific weights (e.g., 45% for TikTok) are applied.
*   **Purpose:** This ensures that TikTok acquires the most customers for its budget, creating the "Insight" that it has a lower **CAC** compared to Facebook.

### C. Relational Mapping (Foreign Keys)
*   The script assigns a `campaign_id` to each customer. 
*   It then assigns a `customer_id` to each order. 
*   **The Logic:** By generating more orders (10,000) than customers (3,000), the script naturally creates a "One-to-Many" relationship, which is critical for testing **Purchase Frequency** calculations in Power BI.

### D. Revenue Distribution (Normal Distribution)
Instead of using completely random numbers for revenue, the script uses `np.random.normal`:
*   **Mean ($μ$):** $262$
*   **Standard Deviation ($σ$):** $50$
*   **The Logic:** This ensures most orders cluster around the $262$ mark, creating a realistic **Average Order Value (AOV)** rather than a chaotic spread of numbers.

---

## 3. Data Integrity Checks
The script is designed to prevent data "orphans":
1.  **Customer Consistency:** Every `customer_id` in the `orders` table exists in the `customers` table.
2.  **Campaign Consistency:** Every `campaign_id` in the `customers` table exists in the `campaigns` table.
3.  **Non-Negative Values:** Using `np.abs()` on revenue ensures that no transaction has a negative value, maintaining financial data integrity.

---

## 4. Analytical Goal of the Code
The code was not just written to produce data, but to produce **actionable data**. By controlling the weights and distributions, the script provides a "Ground Truth" that allows the Power BI dashboard to demonstrate a clear ROI story.
