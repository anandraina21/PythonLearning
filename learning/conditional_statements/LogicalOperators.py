has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")
# elif has_high_income and not has_good_credit:
#     print("Ineligible for a loan")
# elif not has_high_income and has_good_credit:
#     print("Ineligible for loan still")
elif not has_good_credit or not has_high_income:
    print("Ineligible for the loan!")
# else:
#     print('Ineligible for loan')
