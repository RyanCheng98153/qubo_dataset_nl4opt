import json
from collections import defaultdict

# Prepare dictionaries for storing results
obj_type_to_directions = defaultdict(set)
const_type_to_direction_operator_pairs = defaultdict(set)

obj_coeffs = []
linear_coeffs = []

xby_params = []

sum_limits = []
ratio_limits = []
upperbound_limits = []
lowerbound_limits = []

with open('test_extracted.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)

        # Process obj_declaration
        if "obj_declaration" in data:
            obj_decl = data["obj_declaration"]
            obj_type = obj_decl.get("type")
            direction = obj_decl.get("direction")
            if obj_type and direction:
                obj_type_to_directions[obj_type].add(direction)

        # Process const_declarations
        if "const_declarations" in data:
            for const in data["const_declarations"]:
                const_type = const.get("type")
                direction = const.get("direction")
                operator = const.get("operator")
                if const_type and direction and operator:
                    const_type_to_direction_operator_pairs[const_type].add((direction, operator))
        
        for obj_decl in [data["obj_declaration"]]:
            if obj_decl["type"] != "objective":
                continue
            obj_coeffs.extend([
                coeff for var, coeff in obj_decl["terms"].items()
            ])
        
        for const_decl in data["const_declarations"]:
            if const_decl["type"] != "linear":
                continue
            linear_coeffs.extend([
                coeff for var, coeff in const_decl["terms"].items()
            ])
        
        for const_decl in data["const_declarations"]:
            if const_decl["type"] != "linear":
                continue
            linear_coeffs.extend([
                coeff for var, coeff in const_decl["terms"].items()
            ])
        
        for const_decl in data["const_declarations"]:
            if const_decl["type"] != "xby":
                continue
            xby_params.append(const_decl["param"])
        
        for const_decl in data["const_declarations"]:
            if const_decl["type"] != "sum":
                continue
            sum_limits.append(const_decl["limit"])
        
        for const_decl in data["const_declarations"]:
            if const_decl["type"] != "upperbound":
                continue
            upperbound_limits.append(const_decl["limit"])
        
        for const_decl in data["const_declarations"]:
            if const_decl["type"] != "lowerbound":
                continue
            lowerbound_limits.append(const_decl["limit"])
        
        for const_decl in data["const_declarations"]:
            if const_decl["type"] != "ratio":
                continue
            ratio_limits.append(const_decl["limit"])

# Output results
print("[obj_declaration directions by type]")
for obj_type, directions in obj_type_to_directions.items():
    print(f"Type: {obj_type}")
    print("Directions:")
    for direction in directions:
        print(f"- {direction}")

print("\n[const_declaration (direction, operator) pairs by type]")
for const_type, pairs in const_type_to_direction_operator_pairs.items():
    print(f"type: {const_type}")
    print("Pairs: (direction, operator)")
    for direction, operator in pairs:
        print(f"- ({direction},\t {operator})")

def special_coeff(s):
    s_clean = s.replace(",", "").replace(".", "").replace("%", "")
    return not s_clean.isdigit()

print("\n[obj coefficients]")
print(list(filter(special_coeff, list(set(obj_coeffs)))))

print("\n[linear coefficients]")
print(list(filter(special_coeff, list(set(linear_coeffs)))))

print("\n[xy parameters]")
print("[]   # XY has no parameters")

print("\n[xby parameters]")
print(list(filter(special_coeff, list(set(xby_params)))))

print("\n[sum limits]")
print(list(filter(special_coeff, list(set(sum_limits)))))

print("\n[upperbound limits]")
print(list(filter(special_coeff, list(set(upperbound_limits)))))

print("\n[lowerbound limits]")
print(list(filter(special_coeff, list(set(lowerbound_limits)))))

print("\n[ratio limits]")
print(list(filter(special_coeff, list(set(ratio_limits)))))