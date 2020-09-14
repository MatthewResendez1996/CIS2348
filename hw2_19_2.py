lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))
water_cups = float(input('Enter amount of water (in cups):\n'))
agave_nectar_cups = float(input('Enter amount of agave nectar (in cups):\n'))
servings_cups = float(input('How many servings does this make?\n'))

print (f"\nLemonade ingredients - yields {servings_cups:.2f} servings",)
print (f"{lemon_juice_cups:.2f} cup(s) lemon juice")
print (f"{water_cups:.2f} cup(s) water")
print (f"{agave_nectar_cups:.2f} cup(s) agave nectar")

useramt = float (input ("\nHow many servings would you like to make?\n"))
cuseramt = (useramt / servings_cups)
clemon = (cuseramt * lemon_juice_cups)
cwater = (cuseramt * water_cups)
cagave = (cuseramt * agave_nectar_cups)

print (f"\nLemonade ingredients - yields {useramt:.2f} servings",)
print (f"{clemon:.2f} cup(s) lemon juice")
print (f"{cwater:.2f} cup(s) water")
print (f"{cagave:.2f} cup(s) agave nectar")

dink = 16
clemongal = (clemon / dink)
cwatergal = (cwater / dink)
cagavegal = (cagave / dink)
print (f"\nLemonade ingredients - yields {useramt:.2f} servings",)
print (f"{clemongal:.2f} gallon(s) lemon juice")
print (f"{cwatergal:.2f} gallon(s) water")
print (f"{cagavegal:.2f} gallon(s) agave nectar")
