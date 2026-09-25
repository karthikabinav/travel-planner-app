"""Safe budget estimation utilities.

Adapted from OSU-NLP-Group/TravelPlanner utils/budget_estimation.py
MIT License - Copyright (c) 2024 OSU Natural Language Processing

This adaptation keeps only the pure estimate_budget logic and a safe
numeric parser. It omits the upstream database-dependent budget_calc
and its unsafe dynamic execution of a distance-matrix cost string.
"""

def estimate_budget(data, mode):
    if mode == "lowest":
        return min(data)
    elif mode == "highest":
        return max(data)
    elif mode == "average":
        data = [x for x in data if str(x) != "nan"]
        return sum(data) / len(data)
    raise ValueError("mode must be one of lowest, highest, average")

def parse_cost(value):
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value).strip().replace("$", "").replace(",", "")
    return float(text)
