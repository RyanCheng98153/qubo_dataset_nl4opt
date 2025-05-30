def to_int_float(x):
    x = float(x)  # Ensure x is a float
    if isinstance(x, float) and x.is_integer():
        return int(x)
    return x

# Generate the objective function manually
def build_objective(obj_decl):
    direction = obj_decl["direction"]
    terms = obj_decl["terms"]
    target = obj_decl["name"]
    # Construct expression like: 100*sled_dogs + 300*trucks
    term_exprs = []
    for var, coeff in terms.items():
        coeff = to_int_float(coeff)
        term_exprs.append(f"{coeff}*{var}")
    
    objective_expr = " + ".join(term_exprs)
    objective_expr = f"{target} = {objective_expr}"
    
    MAX_TAG = ["maximum", "maximize", "maximized"]
    MIN_TAG = ["minimize", "lowest", "reduce", "minimum", "minimizing"]
    
    if direction in MAX_TAG:
        direction = "MAXIMIZE"
    elif direction in MIN_TAG:
        direction = "MINIMIZE"
    else:
        raise ValueError(f"Unknown direction: {direction}")
    
    return f"{direction}, {objective_expr}"

# Generate the objective function manually (with default coefficient 1)
def build_objective_from_vars(obj_decl):
    direction = obj_decl["direction"]
    variables = obj_decl["vars"]
    
    term_exprs = [f"1*{var}" for var in variables]
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
