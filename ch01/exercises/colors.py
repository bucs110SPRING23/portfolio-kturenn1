list = ["red", "green", "blue"]
mylist = list
length = int(len(mylist))
print("I have", length, "colors.")
print(*mylist, sep="\n")