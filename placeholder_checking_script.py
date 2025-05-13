import json
import re

def extract_placeholders_from_file(filepath):
    placeholders = set()

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line)
                response = data.get("response", "")
                found = re.findall(r"\{\{(.*?)\}\}", response)
                placeholders.update(map(str.strip, found))
            except json.JSONDecodeError:
                print(f"Skipping invalid line: {line}")

    return sorted(placeholders)

def write_placeholders_to_file(placeholders, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        for ph in placeholders:
            f.write(f"{{{{{ph}}}}}\n") 

input_file = "bitext-retail-banking-llm-chatbot-training-dataset.csv"
output_file = "placeholders.txt"

placeholders = extract_placeholders_from_file(input_file)
write_placeholders_to_file(placeholders, output_file)

print(f"Extracted {len(placeholders)} placeholders and saved to '{output_file}'")
