import json
from formulation.objective import build_objective, build_objective_from_vars
from formulation.constraint import (
    build_constraint_linear, 
    build_constraint_xy, 
    build_constraint_upperbound, 
    build_constraint_sum, 
    build_constraint_lowerbound,
    build_constraint_xby,
    build_constraint_ratio
)

def revise_varname(name, var_mentions):
    return var_mentions.get(name, name).replace(" ", "_")
    
with open('test_extracted.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        
        # if data["id"] not in [
        #     # "1117636837", 
        #     # "1884763091",
        #     # "-1394927728",
        #     "-1396068089"
        # ]:
        #     continue
        
        print()
        print("======================")
        print()
        
        document = data["document"]
        obj_declaration = data["obj_declaration"]
        obj_type = obj_declaration["type"]
        var_mentions = data["var_mention_to_first_var"]
        
        obj_declaration["name"] = obj_declaration["name"].replace(" ", "_")
        
        if obj_type == "objective":
            obj_declaration["terms"] = {
                revise_varname(var, var_mentions): coeff
                for var, coeff in obj_declaration["terms"].items()
            }
            objective_statement = build_objective(obj_declaration)
        if obj_type == "objvar":
            obj_declaration["vars"] = [
                revise_varname(var, var_mentions)
                for var in obj_declaration["vars"]
            ]
            objective_statement = build_objective_from_vars(obj_declaration)
        
        print(objective_statement)
        
        const_declaration_list = data["const_declarations"]
        for const_declaration in const_declaration_list:
            const_type = const_declaration["type"]
            print(const_type)
            
            var_mentions = data["var_mention_to_first_var"]
            
            if const_type == "linear":
                const_declaration["terms"] = {
                    revise_varname(var, var_mentions): coeff 
                    for var, coeff in const_declaration["terms"].items()
                }
                const_statement = build_constraint_linear(const_declaration)
            
            if const_type == "xy":
                const_declaration["x_var"] = revise_varname(const_declaration["x_var"], var_mentions)
                const_declaration["y_var"] = revise_varname(const_declaration["y_var"], var_mentions)
                const_statement = build_constraint_xy(const_declaration)
            
            if const_type == "upperbound":
                const_declaration["var"] = revise_varname(const_declaration["var"], var_mentions)
                const_statement = build_constraint_upperbound(const_declaration)
            
            if const_type == "sum":
                vars_list = [var.replace(" ", "_") for var in data["vars"]]
                const_statement = build_constraint_sum(const_declaration, vars_list)
            
            if const_type == "lowerbound":
                const_declaration["var"] = revise_varname(const_declaration["var"], var_mentions)
                const_statement = build_constraint_lowerbound(const_declaration)
            
            if const_type == "xby":
                const_declaration["x_var"] = revise_varname(const_declaration["x_var"], var_mentions)
                const_declaration["y_var"] = revise_varname(const_declaration["y_var"], var_mentions)
                const_statement = build_constraint_xby(const_declaration)
            
            if const_type == "ratio":
                vars_list = [var.replace(" ", "_") for var in data["vars"]]
                const_declaration["var"] = revise_varname(const_declaration["var"], var_mentions)
                const_statement = build_constraint_ratio(const_declaration, vars_list)
            
            print(const_statement)
            
        # break