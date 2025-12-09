sentence = "List comprehension is powerful"
values = [len(word) for word in sentence.split()]
print(values*2)