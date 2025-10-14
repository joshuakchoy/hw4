def reverse_sort_dictionary(dictionary):
    for key in dictionary:
        dictionary[key] = dictionary[key][0]
    return dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))