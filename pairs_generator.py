# %%
import csv
import json

def read_csv_file(file_path):
    data = []
    
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip header row if present
        
        for row in reader:
            data.append(row)
    
    return data

def create_prompt_completion_pairs(data):
    prompt_completion_pairs = []
    prompt_template = """
I have a spreadsheet with ESG data about a company in csv format.
These are the column headings:
Company name,Number of employees,Female employees,Male employees,Female employees in percentage,Male employees in percentage,Sickness absence in days per employee for one year,Median salary for men in DKK,Median salary for women in DKK

This is the data:
{data_line}

Can you come up with 5 suggestions to improve the company's ESG data?
Write a description of the improvement, the numeric data as it is now, and a specific numeric goal for the data. Come up with 3 ideas for initiatives that the company can do to reach the goal (separate with a comma).

In the answer, remove double quotations from numbers.
The answer needs to be in Danish."""

    for row in data:
        data_line = ','.join(row)
        prompt = prompt_template.format(data_line=data_line)
        completion = ""

        prompt_completion_pair = {
            "prompt": prompt,
            "completion": completion
        }
        
        prompt_completion_pairs.append(prompt_completion_pair)
    
    return prompt_completion_pairs

# # Example usage
# csv_file_path = 'path/to/your/file.csv'
# csv_data = read_csv_file(csv_file_path)
# prompt_completion_pairs = create_prompt_completion_pairs(csv_data)

# # Print the pairs
# for pair in prompt_completion_pairs:
#     print(json.dumps(pair, ensure_ascii=False))

# %%
