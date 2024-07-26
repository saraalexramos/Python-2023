class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

def sort_by_length(routes: list):
    sorted_routes = sorted(routes, key = lambda route: route.length, reverse = True)
    return sorted_routes

def sort_by_difficulty(routes: list):
    sorted_routes = sorted(routes, key=lambda route: (route.grade, -route.length), reverse = True)
    return sorted_routes

