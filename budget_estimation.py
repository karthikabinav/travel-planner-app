from tools.accommodations.apis import Accommodations
from tools.flights.apis import Flights
from tools.restaurants.apis import Restaurants
from tools.googleDistanceMatrix.apis import GoogleDistanceMatrix
import pandas as pd

hotel = Accommodations()
flight = Flights()
flight.load_db()
restaurant = Restaurants()
distanceMatrix = GoogleDistanceMatrix()


def estimate_budget(data, mode):
    """Estimate the budget based on the mode (lowest, highest, average) for flight, hotel, or restaurant data."""
    if mode == "lowest":
        return min(data)
    elif mode == "highest":
        return max(data)
    elif mode == "average":
        data = [x for x in data if str(x) != 'nan']
        return sum(data) / len(data)

# NOTE: Original file in OSU-NLP-Group/TravelPlanner utils/budget_estimation.py contains eval() on external distance matrix data in budget_calc, which is an unsafe code-injection pattern. That function was not copied verbatim; a safe float() parsing should be used instead of eval() if budget_calc is reimplemented.
