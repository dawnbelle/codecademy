# sal's shipping costs

weight = 50

# ground shipping
if weight <= 2:
	cost_ground = weight * 1.50 + 20
elif weight <= 6:
	cost_ground = weight * 3.00 + 20
elif weight <= 10:
	cost_ground = weight * 4.00 + 20
else:
	cost_ground = weight * 4.75 + 20
print("Ground Shipping $", cost_ground)

# premium shipping 
cost_premium = 125.00
print("Ground Premium $", cost_premium)

# drone shipping
if weight <= 2:
	cost_drone = weight * 4.50 
elif weight <= 6:
	cost_drone = weight * 9.00
elif weight <= 10:
	cost_drone = weight * 12.00
else: 
	cost_drone = weight * 14.25
print("Drone Shipping $", cost_drone)
