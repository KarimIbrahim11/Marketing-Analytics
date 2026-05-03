# Data Model Documentation

This document describes the data architecture and relationships used to power the Marketing & Customer Value dashboards. The model is designed following the **Star Schema** principles to ensure high performance and accurate data filtering.

## 🏗️ Schema Architecture
The model consists of a central **Fact table** supported by **Dimension tables**, organized in a Star Schema. This structure allows for efficient aggregation of marketing costs and customer revenue across different dimensions like marketing channels.

---

## 📊 Table Descriptions

### 1. Fact_Orders (`orders`)
This is the primary transaction table containing quantitative data.
*   **Key Columns:** `order_id`, `customer_id`, `revenue`.
*   **Purpose:** Stores every individual sale, allowing for the calculation of total revenue and average order value.

### 2. Dim_Customers (`customers`)
This table acts as a bridge between marketing campaigns and specific sales.
*   **Key Columns:** `customer_id`, `campaign_id`, `acquisition_date`.
*   **Purpose:** Tracks when and through which campaign a customer was first acquired.

### 3. Dim_Campaigns (`campaigns`)
This table provides descriptive attributes for marketing efforts.
*   **Key Columns:** `campaign_id`, `channel`, `spend`.
*   **Purpose:** Stores the marketing budget spent on each channel (e.g., TikTok, Google Ads) to calculate CAC and ROAS.

### 4. Measure Table (`measure`)
*   **Purpose:** A dedicated organizational table (folder) used exclusively to store all DAX calculations (measures) in one place for better manageability.

---

## 🔗 Relationships & Cardinality

| From Table | To Table | Key | Cardinality | Direction |
| :--- | :--- | :--- | :--- | :--- |
| **campaigns** | **customers** | `campaign_id` | One-to-Many (1:*) | Single |
| **customers** | **orders** | `customer_id` | One-to-Many (1:*) | Single |

### Relationship Logic:
1.  **Campaigns to Customers:** A single marketing campaign can acquire many customers, but each customer is linked back to the specific campaign that brought them in.
2.  **Customers to Orders:** One unique customer can place multiple orders over time (enabling the calculation of Purchase Frequency and CLTV).
3.  **Filter Propagation:** Filters applied to the `channel` in the **campaigns** table will automatically flow down to filter **customers** and subsequently filter the **orders** table, ensuring consistent reporting across all visuals.

---

## ⚙️ Optimization Note
*   **Data Types:** All ID columns are set to whole numbers or text for optimized indexing.
*   **Single Direction Filters:** We use one-way filtering (from Dimensions to Facts) to prevent ambiguity in complex DAX calculations and maintain model stability.
