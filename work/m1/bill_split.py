amt, tip, ppl = input("Pls input bill amount, tip %, and no. of diners separated by commas: ").split(",")
amt = float(amt)
tip = int(tip)
ppl = int(ppl)

total = amt * (1 + tip/100)
print(f"Each person pays ${total/ppl:.2f}")