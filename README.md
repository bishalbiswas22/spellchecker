Dictionary based spell checking in Python
SpellCheck is a spelling checking and correction module in Python built using Fuzzywuzzy string matching module.

Steps to get started
Create your own dictionary of word

Import the spellcheck module in your script
from spellcheck import SpellCheck

Initialize the spellcheck object in your code
spell_check =  SpellCheck('words.txt')

Use the object to get suggested words or corrected string
print(spell_check.suggestions())
print(spell_check.correct())
