import pandas as pd
import random

def generate_synthetic_data(num_companies=170):
    data = []
    
    for _ in range(num_companies):
        male_employees = random.randint(1, 75)
        female_employees = random.randint(1, 75)
        total_employees = male_employees + female_employees
        male_percentage = (male_employees / total_employees) * 100
        female_percentage = (female_employees / total_employees) * 100
        sickness_absence = round(random.uniform(2, 10), 2)
        male_salary = random.randint(20000, 60000)
        female_salary = random.randint(int(male_salary*0.8), male_salary)  # Female salary 80-100% of male salary
        employee_satisfaction = round(min(max(np.random.normal(4.5, 1), 1), 5), 2)  # Normal distribution centered around 4.5, values clipped to [1, 5]

        data.append([female_employees, male_employees, female_percentage, male_percentage, sickness_absence, male_salary, female_salary, employee_satisfaction])

    df = pd.DataFrame(data, columns=["Female Employees", "Male Employees", "Female Employees in percentage", "Male Employees in percentage", "Sickness absence in days per employee for one year", "Median Salary for Men in DKK", "Median Salary for Women in DKK", "Employee Satisfaction"])

    df.to_csv('synthetic_data.csv', index=False)

generate_synthetic_data()