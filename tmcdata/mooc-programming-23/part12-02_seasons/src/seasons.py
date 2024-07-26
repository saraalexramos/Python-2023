def sort_by_seasons(items: list):
    sorted_items = sorted(items, key= lambda item: item["seasons"])
    return sorted_items
