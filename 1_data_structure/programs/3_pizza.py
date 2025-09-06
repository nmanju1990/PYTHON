n = int(input("Enter number of people: "))
x = int(input("Enter slices needed per person: "))

# total slices required
total_slices = n * x

# pizzas needed (each pizza has 4 slices)
if total_slices % 4 == 0:
    pizzas = total_slices // 4
else:
    pizzas = (total_slices // 4) + 1

print("Pizzas needed:", pizzas)
