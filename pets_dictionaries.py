#Pet dictionaries
pet1 = {
    "Animal": "Dog",
    "Owner": "Jimmy"
}

pet2 = {
    "Animal": "Cat",
    "Owner": "Maria"
}

pet3 = {
    "Animal": "Bunny",
    "Owner": "Willam"
}

pet4 = {
    "Animal": "Guinea pig",
    "Owner": "Nataly"
}

#Pet list
pets = [
    pet1, 
    pet2, 
    pet3, 
    pet4
]

#Print
for pet in pets:
    print("Animal:", pet["Animal"])
    print("Owner:", pet["Owner"])
    print()