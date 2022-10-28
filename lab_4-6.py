# Creator CS 10/18/2022

# Ask user what animal will be coming, and what dish they are bringing out
beast = input("What animal will be bringing the dish?")
dish = input("What dish will be brought out?")

#checking if the first letter of the beast's name is the same as the first and last letter of the dish's name,
#and printing if they are allowed to bring their dish
if beast[0] == dish[0] and beast[0] == dish[len(dish)-1]:
    print ("The beast is allowed to bring the dish to the feast!")
else:
    print ("The beast is NOT allowed to bring the dish to the feast!")    