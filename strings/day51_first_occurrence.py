def first_occurrence(haystack, needle):
    return haystack.find(needle)
haystack = input("enter string: ")
needle = input("enter word: ")
print(first_occurrence(haystack, needle))
