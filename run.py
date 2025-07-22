#1
def is_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(is_even(1))

#2
def sum_list(numbers):
    return sum(numbers)

print(sum_list([1,2,3,4,5]))

#3
def reverse_string(s):
    return s[::-1]

print(reverse_string("Aditya"))

#4
def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("level"))

#5
def count_vowels(s):
    vowel = 'aiueoAIUEO'
    return sum(1 for char in s if char in vowel)

print(count_vowels("Aditya"))

#6
def replace_space(text):
    return text.replace(" ", "-")

print(replace_space("Hello Python World"))

#7
def min_element(lst):
    return min(lst)

print(min_element([5, 9, 2, 7]))

#8
def number_to_letter(n):
    return chr(n + 96)

print(number_to_letter(2))

#9
def digit_sum(n):
    return sum(int(digit) for digit in str(n))

print(digit_sum(1234))

#10
def word_count(sentence):
    return len(sentence.split())

print(word_count("saya suka makan nasi"))