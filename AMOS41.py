#python program that gives response to the user based on their request
menu=['rice','noodles','beans','yam']
customers_request=(input('what do you want to be offered?'))
for meal in menu:
    if customers_request in menu:
        print('your requested meal is available')
        break
    else:
        print('your requested meal is not available')
        break
