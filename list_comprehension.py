numbers = [45,87,96,65,43,90,85,14,26,61,70]
odd=[]
for num in numbers:
    if num % 2==1 and num%5==0:
        odd.append(num)
print(odd)