\Завдання 1 

import queue
import time
import random


def generate_request():
    request_id = random.randint(1000, 9999)
    request_data = f"Заявка №{request_id}"
    request_queue.put(request_data)
    print(f"Створено нову заявку: {request_data}")


def process_request():
    if not request_queue.empty():
        request_data = request_queue.get()
        print(f"Обробляється заявка: {request_data}")
        processing_time = random.randint(1, 3)
        time.sleep(processing_time)
        print(f"Заявка '{request_data}' оброблена успішно.")
    else:
        print("Черга заявок порожня.")


request_queue = queue.Queue()
keep_running = True

while keep_running:
    if random.random() < 0.3:
        generate_request()

    process_request()

    user_input = input("Натисніть Enter для продовження або 'q' для виходу: ")
    if user_input.lower() == 'q':
        keep_running = False

print("Програма завершена.") 




\Завдання 2 

from collections import deque


def is_palindrome(string):
    cleaned_string = ''.join(string.split()).lower()
    char_deque = deque(cleaned_string)
    
    while len(char_deque) > 1:
        left_char = char_deque.popleft()
        right_char = char_deque.pop()
        
        if left_char != right_char:
            return False
    
    return True


print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("Race car"))  # True
print(is_palindrome("Hello World"))  # False
print(is_palindrome("Able was I ere I saw Elba"))  # True
print(is_palindrome("Step on no pets"))  # True
print(is_palindrome("This is not a palindrome"))  # False




\Завдання 3 (Необовʼязкове) 

from collections import deque


def check_brackets(expression):
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    stack = deque()
    
    for char in expression:
        if char in brackets.keys():
            stack.append(char)
        elif char in brackets.values():
            if not stack:
                return "Несиметрично"
            
            opening_bracket = stack.pop()
            if brackets[opening_bracket] != char:
                return "Несиметрично"
    
    if not stack:
        return "Симетрично"
    else:
        return "Несиметрично"


print(check_brackets("( ){[ 1 ]( 1 + 3 )( ){ }}"))  # Симетрично
print(check_brackets("( 23 ( 2 - 3);"))  # Несиметрично
print(check_brackets("( 11 }"))  # Несиметрично
print(check_brackets("( [ ) ]"))  # Несиметрично
print(check_brackets("{ [ ( ) ] }"))  # Симетрично











