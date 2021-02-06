import timeit

#------- 1st Solution -------------------
def fizzbuzz_noob():
    for i in range(1, 101):
        if(i%15==0):
            print('fizzbuzz')
        elif(i%5==0):
            print('buzz')
        elif(i%3==0):
            print('fizz')
        else:
            print(i)
start = timeit.default_timer()
fizzbuzz_noob()
stop = timeit.default_timer()


#------- 2nd Solution -------------------
def fizzbuzz_better():
    for i in range(1, 101):
        res = ''
        if (i % 3 == 0): res += 'fizz'
        if (i % 5 == 0): res += 'buzz'
        if (res == ''):
            print(i)
        else:
            print(res)
start1 = timeit.default_timer()
fizzbuzz_better()
stop1 = timeit.default_timer()


#---------- 3rd solution ----------------
def fizzbuzz_pro():
    c3 = 0
    c5 = 0
    for i in range(1, 101):
        c3 += 1
        c5 += 1
        res = ''
        if (i % 3 == 0): 
            res += 'fizz'
            c3 = 0
        if (i % 5 == 0):
            res += 'buzz'
            c5 = 0
        if (res == ''):
            print(i)
        else:
            print(res)
start2 = timeit.default_timer()
fizzbuzz_pro()
stop2 = timeit.default_timer()



print('brute force', stop - start)
print('better', stop1 - start1)
print('pro', stop2 - start2) 
