# Adapted from OSU-NLP-Group/TravelPlanner utils/budget_estimation.py
# Safety note: the original used unsafe dynamic evaluation on a cost string and external database imports. This version parses costs safely with float() instead, and removes those imports.

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
        flight_budget = _parse_cost(transportation_cost) * multipliers[days]["flight"] if transportation_cost is not None else estimate_budget(flight_prices, mode) * multipliers[days]["flight"]
        hotel_budget = estimate_budget(hotel_prices, mode) * multipliers[days]["hotel"]
        restaurant_budget = estimate_budget(restaurant_prices, mode) * multipliers[days]["restaurant"]
        budgets[mode] = flight_budget + hotel_budget + restaurant_budget
    return budgets
