# 1: Tuples
cars = ("Mercedes", "R34", "Pagani", "Dodge", "MacLarren")
print(cars)
print(cars[2])
print(cars[1:4])
print(cars[1:])
for gari in cars:
    print(cars)

# 2: Lists
colours = ["Red", "Green", "Purple", "Blue", "Grey", "Black"]
print(colours)
print(colours[2])
colours[0] = "Light Red"
print(colours[1:4])
print(colours[1:])
for rangi in colours:
 print(rangi)
print(colours)
colours.reverse()
colours.pop(1)
print(colours)
colours.sort(reverse=True)
print(colours)

# 3: Dictionaries
students = {"ADM1": "Tracy", "ADM2": "Moses", "ADM3": "Eugene"}
print(students["ADM1"])
for funguo in students.keys():
    print(funguo)

    for jina in students.values():
        print(jina)


# 3: Sets
ranks = {1, 5, 8, 4, 0, 5, 3, 2, 1, 6, 8, 10, 11, 12, 10}
print(ranks)

players = ["Kevin De", "Bruyne", "Grealish", "Walker", "Ederson", "Dias", "Aguero"]
generatedlist = []
for n in players:
    if len(n) > 5:
        generatedlist.append(n)

        for x in generatedlist:
            print(x)





