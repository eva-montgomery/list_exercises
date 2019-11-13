# De-dup
# Given an list of numbers or strings, create a new list containing the same elements as the rst list, except with any duplicate values removed. Print the list.

de_dup = ["horse", "dog", "bird", "cat"]
de_dup_2 = ["horse", "dog", "bird", "cat", "flamingo", "mouse", "rat"]
de_dup_3 = de_dup + de_dup_2
print(de_dup_3[4:])