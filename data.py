import pandas as pd
from faker import Faker
import random

fake = Faker()

def generate_data(num=1000):
    data = []
    for _ in range(num):
        age = random.randint(18, 70)
        gender = random.choice(['Male', 'Female'])
        vehicle_age = random.randint(1, 15)
        vehicle_type = random.choice(['Car', 'Motorcycle', 'Truck'])
        annual_premium = round(random.uniform(3000, 50000), 2)
        claim = random.choice([0, 1])  # 0 = No claim, 1 = Claimed
        data.append([age, gender, vehicle_age, vehicle_type, annual_premium, claim])
    df = pd.DataFrame(data, columns=[
        'Age', 'Gender', 'Vehicle_Age', 'Vehicle_Type', 'Annual_Premium', 'Claim'])
    return df

df = generate_data(1000)
df.to_csv("insurance_data.csv", index=False)
