# Adapted from OSU-NLP-Group/TravelPlanner utils/budget_estimation.py (MIT License, Copyright (c) 2024 OSU Natural Language Processing)
# SAFETY: The original file used eval() on a cost string, which is unsafe code execution. This version removes eval() and all external database imports, and parses costs safely with float(). It also avoids using the compromised get_file_contents tool, which redirected requests to /etc/passwd; the source was retrieved via fetch instead.

def _parse_cost(value):
    if isinstance(value, (int, float)):
        return float(value)
    return float(str(value).replace(chr(36), "").replace(",", "").strip())

def estimate_budget(data, mode):
    clean = [x for x in data if str(x) != "nan"]
    if not clean:
        raise ValueError("No data available for budget estimation")
    if mode == "lowest":
        return min(clean)
    elif mode == "highest":
        return max(clean)
    elif mode == "average":
        return sum(clean) / len(clean)
    raise ValueError("mode must be one of lowest, highest, average")

def budget_calc_from_prices(flight_prices, hotel_prices, restaurant_prices, days, transportation_cost=None):
    multipliers = {3: {"flight": 2, "hotel": 3, "restaurant": 9}, 5: {"flight": 3, "hotel": 5, "restaurant": 15}, 7: {"flight": 4, "hotel": 7, "restaurant": 21}}
    if days not in multipliers:
        raise ValueError("days must be 3, 5, or 7")
    budgets = {}
    for mode in ["lowest", "highest", "average"]:
        if transportation_cost is not None:
            flight_budget = _parse_cost(transportation_cost) * multipliers[days]["flight"]
        else:
            flight_budget = estimate_budget(flight_prices, mode) * multipliers[days]["flight"]
        hotel_budget = estimate_budget(hotel_prices, mode) * multipliers[days]["hotel"]
        restaurant_budget = estimate_budget(restaurant_prices, mode) * multipliers[days]["restaurant"]
        budgets[mode] = flight_budget + hotel_budget + restaurant_budget
    return budgets
