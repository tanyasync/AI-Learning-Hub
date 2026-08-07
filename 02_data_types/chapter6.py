#strings

chai_type="Ginger chai"
customer_name="Tanya"
print(f"order for {customer_name} is {chai_type}")

chai_description="Aromatic and Bold"
print(f"First word: {chai_description[0:8]}")
print(f"First word: {chai_description[0:8:1]}")
print(f"First word: {chai_description[0:8:2]}")
print(f"First word: {chai_description[:8]}")
print(f"Last word: {chai_description[13:]}")
print(f"Last word: {chai_description[13:17:2]}")
print(f"Last word: {chai_description[::-1]}") #reverse string

label_text="Chai Speàcial"
encoded_label=label_text.encode("utf-8")
print(f"encoded label: {encoded_label}")
print(f"Non encoded label:{label_text}")
decoded_label= encoded_label.decode("utf-8")
print(f"decoded label:{decoded_label}")
print(f"Non decoded label:{label_text}")
