#Looping Safe Practice - do not loop orginal list
items: list[str] = ['A', 'B', 'C', 'D']
new_items: list[str] = []

for item in items:
    if item == 'B':
        continue
    else:
        print(item)
        new_items.append(item)