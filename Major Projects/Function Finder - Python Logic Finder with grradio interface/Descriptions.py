FUNCTION_DESCRIPTIONS_COMPLETE = {

    "factorial": {
        "description": "Returns the factorial of a positive integer.",
        "input_type": "Integer (e.g. 5)",
        "output_type": "Integer"
    },

    "fibonacci": {
        "description": "Generates a Fibonacci series of N terms.",
        "input_type": "Integer (e.g. 10)",
        "output_type": "List of integers"
    },

    "is_prime": {
        "description": "Checks whether a number is prime or not.",
        "input_type": "Integer",
        "output_type": "True / False"
    },

    "primes_in_range": {
        "description": "Returns all prime numbers up to N.",
        "input_type": "Integer",
        "output_type": "List"
    },

    "is_armstrong": {
        "description": "Checks if a number is an Armstrong number.",
        "input_type": "Integer",
        "output_type": "True / False"
    },

    "gcd": {
        "description": "Finds the Greatest Common Divisor of two integers.",
        "input_type": "Two integers",
        "output_type": "Integer"
    },

    "lcm": {
        "description": "Calculates the Least Common Multiple of two integers.",
        "input_type": "Two integers",
        "output_type": "Integer"
    },

    "is_palindrome_number": {
        "description": "Checks if a number is a palindrome.",
        "input_type": "Integer",
        "output_type": "True / False"
    },

    "sum_of_digits": {
        "description": "Returns the sum of digits of a number.",
        "input_type": "Integer",
        "output_type": "Integer"
    },

    "reverse_number": {
        "description": "Reverses the digits of a number.",
        "input_type": "Integer",
        "output_type": "Integer"
    },

    # STRING FUNCTIONS
    "reverse_string": {
        "description": "Reverses the input string.",
        "input_type": "String",
        "output_type": "String"
    },

    "is_palindrome_string": {
        "description": "Checks if a string reads the same backwards.",
        "input_type": "String",
        "output_type": "True / False"
    },

    "count_vowels_consonants": {
        "description": "Counts vowels and consonants in a string.",
        "input_type": "String",
        "output_type": "Dictionary"
    },

    "char_frequency": {
        "description": "Counts the frequency of each character.",
        "input_type": "String",
        "output_type": "Dictionary"
    },

    "remove_duplicates_string": {
        "description": "Removes duplicate characters while preserving order.",
        "input_type": "String",
        "output_type": "String"
    },

    "anagrams": {
        "description": "Checks if two strings are anagrams.",
        "input_type": "Two strings",
        "output_type": "True / False"
    },

    "longest_word": {
        "description": "Returns the longest word in a sentence.",
        "input_type": "String",
        "output_type": "String"
    },

    "capitalize_words": {
        "description": "Capitalizes every word in the sentence.",
        "input_type": "String",
        "output_type": "String"
    },

    "replace_vowels": {
        "description": "Replaces vowels in a string with '#'.",
        "input_type": "String",
        "output_type": "String"
    },

    "count_words": {
        "description": "Counts total words in a sentence.",
        "input_type": "String",
        "output_type": "Integer"
    },

    # LIST FUNCTIONS
    "max_in_list": {
        "description": "Returns the maximum number in the list.",
        "input_type": "List",
        "output_type": "Integer"
    },

    "second_largest": {
        "description": "Returns the second largest element in the list.",
        "input_type": "List",
        "output_type": "Integer"
    },

    "min_in_list": {
        "description": "Returns the minimum number in the list.",
        "input_type": "List",
        "output_type": "Integer"
    },

    "sum_list": {
        "description": "Returns the sum of all elements in the list.",
        "input_type": "List",
        "output_type": "Integer"
    },

    "remove_duplicates_list": {
        "description": "Removes duplicate items from a list.",
        "input_type": "List",
        "output_type": "List"
    },

    "manual_sort": {
        "description": "Sorts a list without using built-in functions.",
        "input_type": "List",
        "output_type": "List"
    },

    "even_odd_list": {
        "description": "Separates even and odd numbers.",
        "input_type": "List",
        "output_type": "Dictionary"
    },

    "merge_arrays": {
        "description": "Merges two lists and sorts them.",
        "input_type": "Two lists",
        "output_type": "List"
    },

    "rotate_list": {
        "description": "Rotates a list by K positions.",
        "input_type": "List + Integer",
        "output_type": "List"
    },

    "common_elements": {
        "description": "Returns common elements between two lists.",
        "input_type": "Two lists",
        "output_type": "List"
    },

    # DICTIONARY FUNCTIONS
    "word_frequency": {
        "description": "Counts how many times each word appears.",
        "input_type": "String",
        "output_type": "Dictionary"
    },

    "max_value_key": {
        "description": "Returns the key with the highest value.",
        "input_type": "Dictionary",
        "output_type": "Key"
    },

    "sort_dict_by_value": {
        "description": "Sorts dictionary by value.",
        "input_type": "Dictionary",
        "output_type": "Dictionary"
    },

    "merge_dicts": {
        "description": "Merges two dictionaries.",
        "input_type": "Two dictionaries",
        "output_type": "Dictionary"
    },

    "invert_dict": {
        "description": "Swaps keys and values.",
        "input_type": "Dictionary",
        "output_type": "Dictionary"
    },

    "tuples_to_dict": {
        "description": "Converts list of tuples into a dictionary.",
        "input_type": "List of tuples",
        "output_type": "Dictionary"
    },

    "remove_key": {
        "description": "Removes a key from a dictionary.",
        "input_type": "Dictionary + Key",
        "output_type": "Dictionary"
    },

    "sum_dict_values": {
        "description": "Returns the sum of dictionary values.",
        "input_type": "Dictionary",
        "output_type": "Integer"
    },

    "key_exists": {
        "description": "Checks whether a key exists.",
        "input_type": "Dictionary + Key",
        "output_type": "True / False"
    },

    "dict_intersection": {
        "description": "Returns common keys from two dictionaries.",
        "input_type": "Two dictionaries",
        "output_type": "Dictionary"
    },

    # SEARCHING & SORTING
    "binary_search": {
        "description": "Searches for an element using binary search.",
        "input_type": "Sorted list + Value",
        "output_type": "Index or -1"
    },

    "linear_search": {
        "description": "Searches element by scanning list.",
        "input_type": "List + Value",
        "output_type": "Index or -1"
    },

    "bubble_sort": {
        "description": "Sorts list using bubble sort.",
        "input_type": "List",
        "output_type": "List"
    },

    "selection_sort": {
        "description": "Sorts list using selection sort.",
        "input_type": "List",
        "output_type": "List"
    },

    "insertion_sort": {
        "description": "Sorts list using insertion sort.",
        "input_type": "List",
        "output_type": "List"
    },

    "missing_number": {
        "description": "Finds missing number in 1–N sequence.",
        "input_type": "List",
        "output_type": "Integer"
    },

    "find_duplicates": {
        "description": "Returns duplicate items in list.",
        "input_type": "List",
        "output_type": "List"
    },

    "balanced_parentheses": {
        "description": "Checks if brackets are balanced.",
        "input_type": "String",
        "output_type": "True / False"
    },

    "count_occurrences": {
        "description": "Counts how many times each item occurs.",
        "input_type": "List",
        "output_type": "Dictionary"
    },

    "transpose_matrix": {
        "description": "Returns the transposed version of a matrix.",
        "input_type": "Matrix (list of lists)",
        "output_type": "Matrix"
    },
}
