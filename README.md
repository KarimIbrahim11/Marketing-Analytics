# Marketing Analytics: Customer Acquisition & Lifetime Value Study

## 📌 Project Overview
This project demonstrates a complete end-to-end marketing analytics workflow. It involves generating a medium-sized synthetic dataset (10,000+ records) using **Python**, followed by advanced data modeling and interactive visualization in **Power BI**. The primary goal is to evaluate marketing efficiency through **CAC** and long-term profitability through **CLTV**.

## 🛠️ Tech Stack
*   **Data Generation:** Python (Pandas, NumPy)
*   **Data Modeling:** Power BI (Star Schema)
*   **Analytics & Logic:** DAX (Data Analysis Expressions)
*   **Visualization:** Power BI Desktop

## 📊 Data Architecture
The project follows a **Star Schema** design to ensure optimal performance and scalability:
*   **Fact_Orders:** Contains transactional data (Revenue, Order IDs, Dates).
*   **Dim_Customers:** Stores unique customer profiles and their acquisition source.
*   **Dim_Campaigns:** Detailed records of marketing spend and channels (Facebook, Google, etc.).

---

## 📈 Dashboard Structure

### 1. Marketing Performance Dashboard (Acquisition Focus)
*Designed to monitor immediate campaign ROI and spending efficiency.*
*   **CAC (Customer Acquisition Cost):** Total Spend / New Customers Acquired.
*   **ROAS (Return on Ad Spend):** Total Revenue / Ad Spend.
*   **CPO (Cost Per Order):** Total Spend / Total Number of Orders.
*   **Visuals:** Channel-wise CAC comparison, Spend distribution, and ROAS trends.

### 2. Customer Insights Dashboard (Value & Retention Focus)
*Designed to understand the long-term value and behavior of the customer base.*
*   **CLTV (Customer Lifetime Value):** Predicting the total revenue a customer generates.
*   **AOV (Average Order Value):** Revenue / Total Orders.
*   **Purchase Frequency:** How often customers return to buy.
*   **CLTV to CAC Ratio:** The ultimate health metric (Target > 3:1).

---

## 📝 Key DAX Measures Used
```dax
// Customer Acquisition Cost
CAC = DIVIDE([Total Spend], [Total Customers], 0)

// Average Order Value
AOV = DIVIDE([Total Revenue], [Total Orders], 0)

// Historical Customer Lifetime Value
Avg CLTV = DIVIDE([Total Revenue], [Total Customers], 0)

// Return on Ad Spend
ROAS = DIVIDE([Total Revenue], [Total Spend], 0)
