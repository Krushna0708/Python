with open("main.txt","w") as file:
    file.write("Hello ")
file = open("main.txt","a")
file.write("World!")
file.close()