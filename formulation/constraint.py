def revise_operator(op, direction):
    if direction not in [
        "less than",
        "more than",
        "below",
        "must be large than",
        "must be larger",
        "larger than",
        "must exceed",
        "must be more",
        "more",
        "less"
    ]:
        return op
    
    if op == ">=":
        return ">"
    elif op == "<=":
        return "<"
    else:
        raise ValueError(f"Unsupported operator: {op}")

def to_int_float(x):
    x = x.replace(',', '')  # Remove commas for thousands
    if x.endswith("%"):
        x = x[:-1]  # Remove percentage sign
        x = float(x) / 100  # Convert percentage to decimal
    x = float(x)  # Ensure x is a float
    if isinstance(x, float) and x.is_integer():
        return int(x)
    return x

special_linear_coeffs = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5
}

def build_constraint_linear(const_decl):
    # Extract terms (variables and their coeffs)
    terms = const_decl["terms"]

    # Construct expression
    term_exprs = []
    for var, coeff in terms.items():
        if coeff in special_linear_coeffs:
            coeff = special_linear_coeffs[coeff]
        else:
            coeff = to_int_float(coeff)
        term_exprs.append(f"{coeff}*{var}")
    
    # Extract operator
    operator_map = {
        "LESS_OR_EQUAL": "<=",
        "GREATER_OR_EQUAL": ">="
    }
    operator = operator_map.get(const_decl["operator"])
    operator = revise_operator(operator, const_decl["direction"])
    
    # Extract right hand side value
    limit = to_int_float(const_decl["limit"])
    
    sum_expr = " + ".join(term_exprs)
    const_expr = sum_expr + f" {operator} {limit}"
    
    return const_expr

# Constraint Declaration: xy
# const_decl_xy = {
#     "type": "xy",
#     "x_var": "sled dog",
#     "direction": "less than",
#     "y_var": "truck",
#     "operator": "LESS_OR_EQUAL"
# }
def build_constraint_xy(const_decl):
    # Extract variables
    x_var = const_decl["x_var"]
    y_var = const_decl["y_var"]
    
    # Map operator from JSON
    operator_map = {
        "LESS_OR_EQUAL": "<=",
        "GREATER_OR_EQUAL": ">="
    }
    operator = operator_map.get(const_decl["operator"])
    operator = revise_operator(operator, const_decl["direction"])    

    const_expr = f"{x_var} {operator} {y_var}"
    return const_expr

special_upperbound_limits = {
    'fifteen': 15,
}

def build_constraint_upperbound(const_decl):
    # Extract variable and constant
    var = const_decl["var"]
    limit_str = const_decl["limit"]
    if limit_str in special_upperbound_limits:
        limit = special_upperbound_limits[limit_str]
    else:
        limit = to_int_float(limit_str)
    
    # Map operator
    operator_map = {
        "LESS_OR_EQUAL": "<=",
        "GREATER_OR_EQUAL": ">="
    }
    operator = operator_map.get(const_decl["operator"])
    operator = revise_operator(operator, const_decl["direction"])

    # Build constraint expression
    const_expr = f"{var} {operator} {limit}"
    return const_expr

def build_constraint_sum(const_decl, vars_list):
    # Extract limit and operator
    limit = to_int_float(const_decl["limit"])

    operator_map = {
        "LESS_OR_EQUAL": "<=",
        "GREATER_OR_EQUAL": ">="
    }
    operator = operator_map.get(const_decl["operator"])
    operator = revise_operator(operator, const_decl.get("direction", ""))

    # Build the sum expression from variable list
    sum_expr = " + ".join(vars_list)
    const_expr = f"{sum_expr} {operator} {limit}"

    return const_expr

special_lowerbound_limits = {
    "five": 5,
    "third": 0.333,
}

def build_constraint_lowerbound(const_decl):
    # Extract variable and limit
    var = const_decl["var"]
    limit_str = const_decl["limit"]
    if limit_str in special_lowerbound_limits:
        limit = special_lowerbound_limits[limit_str]
    else:
        limit = to_int_float(limit_str)
    
    # Map operator
    operator_map = {
        "LESS_OR_EQUAL": "<=",
        "GREATER_OR_EQUAL": ">="
    }
    operator = operator_map.get(const_decl["operator"])
    operator = revise_operator(operator, const_decl["direction"])

    # Build constraint expression
    const_expr = f"{var} {operator} {limit}"
    return const_expr

special_xby_params = {
    '5 times': 5,
    'three': 3, 
    'half': 0.5,
    'third': 0.333,
    'four': 4,
    '2 times': 2,
    'two' : 2,
    'twice': 2, 
    'five times': 5, 
    'two times': 2,
    '1.5 times': 1.5,
    'three times': 3, 
    'a third': 0.333,
    'thrice': "3",
}

def build_constraint_xby(const_decl):
    # Extract variables and parameter
    x_var = const_decl["x_var"]
    y_var = const_decl["y_var"]
    
    param_str = const_decl["param"]
    if param_str in special_xby_params:
        param = special_xby_params[param_str]
    else:
        param = to_int_float(param_str)

    operator_map = {
        "LESS_OR_EQUAL": "<=",
        "GREATER_OR_EQUAL": ">="
    }
    operator = operator_map.get(const_decl["operator"])
    operator = revise_operator(operator, const_decl["direction"])

    # Build the constraint expression
    const_expr = f"{x_var} {operator} {param} * {y_var}"
    return const_expr

special_ratio_limits = {
    'fifteen percent': 0.15,
    '5': 0.05,
    'third': 0.333,
    '35 percent': 0.35,
    '60': 0.6,
}

def build_constraint_ratio(const_decl, vars_list):
    if const_decl["type"] != "ratio":
        raise ValueError("Only 'ratio' constraint types are supported.")
    
    x_var = const_decl["var"]
    
    # Parse percentage like "20%" into float 0.2
    limit_str = const_decl["limit"]
    if limit_str in special_ratio_limits:
        limit = special_ratio_limits[limit_str]
    else:
        limit = to_int_float(limit_str)
    
    operator_map = {
        "LESS_OR_EQUAL": "<=",
        "GREATER_OR_EQUAL": ">="
    }
    operator = operator_map.get(const_decl["operator"])
    operator = revise_operator(operator, const_decl.get("direction", ""))

    # All other variables except the one used in numerator (x)
    other_vars = [var for var in vars_list if var != x_var]

    if not other_vars:
        raise ValueError("Ratio constraint requires at least one other variable in the denominator.")

    sum_expr = f"{x_var} + " + " + ".join(other_vars)
    constraint_expr = f"{x_var} {operator} {limit} * ({sum_expr})"
    return constraint_expr