from collections import deque

def is_palindrome(input_string):
    # Видалити пробіли та зробити рядок нечутливим до регістру
    normalized_string = ''.join(input_string.split()).lower()
    
    # Створити deque та додати всі символи рядка
    char_deque = deque(normalized_string)
    
    # Порівнювати символи з обох кінців deque
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

# Приклади використання функції
test_strings = ["A man a plan a canal Panama", "racecar", "hello", "Was it a car or a cat I saw"]

for string in test_strings:
    result = is_palindrome(string)
    print(f"'{string}' is a palindrome: {result}")

