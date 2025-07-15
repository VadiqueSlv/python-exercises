## Tasks

1. Check if a number is evenWrite a program that determines whether a number is even or not
2. Check number and calculate squareThe user inputs a numberIf the number is greater than 100 print `"Too much"`Otherwise, print the square of the number
3. Sum numbers from 1 to NThe user inputs a number NCalculate the sum of all numbers from 1 to N inclusive
4. Count the letter "a" in a stringThe user inputs a string (e.g., `"banana"`)The program counts how many times the letter `"a"` appears in the string
5. Check if a number is primeWrite a function that checks if a given number is prime
6. Calculate the average of a list of numbersWrite a function that takes a list of numbers and returns their average value
7. Work with a list
   Create a list of 5 numbers, add one more number to it, and sort the list in ascending order

#### Stage 2

1. **Group elements by N (group_elements.py)**

   Group elements of a list into sublists of size N. The last group may contain fewer elements.

```python
grouped([1, 2, 3, 4, 5], n=2) ➝ [[1, 2], [3, 4], [5]]
```

2. **Find sublist with maximum sum (sublist_with_max_sum.py)**

   Find a contiguous sublist with the maximum sum (Kadane-like), but return the actual sublist, not just the sum.
3. **Remove all occurrences of the maximum value (remove_max.py)**

   Remove all elements equal to the maximum value, keeping the original order.

```python
remove_max([1, 3, 2, 3, 1]) ➝ [1, 2, 1]
```

4. **Group dictionaries by key value (group_by_key.py)**

   Group a list of dictionaries by the value of a specific key.

```python
data = [{'a': 1}, {'a': 2}, {'a': 1}]
# ➝ {1: [{'a': 1}, {'a': 1}], 2: [{'a': 2}]}
```

5. **Deep merge two dictionaries**

   Merge two dictionaries with nested structure recursively, giving priority to values from the second dictionary.
6. **Invert dictionary with unique values (invert_dict.py)**

   Invert a dictionary where all values are unique.

```python
{'a': 1, 'b': 2} ➝ {1: 'a', 2: 'b'}
```

7. **Check near-palindrome**

   Check if a string can become a palindrome by removing at most one character.

   Example: `"abca"` ➝ yes, by removing `'b'` or `'c'`.
