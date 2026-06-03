with open("count_word.txt","w")as file:
    file.write("Hi my name is krushna and  I am 20 years old ")

with open("count_word.txt","r")as file:
    data = file.read()

print(len(data.split()))