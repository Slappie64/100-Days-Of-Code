print("Tip Calculator")

bill_amount = float(input("How much was the total for the bill? \n£"))
tip_amount = 1 + float(input("How much tip would you like to leave? (Percentage) \n")) / 100
total_people = float(input("How many people is this split between? \n"))

bill_with_tip = bill_amount * tip_amount
amount_per_person = bill_with_tip / total_people

formatted_amount = "{:.2f}".format(amount_per_person)

print(f"Each person should pay £{formatted_amount}")