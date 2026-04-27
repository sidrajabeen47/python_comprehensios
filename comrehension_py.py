# --- Set Comprehensions ---

# 1. Create a set of even numbers from 1 to 10
even_set = {x for x in range(1, 11) if x % 2 == 0}
print(even_set)

# 2. From the string "mississippi", create a set of unique letters
text = "mississippi"
unique_letters = {char for char in text}
print(unique_letters)

# 3. Convert all words to lowercase and remove duplicates
words = ["Python", "python", "JAVA", "java", "C++"]
lower_words = {word.lower() for word in words}
print(lower_words)


# --- Dictionary Comprehensions ---

# 4. Numbers 1 to 5 as keys and their squares as values
squares = {x: x**2 for x in range(1, 6)}
print(squares)

# 5. Key = word and value = length of word
words_list = ["apple", "dog", "car"]
word_lengths = {word: len(word) for word in words_list}
print(word_lengths)

# 6. Numbers 1 to 5 as keys and values are "even" or "odd"
even_odd_dict = {x: "even" if x % 2 == 0 else "odd" for x in range(1, 6)}
print(even_odd_dict)


# --- Generator Expressions ---

# 7. Generator for numbers doubled from 1 to 5, then convert to tuple
gen = (x * 2 for x in range(1, 6))
result = tuple(gen)
print(result)

# 8. Sum of squares from 1 to 5 using a generator expression
total = sum(x**2 for x in range(1, 6))
print(total)
