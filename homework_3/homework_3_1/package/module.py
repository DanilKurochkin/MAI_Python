from typing import List

class SumCalculator:
    @staticmethod
    def calculate_sum(numbers: List[float]):
        if not isinstance(numbers, list):
            raise ValueError("На вход должен подавать массив.")
        return sum(numbers)