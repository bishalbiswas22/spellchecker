# Import the spellchecker library
from spellchecker import SpellChecker

# Create an object
spell = SpellChecker()

# Function to check spelling and provide suggestions
def check_spelling(text):
    words_to_check = text.split()
    misspelled = spell.unknown(words_to_check)
    for word in misspelled:
        print(f"Suggestions for '{word}': {spell.candidates(word)}")
        print(f"Correction for '{word}': {spell.correction(word)}")

# Get user choice for input method
choice = input("Enter '1' to input text manually or '2' to read from a file: ")

if choice == '1':
    # Take user input
    string_to_be_checked = input("dehl, superfst ")
    check_spelling(string_to_be_checked)
elif choice == '2':
    # Read input from a file
    file_path = input("/content/words.txt ")
    try:
        with open('/content/words.txt', 'r') as file:
            string_to_be_checked = file.read().strip()
            check_spelling(string_to_be_checked)
    except FileNotFoundError:
        print(f"File at path '{file_path}' not found.")
else:
    print("Invalid choice. Please enter '1' or '2'.")
