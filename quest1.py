def isPrime(num):
    if num==2 or num==3:
        return True
    elif num%2 or num<2:
        return False
    for n in range(3,int(num**1/2)+1,2):
        if num%n==0:
            return False
    return True

sum=0
list1=[]

for num in range(1,100):
    if isPrime(num) is True:
        sum+=num
        list1.append(sum)
print(list1)
list2=[]
for sum in list1:
    if sum<100:
        if isPrime(sum) is True:
            list2.append(sum)
print(list2)
print(max(list2))
