def parse_linear_constraint(json_obj):
    """
    Parses a linear constraint JSON object into a tuple: (coefficients list, variable names list, operator, rhs constant)
    Example output:
        ([50.0, 100.0], ['sled dogs', 'truck'], '<=', 1000.0)
    """
    # 1. Extract direction and ensure it's linear (optional check)
    if json_obj.get("type") != "linear":
        raise ValueError("Only 'linear' constraint types are supported.")
    
    # 2. Extract terms (variables and their coefficients)
    terms = json_obj.get("terms", {})
    variable_names = list(terms.keys())
    coefficients = [float(terms[var]) for var in variable_names]

    # 3. Extract operator
    operator_map = {
        "LESS_OR_EQUAL": "<=",
        "GREATER_OR_EQUAL": ">=",
        "EQUAL": "=="
    }
    operator = operator_map.get(json_obj.get("operator"))
    if operator is None:
        raise ValueError("Unsupported operator.")

    # 4. Extract RHS value
    rhs = float(json_obj.get("limit"))

    # 5. Return parsed constraint
    return coefficients, variable_names, operator, rhs