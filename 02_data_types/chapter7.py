#tupples

masala_spices=("cardomom","cloves","cinnamon")

(spice1, spice2, spice3) = masala_spices

print(f"main masala spices: {spice1},{spice2},{spice3}")

ginger_ratio,cadomom_ratio=2,1
print(f"Ratio of G:{ginger_ratio}, and C:{cadomom_ratio}")
ginger_ratio, cadomom_ratio=cadomom_ratio,ginger_ratio
print(f"Ratio of G:{ginger_ratio}, and C:{cadomom_ratio}")


#membership test
print(f"Is ginger in masala spices? {'ginger' in masala_spices}")
print(f"Is cardomom in masala spices? {'cardomom' in masala_spices}")
print(f"Is cinnamon in masala spices? {'cinnamon' in masala_spices}")
print(f"Is cinnamon in masala spices? {'Cinnamon' in masala_spices}")