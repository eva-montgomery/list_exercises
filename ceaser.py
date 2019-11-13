# Caesar Cipher
# Given a string, print the Caesar Cipher (or ROT13) of that string. What is Caesar Cipher? http://practicalcryptography.com/ciphers/caesar-cipher/
# Use your solution to decipher the following text: "lbh zhfg hayrnea jung lbh unir yrnearq


alphabet = list("abcdefghijklmnopqrstuvwxyz") #--> convert to list
rotate_by = 13

sentence = "lbh zhfg hayrnea jung lbh unir yrnearq"

# letter = "a"
# --> find the position of letter a
# then 13 to it
result = ""

for letter in sentence:
    try:
        position = alphabet.index(letter)
        new_position = (position + rotate_by) % 26
        new_letter = alphabet[new_position]
        result += new_letter
    except ValueError:
        result += letter    
print(result)
