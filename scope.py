#global variable 
balance = 3000
def buy_things(item,price):
    # balance = 500
    #local scope variable
    #You can access global variable without using the global keyword
    global balance
    #If you can to modify a global variable, you have to use the global keyword
    dream_phone = 'xphone'
    print(f'Previous balance value',balance)
    balance = balance-price
    print(f"Balance after buying {item}",balance)
# print(dream_phone)
buy_things('sunglass',1000)
print('Global balance',balance)

    