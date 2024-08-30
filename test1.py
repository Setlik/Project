card_number = str(input())
private_number = card_number[:6] + ((card_number[6:-4])* '*') + card_number[-4:]
print(private_number)