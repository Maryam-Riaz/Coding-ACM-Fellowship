import datetime

str = datetime.datetime.now()
print(str)

# a visually better way to display this
print (str.strftime("%d/%m/%Y, %H:%M:%S"))