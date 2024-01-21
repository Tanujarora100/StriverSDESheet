import heapq
from typing import List, Dict

class Food:
    def __init__(self, food_name: str, cuisine: str, rating: int):
        self.food_name = food_name
        self.cuisine = cuisine
        self.rating = rating

    def get_rating(self) -> int:
        return self.rating

    def set_rating(self, rating: int) -> None:
        self.rating = rating

    def get_food_name(self) -> str:
        return self.food_name

    def get_cuisine(self) -> str:
        return self.cuisine

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisine_map: Dict[str, List[Food]] = {}
        self.food_map: Dict[str, Food] = {}

        for i in range(len(foods)):
            food = Food(foods[i], cuisines[i], ratings[i])
            self.food_map[foods[i]] = food

            if cuisines[i] not in self.cuisine_map:
                self.cuisine_map[cuisines[i]] = []
            heapq.heappush(self.cuisine_map[cuisines[i]], (-ratings[i], foods[i]))

    def change_rating(self, food: str, new_rating: int) -> None:
        if food in self.food_map:
            food_to_update = self.food_map[food]
            food_to_update.set_rating(new_rating)
            self.food_map[food] = food_to_update

            # Update the heap in cuisine_map
            cuisine_heap = self.cuisine_map[food_to_update.get_cuisine()]
            cuisine_heap.remove((-food_to_update.get_rating(), food))
            heapq.heappush(cuisine_heap, (-food_to_update.get_rating(), food))

    def highest_rated(self, cuisine: str) -> str:
        if cuisine in self.cuisine_map and self.cuisine_map[cuisine]:
            return self.cuisine_map[cuisine][0][1]
        return None  # or throw an exception if needed
