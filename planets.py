planet_list = ["Mercury", "Mars"]

# Append list
planet_list.append("Jupiter")
planet_list.append("Saturn")
print (planet_list)

# Extended List
planet_list1 = ["Uranus", "Neptune"]
planet_list.extend(planet_list1)
print('Planet List: ', planet_list)

# Insert List

planet_list.insert(1, 'Earth')
planet_list.insert(1, 'Venus')
print('Updated List: ', planet_list)

# Append List
planet_list.append("Pluto")
print ('Add Pluto',planet_list)

# slice list
planet_list2 = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
rocky_planets = slice(1,4)
print('Slice:', planet_list2[rocky_planets])

# del pluto
del planet_list[8]
print('del', planet_list)