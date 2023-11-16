

num = input("enter number")


print(num)
# 1 000 000
# 0 123 456

# ,000
str = ""



for n in range(len(num)-1 , -1 ,-1):
    str = num[n] + str
    if n % 3 == 1 :
        str = "," + str


print("hi" , str)

    
