code1, prod1, price1 = input().split()
code1 = int(code1)
prod1 = int(prod1)
price1 = float(price1)

code2, prod2, price2 = input().split()
code2 = int(code2)
prod2 = int(prod2)
price2 = float(price2)

value_to_pay = (prod1*price1)+(prod2*price2)

print(f"VALOR A PAGAR: R$ {value_to_pay:.2f}")
