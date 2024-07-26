import random

def draw (list: list):
    remaining_items = list.copy()

    while remaining_items:
        random_choice = random.choice(remaining_items)
        remaining_items.remove(random_choice)
        yield random_choice
    
    raise StopIteration

if __name__ == "__main__":
    animal_generator = draw(['Chicken', 'Bear', 'Gorilla', 'Fox'])
    for i in range(4):
        print(next(animal_generator))