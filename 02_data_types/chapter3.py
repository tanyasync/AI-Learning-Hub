 #integer

black_tea_grams=14
ginger_grams=5

total_grams=black_tea_grams+ginger_grams
print(f"Total grams of base tea is {total_grams}")

remaining_tea=black_tea_grams-ginger_grams
print(f"Total grams of remaining tea is {remaining_tea}")

milk_litres=7
servings=4
milk_per_serving=milk_litres/servings
print(f"Milk per serving is {milk_per_serving}")

total_tea_bags=7
pots=4
bags_per_pot=total_tea_bags//pots
print(f"Tea bags per pot: {bags_per_pot}")

total_cardomom_pods=10
pods_per_cup=3
leftover_pods=total_cardomom_pods%pods_per_cup
print(f"Leftover cardomom pods: {leftover_pods}")

base_flavour_strength=3
scale_factor=2
powerful_flavour=base_flavour_strength**scale_factor
print(f"Scaled flavour strength:{powerful_flavour}")
#2*2*2

total_tea_leaves_harvested=1_000_000_000
print(f"tea leaves:{total_tea_leaves_harvested}")
