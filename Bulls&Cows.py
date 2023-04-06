#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import time

def generate_secret_number(digits):
    secret_number = ''
    while len(secret_number) < digits:
        digit = str(random.randint(0, 9))
        if digit not in secret_number:
            secret_number += digit
    return secret_number

def evaluate_guess(secret_number, guess):
    bulls = sum(s == g for s, g in zip(secret_number, guess))
    cows = sum(s in guess for s in secret_number) - bulls
    return f"+{bulls}, -{cows}"

def play_game(digits):
    secret_number = generate_secret_number(digits)
    attempts = 0
    start_time = time.time()
    print(f"Welcome to the Bulls and Cows Game with {digits}-digit numbers!")
    
    while True:
        guess = input(f"Enter your {digits}-digit guess: ")
        if len(guess) == digits and guess.isdigit() and len(set(guess)) == digits:
            attempts += 1
            result = evaluate_guess(secret_number, guess)
            if result == f"+{digits}, -0":
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"Congratulations! You found the secret number {secret_number} in {attempts} attempts and {elapsed_time:.2f} seconds.")
                break
            else:
                print(f"Result: {result}")
        else:
            print(f"Invalid input. Please enter a {digits}-digit number with unique digits.")
            
if __name__ == "__main__":
    while True:
        try:
            user_digits = int(input("Enter the length of the secret number (2-5): "))
            if 2 <= user_digits <= 5:
                break
            else:
                print("Invalid input. Please enter a number between 2 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 2 and 5.")
    
    play_game(user_digits)


# In[ ]:




