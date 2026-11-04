usage = input("Enter your electricity use in kWh: ")

try: 
    usage = float(usage)
except ValueError:
    print("Please enter a number")
else:
    above600 = 0
    threeto6 = 0
    below300 = 0
    if usage >= 600:
        above600 = usage - 600
        threeto6 = 300
        below300 = 300
    elif usage >= 300:
        threeto6 = usage - 300
        below300 = 300
    else:
        below300 = usage

    bill = below300*0.3 + threeto6*0.35 + above600*0.4
    print(f"Electricity bill: ${bill:.2f}")