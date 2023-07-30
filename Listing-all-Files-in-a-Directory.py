import os

for i in os.listdir():  #since no directory is specified pyhton assumes the current direcotry 
    print(i)


# to specify a specific directory the path must be provided in the parenthesis as follows:
# os.listdir(r'C:\Users\Maryam\Documents')
# the r specifies raw string

# the same task can be accomplished by the use of glob.glob(r"*") 