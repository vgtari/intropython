names = ["Hannah", "Otto", "Eevee", "Adharahda ", "Renneria", "Bob"]
requestedlist = []
for x in names:
    if len(x) > 4 and len(x) < 7:
        requestedlist.append(x)

for x in requestedlist:
    print(x)

names.sort()
for x in names:
    if len(x) > 7:
        print(x)
