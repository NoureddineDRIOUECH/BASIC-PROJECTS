credit_card_number = input("Enter yout credit card number : ")
credit_card_number = credit_card_number.replace("-","")
credit_card_number = credit_card_number.replace(" ","")
credit_card_number = credit_card_number[::-1]
add_some = 0
add_even_digits = 0
total =0
for i in credit_card_number[::2]:
    add_some += int(credit_card_number[int(i)])
for i in credit_card_number[1::2]:
    i = int(i)*2
    if i >=10:
        add_even_digits += (1+(i%10))
    else:
        add_even_digits += i
total = add_some + add_even_digits
if total%10 == 0:
    print("VAlID")
else:
    print("INVALID Please try again")