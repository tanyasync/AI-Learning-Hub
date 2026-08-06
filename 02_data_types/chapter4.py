#boolean 

is_boiling=True
stir_count=5
total_actions=stir_count + is_boiling #upcasting boolean to integer
print(f"Total actions:{total_actions}")

milk_present=None #no milk
print(f"Is there Milk? {bool(milk_present)}")

water_hot=True
tea_added=False

can_server=water_hot and tea_added
print(f"can serve tea? {can_server}")