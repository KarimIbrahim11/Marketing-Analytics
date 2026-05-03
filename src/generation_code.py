import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Set seed for reproducibility to ensure the same results every time the script runs
np.random.seed(42)

def generate_marketing_data():
    """
    Generates a synthetic marketing dataset including campaigns, customers, and orders.
    This data is designed to simulate realistic CAC, ROAS, and CLTV metrics.
    """
    
    # 1. Generate Campaigns Table
    # Defining specific spend for each channel to test different ROAS scenarios
    campaign_data = {
        'campaign_id': [1, 2, 3, 4],
        'channel': ['TikTok Ads', 'Google Ads', 'Email Marketing', 'Facebook Ads'],
        'spend': [25120.97, 3038.60, 26409.95, 21126.33]
    }
    df_campaigns = pd.DataFrame(campaign_data)

    # 2. Generate Customers Table (3,000 customers)
    # Using weighted random choice to simulate TikTok as the most efficient acquisition channel
    customer_ids = range(1, 3001)
    channels_pool = random.choices(
        [1, 2, 3, 4], 
        weights=[0.45, 0.05, 0.30, 0.20], # TikTok (45%) vs Google (5%)
        k=3000
    )

    df_customers = pd.DataFrame({
        'customer_id': customer_ids,
        'campaign_id': channels_pool,
        'acquisition_date': [
            datetime(2025, 1, 1) + timedelta(days=np.random.randint(0, 365)) 
            for _ in range(3000)
        ]
    })

    # 3. Generate Orders Table (10,000 orders)
    # Creating a 1:N relationship (one customer to many orders) to calculate Purchase Frequency
    order_ids = range(1, 10001)
    order_customers = [random.choice(customer_ids) for _ in range(10000)]
    
    # Using Normal Distribution for Revenue (Mean=262, StdDev=50) to simulate realistic AOV
    revenue = np.random.normal(262.06, 50, 10000) 

    df_orders = pd.DataFrame({
        'order_id': order_ids,
        'customer_id': order_customers,
        'revenue': np.abs(revenue).round(2) # Ensure positive values and clean decimals
    })

    return df_campaigns, df_customers, df_orders

if __name__ == "__main__":
    # Execute generation
    campaigns, customers, orders = generate_marketing_data()

    # Save files to CSV for Power BI consumption
    campaigns.to_csv('campaigns.csv', index=False)
    customers.to_csv('customers.csv', index=False)
    orders.to_csv('orders.csv', index=False)

    print("✅ Success: Data files generated (campaigns.csv, customers.csv, orders.csv)")
