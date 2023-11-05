from multiprocessing import Value
import os

Items = ["Your first idea."]

print("DoIt V0.0.1")
print("Type 'help' for help")

def TakeInput():
    Input = input("Command: ").lower()

    if Input == "help":
        print("Add: homework")
        print("Delete: 1")
        print("Get: 1")
        print("Edit: 1:")
        print("List")
        print("Save")
    elif "add:" in Input:
        Items.append(Input.split(":", 1)[1])
        print("Added Item #", len(Items))
    elif "delete:" in Input:
        try:
           if 0 <= int(Input.split(":", 1)[1]) < len(Items):
               Items.pop(int(Input.split(":", 1)[1]))
               print("Removed item #" + Input.split(":", 1)[1])
           else:
                print("Item does not exist")
        except ValueError:
                print("Invalid input. Please provide a valid index.")
    elif "get:" in Input:
        try:
            if 0 <= int(Input.split(":", 1)[1])  < len(Items):
                print(Items[int(Input.split(":", 1)[1])])
            else:
                print("Item does not exist")
        except ValueError:
            print("Invalid input. Please provide a valid index.")
    elif "edit:" in Input:
        try:
            if 0 <= int(Input.split(":", 1)[1]) - 1 < len(Items):
                Items[int(Input.split(":", 1)[1]) - 1] = Input.split(":")[2]
                print("Edited item #" + Input.split(":", 1)[1] + ".")
            else:
                print("Item does not exist")
        except ValueError:
            print("Invalid input. Please provide a valid index.")
            
    elif "list" in Input:
        Index = 0
        for Item in Items:
            print(str(Index + 1) + ": " + Item)
    elif "save" in Input:
        Index = 0
        for Item in Items:
            open("DoIt Items.txt", "w").write(str(Index + 1) + ": " + Item + "\n")
            print("Saved to working directory.")

while True:
    TakeInput()
