import cProfile
def fun():
    s= 0
    for i in range (11):
        s+=i
    print ("Sum of first 10 positive integers :",s)
cProfile.run('fun()')
