# Leetspeak
# Given a paragraph of text as a string, print the paragraph in leetspeak. To translate a string to leetspeak, you need to replace make the following character
# replacements (treat all input characters as uppercase):

text = "In this program we have used nested for loops"

for index in range(len(text)):
    if text[index] == "A":
        text[index] = "4"
    if text[index] == "E":
        text[index] = "3"
    if text[index] == "G":
        text[index] = "6"
    if text[index] == "I":
        text[index] = "1"
    if text[index] == "O":
        text[index] = "0"
    if text[index] == "S":
        text[index] = "5"
    if text[index] == "T":
        text[index] = "7"