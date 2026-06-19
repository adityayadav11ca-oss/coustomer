import pandas as pd
import random
from faker import Faker

fake = Faker()

num_records = 100

genders = ['Male', 'Female']

categories = [
    'Clothing', 'Electronics', 'Footwear',
    'Beauty', 'Accessories', 'Sports'
]

locations = [
    'Delhi', 'Mumbai', 'Bangalore', 'Hyderabad',
    'Chennai', 'Kolkata', 'Pune', 'Dehradun',
    'Haridwar', 'Lucknow'
]

sizes = ['S', 'M', 'L', 'XL']

colors = [
    'Black', 'White', 'Blue',
    'Red', 'Green', 'Yellow'
]

subscription_status = ['Yes', 'No']

shopping_types = [
    'Online', 'In-Store'
]

discount_applied = ['Yes', 'No']

promo_code_used = ['Yes', 'No']

seasons = ['Summer', 'Winter', 'Spring', 'Autumn']

payment_methods = [
    'UPI', 'Cash', 'Credit Card',
    'Debit Card', 'Net Banking'
]

purchase_frequency = [
    'Weekly',
    'Bi-Weekly',
    'Monthly',
    'Quarterly',
    'Annually',
    'Fortnightly',
    'Every 3 Months'
]

data = []

for i in range(1, num_records + 1):

    amount = round(random.uniform(20, 1000), 2)

    record = {
        'Customer_ID': i,
        'Age': random.randint(18, 60),
        'Gender': random.choice(genders),
        'Purchased_Item': fake.word().capitalize(),
        'Category': random.choice(categories),
        'Purchase_Amount_USD': amount,
        'Location': random.choice(locations),
        'Size': random.choice(sizes),
        'Color': random.choice(colors),
        'Season': random.choice(seasons),
        'Review_Rating': round(random.uniform(1, 5), 1),
        'Subscription_Status': random.choice(subscription_status),
        'Shipping_Type': random.choice(shopping_types),
        'Discount_Applied': random.choice(discount_applied),
        'Promo_Code_Used': random.choice(promo_code_used),
        'Payment_Method': random.choice(payment_methods),
        'Purchase_Frequency': random.choice(purchase_frequency),

    
        'Previous_Purchases': random.randint(1, 20)
    }

    data.append(record)

df = pd.DataFrame(data)

df.to_csv('customer_shopping_behavior.csv', index=False)

print("CSV File Successfully Generated!")
print(df.head())