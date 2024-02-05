# def full_name(first,last):
#     # name = f'{first} {last}'
#     name = ('Full name is: ' +first+' '+last)
#     return name
# #take parameteres in prder(serial order)
# # name =full_name('Alu','kodu')
# name = full_name(last='Kodu',first='Alu')
# print(name)

def all_num(num1,num2):
    sum = num1+num2
    mul = num1+num2
    div =  num1/num2
    sub = num1-num2
    # return [sum,mul,div,sub]
    return sum,mul,div,sub
every_things=all_num(45,5)
print(every_things)