file_name = "guest.txt"

while(True):
    name = input()
    if(name == "quit"):
        break
    else:
        print(f"hello {name}")

    with open(file_name, 'a') as file_object:
        file_object.write("\n"+name)
f = open("guest.txt", "r")
print(f.read().rstrip())
