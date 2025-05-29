# # Given objective declaration
# obj_declaration = {
#     "type": "objective",
#     "direction": "maximize",
#     "name": "number of fish",
#     "terms": {
#         "sled dogs": "100",
#         "trucks": "300"
#     }
# }

# Sanitize variable names (replace spaces with underscores)
def sanitize_varname(name):
    return name.replace(" ", "_")

# Generate the objective function manually
def build_objective(obj_decl):
    direction = obj_decl["direction"]
    terms = obj_decl["terms"]
    target = obj_decl["name"]
    target_sanitized = sanitize_varname(target)
    
    # Construct expression like: 100*sled_dogs + 300*trucks
    term_exprs = []
    for var, coeff in terms.items():
        var_sanitized = sanitize_varname(var)
        term_exprs.append(f"{coeff}*{var_sanitized}")
    
    objective_expr = " + ".join(term_exprs)
    objective_expr = f"{target_sanitized} = {objective_expr}"
    
    MAX_TAG = ["maximum", "maximize", "maximized"]
    MIN_TAG = ["minimize", "lowest", "reduce", "minimum", "minimizing"]
    
    if direction in MAX_TAG:
        direction = "MAXIMIZE"
    elif direction in MIN_TAG:
        direction = "MINIMIZE"
    else:
        raise ValueError(f"Unknown direction: {direction}")
    
    return f"{direction}, {objective_expr}"

# Given objvar declaration
# obj_declaration = {
#     "type": "objvar",
#     "direction": "minimize",
#     "name": "number of butcher shops",
#     "vars": [
#         "small shop",
#         "large shop"
#     ]
# }

# Generate the objective function manually (with default coefficient 1)
def build_objective_from_vars(obj_decl):
    direction = obj_decl["direction"]
    variables = obj_decl["vars"]
    
    term_exprs = [f"1*{sanitize_varname(var)}" for var in variables]
    objective_expr = " + ".join(term_exprs)
    
    MAX_TAG = ["maximize"]
    MIN_TAG = ["reduce", "decrease", "minimum", "minimize"]
    
    if direction in MAX_TAG:
        direction = "MAXIMIZE"
    elif direction in MIN_TAG:
        direction = "MINIMIZE"
    else:
        raise ValueError(f"Unknown direction: {direction}")
    
    return f"{direction}, {objective_expr}"
