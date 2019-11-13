How many coins?
# Write a program that will prompt you for how many coins you want. 
# Initially you have no coins. It will ask you if you want a coin? 
# If you type "yes", it will give you one coin, and print out the current tally. 
# If you type no, it will stop the program. 

coin = "yes"
count = -1

while coin == "yes":
    count = count + 1
    print("You have %d coins" % count)
    coin = input("Do you want another? ")
print("Bye")