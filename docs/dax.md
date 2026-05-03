# DAX Measures Documentation

This document provides a comprehensive breakdown of the DAX measures used in the Marketing Analytics Power BI dashboards. These measures are essential for evaluating campaign performance, spending efficiency, and long-term customer value.

## 📊 Summary Table

| Measure Name | DAX Formula | Description |
| :--- | :--- | :--- |
| **Total Spend** | `Total Spend = SUM(campaigns[spend])` | The total budget spent across all marketing campaigns and channels. |
| **Total Revenue** | `Total Revenue = SUM(orders[revenue])` | The total gross income generated from all completed customer orders. |
| **Total Order** | `Total Order = COUNTROWS(orders)` | The total count of successful transactions recorded in the system. |
| **Total Customer** | `Total Customer = COUNTROWS(customers)` | The total number of unique customers acquired. |
| **AOV** | `AOV = DIVIDE([Total Revenue], [Total order])` | **Average Order Value:** Measures the average amount spent by a customer per transaction. |
| **Purchase Frequency** | `Purchase Frequency = DIVIDE([Total order], [Total customer])` | The average number of times a single customer makes a purchase within the period. |
| **CAC** | `CAC = DIVIDE(SUM(campaigns[spend]), COUNT(customers[customer_id]))` | **Customer Acquisition Cost:** The total cost associated with convincing a customer to buy a product/service. |
| **CLTV** | `CLTV = [AOV] * [Purchase Frequency] * 1` | **Customer Lifetime Value:** An estimate of the total revenue a business can expect from a single customer account (Annualized). |
| **CPO** | `CPO = DIVIDE([Total Spend], [Total order])` | **Cost Per Order:** The marketing cost incurred to generate a single sale. |
| **ROAS** | `ROAS = DIVIDE([Total Revenue], [Total Spend])` | **Return on Ad Spend:** Measures the efficacy of a digital advertising campaign by calculating revenue earned per dollar spent. |

---

## 💡 Implementation Details

### 1. Division Safety
All divisional measures utilize the `DIVIDE` function instead of the standard `/` operator. This ensures that the model handles **Division by Zero** errors gracefully by returning a `BLANK` or `0` instead of breaking the visual.

### 2. Data Modeling & Context
These measures are optimized for a **Star Schema** architecture. The filters flow from the Dimension tables (`Dim_Campaigns` and `Dim_Customers`) to the Fact table (`Fact_Orders`). 
*   **Relationship 1:** `Dim_Campaigns[campaign_id]` to `Dim_Customers[campaign_id]` (One-to-Many).
*   **Relationship 2:** `Dim_Customers[customer_id]` to `Fact_Orders[customer_id]` (One-to-Many).

### 3. Performance Optimization
*   **`COUNTROWS`** is preferred over `COUNT(column)` for the `Total Order` and `Total Customer` measures to provide faster calculation speeds on larger datasets.
*   **Aggregations:** Basic aggregations like `SUM` are used as the foundation for complex ratios (e.g., ROAS), following the best practice of building "Atomic Measures."

---
*Created as part of the Marketing Data Analytics Portfolio project.*
