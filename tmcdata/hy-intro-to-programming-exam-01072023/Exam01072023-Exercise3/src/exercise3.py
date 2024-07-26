
from random import sample

def draw_numbers():  
    numbers = sample(range(1, 39), 7)
    return sorted(numbers)
    

def calculate_winnings(hits: list):
    sum = 0
    for hit in hits:
        if hit == 4:
            sum += 10
        elif hit == 5:
            sum += 50
        elif hit == 6:
            sum += 2750
        elif hit >= 7:
            sum += 6500000
    return sum

        
def play_lottery(ticket: list):
    winning_lottery = draw_numbers()
    hits = []
    
    for row in ticket:
        hit = 0
        for j, number in enumerate(row):
            if number == winning_lottery[j]:
                hit += 1
        hits.append(hit)
    total_winings = calculate_winnings(hits)

    if total_winings == 0:
        return "No winnings!"
    else:
        return f"You won {total_winings} euros!"


if __name__ == "__main__":
    print(draw_numbers())
    print()
    print(calculate_winnings([0, 0, 0, 0, 0, 0, 0]))
    print(calculate_winnings([]))
    print(calculate_winnings([4]))
    print(type(calculate_winnings([4])))
    print(calculate_winnings([4, 5, 4]))
    print(calculate_winnings([4, 7])) 
    print()
    print()
    from random import seed
    seed(1)
    ticket = [[5, 8, 9, 17 , 20, 21, 22], [8, 9, 10, 11, 12, 13, 14]]
    print(play_lottery(ticket))
    print(play_lottery(ticket))
    print(play_lottery([[1, 2, 3, 4, 5, 6, 7]]))