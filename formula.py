import json
from formulation.objective import build_objective, build_objective_from_vars
from formulation.constraint import build_linear_constraint

datasets = []

with open('test_extracted.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        
        document = data["document"]
        obj_declaration = data["obj_declaration"]
        obj_type = obj_declaration["type"]
        
        if obj_type == "objective":
            objective_statement = build_objective(obj_declaration)
        if obj_type == "objvar":
            objective_statement = build_objective_from_vars(obj_declaration)
        
        print(objective_statement)
        
        const_declarations = data["const_declarations"]
        for const in const_declarations:
            const_type = const["type"]
            print(const_type)
            
            # if const_type == "linear":
            #     const_statement = 
        
        break