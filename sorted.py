def reverse_sort_dictionary(dictionary):
    return sorted(
        [(name, info[0]) for name, info in dictionary.items()],
        key=lambda item: item[0],
        reverse=True
    )
