
def sort_by_remaining_stock(items: list):
    sorted_items = sorted(items, key=lambda item: item[2])
    return sorted_items