# is_hot = False
# is_cold = False
#
# if is_hot:
#     print("It is a hot day")
#     print("Drink water")
# elif is_cold:
#     print("It is a cold day")
#     print("Drink soup")
# else:
#     print("It's a lovely day")
#     print("Drink pepsi")
#
# print("Enjoy your day!")

price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.2 * price
    print(f'Down payment: ${down_payment}')
else:
    down_payment = 0.3 * price
    print(f'Down payment: ${down_payment}')
