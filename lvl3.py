#Looping Safe Practice - do not loop orginal list
group: list[str] = ['A', 'B', 'C', 'D']
new_group: list[str] = []

for group in groups:
    if group == 'B':
        continue
    else:
        print(item)
        new_group.append(group)