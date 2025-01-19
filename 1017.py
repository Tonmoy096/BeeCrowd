spent_time = int(input(" Enter the spent time (hours): "))

average_speed = int(input(" Enter the evrage speed (km/h): "))

distance = spent_time * average_speed

per_km = 12

fuel_needed = distance/per_km

print(f" {fuel_needed:.3f} ")
