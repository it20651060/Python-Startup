thisdict = {"id" : 100, "name" : "Saman", "salary" : 50000.0}

print(thisdict)

print("Accessing elements")
# Accessing elements
print(thisdict["id"])
print(thisdict["name"])
print(thisdict["salary"])

print("Adding elements")
#Adding elements
thisdict["bonus"] = 10000
print(thisdict)

print("modifying elements")
#modifying elements
thisdict["salary"] = 60000.0
print(thisdict)

print("modifying elements")
#modifying elements
thisdict["Bonus"] = 20000.0
print(thisdict)

print("adding other collections")
#adding other collections
thisdict["address"] = {"no" : 51, "street" : "1st lane", "town" : "kandy"}
thisdict["mobile"] = ["0718921122", "0723232222"]

print(thisdict)

print("town")
# town
print(thisdict["address"])
print(thisdict["address"]["town"])

ptint("2nd mobile number")
# 2nd mobile number
print(thisdict["mobile"])
print(thisdict["mobile"][1])