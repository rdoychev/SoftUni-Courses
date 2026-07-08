def mask_credit_card(card_number):
    card_str = str(card_number)
    n = len(card_str)
    new_card = ""
    for i in range(n):
        if i < n - 4:
            new_card += "*"
        else:
            new_card += card_str[i]

    return new_card


card = "123456789"
aa = mask_credit_card(card)
print(aa)

print(card[-5:-8:-1])
