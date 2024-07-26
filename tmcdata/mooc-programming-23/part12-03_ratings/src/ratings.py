def sort_by_ratings(items: list):
    sorted_items = sorted(items, key = lambda item: item["rating"], reverse = True)
    return sorted_items

