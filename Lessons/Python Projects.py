distance = float(input("Enter distane travlled in kms: "))
fuel_eff = float(input("Enter fuel efficiency of your vehicle in km/litre: "))
price = float(input("Enter the current price of fuel per liter: "))
passengers = float(input("Enter the number of people in the vehicle: "))

print(f"The total amount of fuel needed is {round(distance/fuel_eff,2)} litres.")
print(f"The cost of fuel is ${round(distance/fuel_eff*price,2)}")
print(f"tThe cost of fuel per passenger is ${round(distance/fuel_eff*price/passengers,2)}")