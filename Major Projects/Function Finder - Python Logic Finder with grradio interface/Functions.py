def factorial(n):
    if not isinstance(n, int) or n < 0:
        return "Enter a positive integer"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_in_range(n):
    return [i for i in range(2, n + 1) if is_prime(i)]

def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == n

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def is_palindrome_number(n):
    return str(n) == str(n)[::-1]

def sum_of_digits(n):
    return sum(int(d) for d in str(n))

def reverse_number(n):
    return int(str(n)[::-1])

def reverse_string(s):
    return s[::-1]

def is_palindrome_string(s):
    return s == s[::-1]

def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    v = sum(1 for ch in s if ch in vowels)
    c = sum(1 for ch in s if ch.isalpha() and ch not in vowels)
    return {"vowels": v, "consonants": c}

def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

def remove_duplicates_string(s):
    res = ""
    for ch in s:
        if ch not in res:
            res += ch
    return res

def anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

def capitalize_words(sentence):
    return sentence.title()

def replace_vowels(s, char="#"):
    vowels = "aeiouAEIOU"
    return "".join(char if ch in vowels else ch for ch in s)

def count_words(sentence):
    return len(sentence.split())

def max_in_list(lst):
    return max(lst)

def second_largest(lst):
    unique = sorted(set(lst))
    return unique[-2] if len(unique) >= 2 else None

def min_in_list(lst):
    return min(lst)

def sum_list(lst):
    return sum(lst)

def remove_duplicates_list(lst):
    return list(dict.fromkeys(lst))

def manual_sort(lst):
    lst = lst[:]
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[i]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

def even_odd_list(lst):
    even = [x for x in lst if x % 2 == 0]
    odd = [x for x in lst if x % 2 != 0]
    return {"even": even, "odd": odd}

def merge_arrays(a, b):
    return sorted(a + b)

def rotate_list(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

def common_elements(a, b):
    return list(set(a) & set(b))

def word_frequency(sentence):
    words = sentence.split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq

def max_value_key(d):
    return max(d, key=d.get)

def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda x: x[1]))

def merge_dicts(d1, d2):
    merged = d1.copy()
    merged.update(d2)
    return merged

def invert_dict(d):
    return {v: k for k, v in d.items()}

def tuples_to_dict(lst):
    return dict(lst)

def remove_key(d, key):
    if key in d:
        d.pop(key)
    return d

def sum_dict_values(d):
    return sum(d.values())

def key_exists(d, key):
    return key in d

def dict_intersection(d1, d2):
    return {k: d1[k] for k in d1 if k in d2}

def binary_search(lst, target):
    if not isinstance(lst, list):
        return "Input 1 must be a list"
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def linear_search(lst, target):
    if not isinstance(lst, list):
        return "Input 1 must be a list"
    for i, v in enumerate(lst):
        if v == target:
            return i
    return -1

def bubble_sort(lst):
    lst = lst[:]
    n = len(lst)
    for i in range(n):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

def selection_sort(lst):
    lst = lst[:]
    for i in range(len(lst)):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

def insertion_sort(lst):
    lst = lst[:]
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

def missing_number(lst):
    n = len(lst) + 1
    return n * (n + 1) // 2 - sum(lst)

def find_duplicates(lst):
    seen = set()
    dup = set()
    for x in lst:
        if x in seen:
            dup.add(x)
        else:
            seen.add(x)
    return list(dup)

def balanced_parentheses(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return len(stack) == 0

def count_occurrences(lst):
    freq = {}
    for x in lst:
        freq[x] = freq.get(x, 0) + 1
    return freq

def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

FUNCTIONS = {
    "factorial": factorial,
    "fibonacci": fibonacci,
    "is_prime": is_prime,
    "primes_in_range": primes_in_range,
    "is_armstrong": is_armstrong,
    "gcd": gcd,
    "lcm": lcm,
    "is_palindrome_number": is_palindrome_number,
    "sum_of_digits": sum_of_digits,
    "reverse_number": reverse_number,
    "reverse_string": reverse_string,
    "is_palindrome_string": is_palindrome_string,
    "count_vowels_consonants": count_vowels_consonants,
    "char_frequency": char_frequency,
    "remove_duplicates_string": remove_duplicates_string,
    "anagrams": anagrams,
    "longest_word": longest_word,
    "capitalize_words": capitalize_words,
    "replace_vowels": replace_vowels,
    "count_words": count_words,
    "max_in_list": max_in_list,
    "second_largest": second_largest,
    "min_in_list": min_in_list,
    "sum_list": sum_list,
    "remove_duplicates_list": remove_duplicates_list,
    "manual_sort": manual_sort,
    "even_odd_list": even_odd_list,
    "merge_arrays": merge_arrays,
    "rotate_list": rotate_list,
    "common_elements": common_elements,
    "word_frequency": word_frequency,
    "max_value_key": max_value_key,
    "sort_dict_by_value": sort_dict_by_value,
    "merge_dicts": merge_dicts,
    "invert_dict": invert_dict,
    "tuples_to_dict": tuples_to_dict,
    "remove_key": remove_key,
    "sum_dict_values": sum_dict_values,
    "key_exists": key_exists,
    "dict_intersection": dict_intersection,
    "binary_search": binary_search,
    "linear_search": linear_search,
    "bubble_sort": bubble_sort,
    "selection_sort": selection_sort,
    "insertion_sort": insertion_sort,
    "missing_number": missing_number,
    "find_duplicates": find_duplicates,
    "balanced_parentheses": balanced_parentheses,
    "count_occurrences": count_occurrences,
    "transpose_matrix": transpose_matrix,
}

TWO_INPUT_FUNCS = [
    "gcd",
    "lcm",
    "anagrams",
    "merge_arrays",
    "binary_search",
    "linear_search",
    "common_elements"
]
