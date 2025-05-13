import csv
import re
from placeholder_values import values

input_csv_path = "bitext-retail-banking-llm-chatbot-training-dataset.csv"
output_csv_path = "Bitex-retail-banking-llm-chatbot-training-dataset-preprocessed.csv"

placeholder_pattern = re.compile(r"\{\{.*?\}\}")

def replace_placeholders(text, values_dict):
    return placeholder_pattern.sub(lambda m: values_dict.get(m.group(0), m.group(0)), text)

with open(input_csv_path, mode="r", encoding="utf-8", newline='') as infile, \
     open(output_csv_path, mode="w", encoding="utf-8", newline='') as outfile:

    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        if "response" in row:
            row["response"] = replace_placeholders(row["response"], values)
        writer.writerow(row)

print("Placeholders replaced and saved to", output_csv_path)
