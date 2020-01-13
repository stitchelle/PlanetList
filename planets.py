planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")
print (planet_list)

# another list of planets
planet_list1 = ["Uranus", "Neptune"]

planet_list.extend(planet_list1)

# Extended List
print('Planet List: ', planet_list)