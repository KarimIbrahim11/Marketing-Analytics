# Marketing Analytics: Customer Acquisition & Lifetime Value Study

## 📌 Project Overview
This project demonstrates a complete end-to-end marketing analytics workflow. It involves generating a medium-sized synthetic dataset (10,000+ records) using **Python**, followed by advanced data modeling and interactive visualization in **Power BI**. The primary goal is to evaluate marketing efficiency through **CAC** and long-term profitability through **CLTV**.

## 📂 Project Structure & Navigation

Explore the different components of this project through the links below:

### 🚀 Core Source Code
*   **[📁 src/](./src)**: Contains the primary Python scripts.
    *   **[generation_code.py](./src/generation_code.py)**: The core engine used to programmatically generate the relational marketing dataset.

### 📖 Documentation & Technical Logic
*   **[📁 docs/](./docs)**: Detailed explanations of the project's technical and analytical framework.
    *   **[Data Generation Logic](./docs/data_generation.md)**: Explains the Python algorithms and statistical distributions used to create realistic data.
    *   **[Data Model Architecture](./docs/data_model.md)**: Describes the Star Schema design and how the tables relate to one another.
    *   **[DAX Measures](./docs/dax.md)**: A complete reference for the formulas used to calculate KPIs like CAC, CLTV, and ROAS.
    *   **[Business Insights & Recommendations](./docs/Insights.md)**: A deep dive into the analytical findings and data-driven strategic advice.

### 📊 Visual Assets
*   **[📁 Images/](./Images)**: High-resolution screenshots of the final outputs.
    *   **[Marketing & Acquisition Dashboard](./Images/Marketing%20&%20Acquisition%20Dashboard.png)**: Visualizing channel efficiency and spend.
    *   **[Customer Value Dashboard](./Images/Customer%20Value%20Dashboard.png)**: Visualizing retention, AOV, and lifetime value.
    *   **[Data Model View](./Images/data%20model.png)**: A technical snapshot of the Power BI relationship diagram.

### 📈 Power BI File
*   **[📁 PowerBI Project/](./PowerBI%20Project)**: Contains the raw `.pbix` file for local exploration and interactive filtering.


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
