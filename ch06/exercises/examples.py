
#json is a string format not a file format
import json

def example():
    idea = input("Enter an idea: ")
    ideas = []
    ideas.append(idea)
    print(ideas)

def main():
    file_pointer = open("assets/ideas.txt", "r")
    
    #reads everything
    ideas = file_pointer.read()
    print(ideas)

    #reads everything "line by line" (says /n)
    ideas = file_pointer.readlines()
    print(ideas)

    #reads the "first" line (wherever the cursor was last)
    ideas = file_pointer.readline()
    print(ideas)
    ideas = file_pointer.readline()
    print(ideas)

    #closing the file resets the cursor
    file_pointer.close()

    #print the 3rd line
    ideas = file_pointer.readlines()
    print(ideas[2])

    #when using "w" (write) you are STARTING OVER. the file is cleared
    #if it doesn't exist it is created
    file_pointer = open("assets/ideas.txt", "w")

    idea = input("Enter an idea: ")
    ideas = []
    ideas.append(idea)

    for i in ideas:
        file_pointer.write(i)
        
    #when using "a" (append) you are moving the cursor to the end of the file
    #if it doesn't exist it is created
    file_pointer = open("assets/ideas.txt", "a")

    idea = input("Enter an idea: ")
    ideas = []
    ideas.append(idea)

    for i in ideas:
        #the write command writes EXACTLY what you write.
        file_pointer.write(i)
        file_pointer.write(i + "\n")

        # \n is new line \t is tab \s is space
        # \\ is the escape character (ex- "\\n" will print \n - where "\n" makes a new line)
        
    #when editing the file, always close it
    file_pointer.close()

main()