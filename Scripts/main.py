import qqq,os

#print(os.name)
#print(list(x**2 for x in range(10) if x<5))
def get_pow(num):
    print('gfgf')
    a,b = 0,1
    while True:
        yield a
        a, b = b, a + b
ggg=get_pow(5)

print(next(ggg(5)))
print(next(id(ggg)))
# print(ggg.__next__())
# print(ggg.__next__())
# print(ggg.__next__())
# print(ggg.__next__())




#print(list(get_pow(4,2)))
