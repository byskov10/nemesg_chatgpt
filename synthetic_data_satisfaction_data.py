import pandas as pd
import numpy as np

def generate_synthetic_data(num_companies=200):
    data = []
    
    for _ in range(num_companies):
        employee_satisfaction = round(min(max(np.random.normal(4.5, 1), 1), 5), 2)  # Normal distribution centered around 4.5, values clipped to [1, 5]
        data.append([employee_satisfaction])

    df = pd.DataFrame(data, columns=["Employee Satisfaction"])
    df.to_csv('synthetic_data_satisfaction.csv', index=False)

generate_synthetic_data()