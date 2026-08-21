import pandas as pd

def etl_pipeline():
    df = pd.read_csv("../data/raw/DataCoSupplyChainDataset.csv", encoding="ISO-8859-1", engine="python")
#clean column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("(", "")
        .str.replace(")", "")
    )
#convert date columns to datetime
    date_cols = [
        'order_date_dateorders',
        'shipping_date_dateorders',
    ]
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors='coerce')

# handle missing values
    df.loc[:, 'customer_lname'] = df['customer_lname'].fillna('Unknown')
    df.loc[:, 'customer_zipcode'] = df['customer_zipcode'].fillna(0)

# create new features
    df['shipping_delay'] = (df['days_for_shipping_real'] - df['days_for_shipment_scheduled'])
    df['order_month'] = df['order_date_dateorders'].dt.month
    df['order_weekday'] = df['order_date_dateorders'].dt.day_name()
    df['shipping_weekday'] = df['shipping_date_dateorders'].dt.day_name()
    df['high_value_order'] = df['order_item_total'] > df['order_item_total'].median()
    df['customer_full_name'] = df['customer_fname'] + ' ' + df['customer_lname']

# save cleaned data to csv
    df.to_csv("../data/cleaned/dataco_cleaned.csv", index=False)

    return df