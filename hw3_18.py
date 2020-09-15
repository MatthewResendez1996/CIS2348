import math

# Dictionary of paint colors and cost per gallon
paint_colors = {
    'red': 35,
    'blue': 25,
    'green': 23
}

# FIXME (1): Prompt user to input wall's width
# Calculate and output wall area
wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))
wall_area = wall_height * wall_width
print('Wall area:', wall_area, "square feet")
paint = wall_area / 350
print(f"Paint needed: {paint:.2f} gallons")
print("Cans needed:", round(paint), "can(s)")

colorchoice = input("\nChoose a color to paint the wall:\n")
if colorchoice in paint_colors:
    price = paint_colors[colorchoice]
    totalprice = int(price) * round(paint)
    print("Cost of purchasing %s paint: $%d" % (colorchoice, totalprice))




