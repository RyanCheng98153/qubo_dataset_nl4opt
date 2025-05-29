import json
import re

def indent_jsonl(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            try:
                # Load the JSON object from the line
                json_obj = json.loads(line)

                # If there's a "document" field, process it
                if "document" in json_obj:
                    document = json_obj["document"].strip()

                    # Insert newline between sentences using regex
                    document = re.sub(r'(?<=[.!?])\s+', '\n', document)

                    # Wrap it in triple quotes for Python-style readability
                    json_obj["document"] = f'"""{document}"""'

                # Convert dict to pretty JSON with 4-space indentation
                pretty_str = json.dumps(json_obj, indent=4)

                # Replace escaped triple-quoted string with actual triple-quoted formatting
                if '"""' in json_obj["document"]:
                    pretty_str = pretty_str.replace(
                        json.dumps(json_obj["document"]),
                        json_obj["document"]
                    )

                outfile.write(pretty_str + '\n')

            except json.JSONDecodeError:
                print(f"Error decoding JSON: {line.strip()}")

if __name__ == "__main__":
    input_file = 'test_extracted.jsonl'
    output_file = input_file.replace('.jsonl', '_prettier.jsonl')
    indent_jsonl(input_file, output_file)
    print(f"Indented JSONL file saved as {output_file}")
