def merge_list(list1, list2):
    if isinstance(list1, int) or isinstance(list2, int):
        raise TypeError("Both inputs must be lists.")
    
    merged = []
    combined = list1 + list2
    while combined:
        minimum = min(combined)
        merged.append(minimum)
        combined.remove(minimum)
    return merged



print(merge_list([1, 3, 5, 8, 7], [2, 4, 6])) # Example usage
