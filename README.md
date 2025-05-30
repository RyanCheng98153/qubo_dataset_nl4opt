{
    "document": """A post office is buying stamping machines and they can buy a dual or single model stamping machine.
A dual model stamping machine can stamp 50 letters per minute while a single model stamping machine can stamp 30 letters per minute.
The dual model stamping machine requires 20 units of glue per minute while the single model stamping machine requires 15 units of glue per minute.
Since the single model stamping machine is quieter, the number of single model stamping machines must be more than the number of dual model stamping machines.
Further, the post office wants to make sure they can stamp at least 300 letters per minute and use at most 135 units of glue per minute.
How many of each stamping machine should they purchase to minimize the total number of stamping machines?""",
    "vars": [
        "dual",
        "single"
    ],
    "params": [
        "50",
        "30",
        "20",
        "15"
    ],
    "obj_declaration": {
        "type": "objvar",
        "direction": "minimize",
        "name": "total number of stamping machines",
        "vars": [
            "dual",
            "single"
        ]
    },
    "const_declarations": [
        {
            "type": "xy",
            "x_var": "single model stamping",
            "direction": "more than",
            "y_var": "dual model stamping",
            "operator": "LESS_OR_EQUAL"
        },
        {
            "type": "linear",
            "direction": "at least",
            "limit": "300",
            "terms": {
                "dual model stamping": "50",
                "single model stamping": "30"
            },
            "operator": "GREATER_OR_EQUAL"
        },
        {
            "type": "linear",
            "direction": "at most",
            "limit": "135",
            "terms": {
                "dual model stamping": "20",
                "single model stamping": "15"
            },
            "operator": "LESS_OR_EQUAL"
        }
    ],
    "id": "-642253022"
}
- xy more than: less_or_equal -> greater

{
    "document": """A smoothie shop has a promotion for their two smoothies; an acai berry smoothie and a banana chocolate smoothie.
It takes 7 units of acai berries and 3 units of water to make the acai berry smoothie.
It takes 6 units of banana chocolate and 4 units of water to make the banana chocolate smoothie.
Banana chocolate smoothies are more popular and thus the number of banana chocolate smoothies made must be more than the number of acai berry smoothies made.
However, the acai berry smoothies have a loyal customer base, and at least 35% of the smoothies made must be acai berry smoothies.
If the smoothie shop has 3500 units of acai berries and 3200 units of banana chocolate, to reduce the total amount of water, how many of each smoothie type should be made?""",
    "vars": [
        "acai berry smoothie",
        "banana chocolate smoothie"
    ],
    "params": [
        "7",
        "3",
        "6",
        "4"
    ],
    "obj_declaration": {
        "type": "objective",
        "direction": "reduce",
        "name": "amount of water",
        "terms": {
            "acai berry smoothie": "3",
            "banana chocolate smoothie": "4"
        }
    },
    "const_declarations": [
        {
            "type": "xy",
            "x_var": "banana chocolate",
            "direction": "more than",
            "y_var": "acai berry smoothies",
            "operator": "LESS_OR_EQUAL"
        },
        {
            "type": "ratio",
            "direction": "at least",
            "limit": "35%",
            "var": "acai berry smoothies",
            "operator": "GREATER_OR_EQUAL"
        },
        {
            "type": "linear",
            "direction": "has",
            "limit": "3500",
            "terms": {
                "acai berry smoothie": "7"
            },
            "operator": "LESS_OR_EQUAL"
        },
        {
            "type": "linear",
            "direction": "has",
            "limit": "3200",
            "terms": {
                "banana chocolate smoothie": "6"
            },
            "operator": "LESS_OR_EQUAL"
        }
    ],
    "id": "-1210596886"
}
- xy more than: less_or_equal -> greater

{
    "document": """Platinum Database sells two types of subscription software packages: a personal license and a commercial license which will cost $550 and $2000 to generate respectively.
    The marketing department estimates that they can sell at most 300 licenses for both versions combined a month.
    The profit per personal license is $450 and the profit per commercial version is $1200.
    If the company does not want to spend more than $400000, how many of each software package should they produce to maximize the profits.""",
    "vars": [
        "personal license",
        "commercial license"
    ],
    "params": [
        "550",
        "2000",
        "450",
        "1200"
    ],
    "obj_declaration": {
        "type": "objective",
        "direction": "maximize",
        "name": "profits",
        "terms": {
            "personal license": "450",
            "commercial version": "1200"
        }
    },
    "const_declarations": [
        {
            "type": "linear",
            "direction": "no more than",
            "limit": "400000",
            "terms": {
                "personal license": "550",
                "commercial license": "2000"
            },
            "operator": "LESS_OR_EQUAL"
        },
        {
            "type": "sum",
            "direction": "at most",
            "limit": "300",
            "operator": "LESS_OR_EQUAL"
        }
    ],
    "id": "1294399767"
}
- linear: more than -> no more than