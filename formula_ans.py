import json
with open("nl4opt_expr.txt", 'r', encoding="utf-8") as f:
    content = f.read()

# Split the file by documents
blocks = content.strip().split("======================")
documents = []

for block in blocks:
    block = block.strip()
    if not block:
        continue

    lines = block.splitlines()
    doc = {"document": "", "objective": {}, "constraints": []}

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if line.startswith("[ Document"):
            # The document text is the next non-empty line
            i += 1
            while i < len(lines) and not lines[i].strip():
                i += 1
            doc["document"] = lines[i].strip()

        elif line.startswith("[ Objective Declaration ]"):
            i += 1
            while i < len(lines) and not lines[i].strip():
                i += 1
            obj_line = lines[i].strip()
            if "," in obj_line:
                sense, formula = obj_line.split(",", 1)
                doc["objective"] = {
                    "direction": sense.strip(),
                    "formula": formula.strip()
                }

        elif line.startswith("[ const_type"):
            # Extract const_type
            const_type = line.split(":")[-1].strip(" ]")
            i += 1
            while i < len(lines) and not lines[i].strip():
                i += 1
            formula = lines[i].strip()
            doc["constraints"].append({
                "const_type": const_type,
                "formula": formula
            })

        i += 1

    documents.append(doc)
from pprint import pprint
# pprint(documents[0])
# print(len(documents))

with open("NL4OPT_with_optimal_solution.jsonl", "r") as file:
    datas = [json.loads(line) for line in file.readlines()]

print(len(datas))


for doc in documents:
    doc["answer"] = None

for idx, data in enumerate(datas):
    for i, doc in enumerate(documents):
        if data["en_question"] == doc["document"]:
            documents[i]["answer"] = data["en_answer"]

print("Finished checking the documents.")

output_jsonl = "nl4opt_expr_ans.jsonl"

with open(output_jsonl, 'w', encoding="utf-8") as f:
    for doc in documents:
        f.write(json.dumps(doc, ensure_ascii=False) + "\n")

output_txt = "nl4opt_expr_ans.txt"
with open(output_txt, 'w', encoding="utf-8") as f:
    f.write("\n")
    
    for idx, doc in enumerate(documents):
        
        f.write( "======================\n\n")
        f.write(f"[ Document {idx + 1} ]\n")
        f.write(doc["document"] + "\n\n")
        
        f.write("[ Objective Declaration ]\n")
        f.write(f"{doc['objective']['direction']}, {doc['objective']['formula']}\n\n")
        
        for const in doc["constraints"]:
            f.write(f"[ const_type: {const['const_type'] } ]\n")
            f.write(f"{const['formula']}\n\n")
        
        f.write("[ Answer ]\n")
        if doc["answer"] is None:
            f.write("None\n\n")
        else:
            f.write(doc["answer"] + "\n\n")
        