import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import mysql.connector
from sqlalchemy import create_engine
from urllib.parse import quote_plus

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="WJ28@Krhps",
    database="customer_behavior"
)

print("MySQL Connected")

password = quote_plus("WJ28@Krhps")

engine = create_engine(
    f"mysql+mysqlconnector://root:{password}@localhost/customer_behavior"
)

df = pd.read_csv('customer_shopping_behavior.csv')

print(df.columns.tolist())
print(df.head())
print(df.info())

numeric_df = df.select_dtypes(include=['int64', 'float64'])

plt.figure(figsize=(10, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

print(df.describe(include='all'))
print(df.isnull().sum())

if 'Review_Rating' in df.columns and 'Category' in df.columns:
    df['Review_Rating'] = df.groupby('Category')['Review_Rating'].transform(
        lambda x: x.fillna(x.mean())
    )

print(df['Review_Rating'])

labels = ['young adults', 'adults', 'middle-aged', 'seniors']

if 'Age' in df.columns:
    df['age_group'] = pd.qcut(
        df['Age'],
        q=4,
        labels=labels,
        duplicates='drop'
    )

    print("AGE GROUP CREATED")
    print(df['age_group'].value_counts())

frequency_mapping = {
    'fortnightly': 14,
    'weekly': 7,
    'monthly': 30,
    'quarterly': 90,
    'bi-weekly': 14,
    'annually': 365,
    'every 3 months': 90
}

freq_col = None

for col in df.columns:
    if 'frequency' in col.lower():
        freq_col = col
        break

if freq_col:
    df[freq_col] = df[freq_col].astype(str).str.lower().str.strip()

    df['Purchase_Frequency_Days'] = df[freq_col].map(
        frequency_mapping
    )

    print(df[[freq_col, 'Purchase_Frequency_Days']].head(10))
else:
    print("Purchase Frequency column not found")

if 'Purchase_Amount_USD' in df.columns:
    sns.boxplot(
        x='age_group',
        y='Purchase_Amount_USD',
        data=df
    )
    plt.title('Purchase Amount by Age Group')
    plt.show()

print(df[['Discount_Applied', 'Promo_Code_Used']].head(10))
print((df['Discount_Applied'] == df['Promo_Code_Used']).all())

df.to_sql(
    'customer_data',
    con=engine,
    if_exists='replace',
    index=False
)

print("Data uploaded to MySQL successfully")

conn.close()