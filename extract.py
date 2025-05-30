import json

keys_to_extract = [
    "document",
    "vars",
    # "var_mentions",
    "params",
    "var_mention_to_first_var",
    # "first_var_to_mentions",
    "obj_declaration",
    "const_declarations",
    # "_input_hash",
    # "order_mapping"
]

input_file = 'test.jsonl'
output_file = input_file.replace('.jsonl', '_extracted.jsonl')

with open(input_file, 'r', encoding='utf-8') as infile, \
     open(output_file, 'w', encoding='utf-8') as outfile:
    
    for line in infile:
        line = line.strip()
        if not line:
            continue
        try:
            item = json.loads(line)
            for item_id, item_data in item.items():
                # extracted = {"id": item_id}
                # extracted.update({key: item_data[key] for key in keys_to_extract if key in item_data})
                extracted = {key: item_data[key] for key in keys_to_extract if key in item_data}
                extracted["id"] = item_id
                outfile.write(json.dumps(extracted, ensure_ascii=False) + '\n')
        except json.JSONDecodeError as e:
            print(f"Skipping line due to JSON error: {e}")
