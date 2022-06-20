def item_obtained(material):
    if material == "shards":
        return "Shadowmourne"
    elif material == "fragments":
        return "Valanyr"
    else:
        return "Dragonwrath"


found = False
key_dict = {"shards": 0, "fragments": 0, "motes": 0}
junk_dict = {}

while not found:
    materials = input().split()
    materials = [i.lower() for i in materials]
    key_material = "shards", "fragments", "motes"
    item_found = False

    for i in range(0, len(materials), 2):
        if materials[i + 1] in key_material:
            key_dict[materials[i + 1]] += int(materials[i])
            if key_dict[materials[i + 1]] >= 250:
                print(f"{item_obtained(materials[i + 1])} obtained!")
                key_dict[materials[i + 1]] -= 250
                found = True
                break
        else:
            if materials[i + 1] not in junk_dict:
                junk_dict[materials[i + 1]] = 0
            junk_dict[materials[i + 1]] += int(materials[i])

sorted_key = sorted(key_dict.items(), key=lambda x: (-x[1], x[0]))
for k, v in sorted_key:
    print(f"{k}: {v}")
sorted_junk = sorted(junk_dict.items(), key=lambda x: (x[0], -x[1]))
for k, v in sorted_junk:
    print(f"{k}: {v}")