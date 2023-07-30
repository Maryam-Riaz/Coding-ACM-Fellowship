num = int(input("How many numbers do you want to enter?"))

sum = 0

for i in range (num):
    input_num = int(input("Enter number : "))
    sum += input_num

avg = sum / num

print ("Average = ",avg)