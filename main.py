# list to tulp
kar = ["karthik", 1, 2]
k = tuple(kar)
print(k)
# tulp to list
kart = ("karthik", 2100030811)
r = list(kart)
print(r)
# dictinoary methods
kar = {"name": "karthik", "id no": "2100030811", "department": "CSE"}
print(kar)
x = kar.keys()
print(x)
y = kar.values()
print(y)
z = kar.items()
print(z)
kar.update({"name": "karthikeya"})
print(kar)
kar["Age"] = 18
print(kar)
kar.popitem()
print(kar)
#  change list to dictionory
players_country = [('MS Dhoni', 'India'), ('Chris Gayle', 'West Indies'),('Messi', 'Germany'), ('AB Devillies', 'South Africa'), ('Rohit Sharma', 'India')]
output_dict = {}
output_dict = dict(players_country)
print(output_dict)

data = [("Name :", "karthik"), ("id", 2100030811)]
print(dict(data))
a = 10
print(type(a))
karthik = ["karthik", 1, 2.5]
print(karthik)
print(karthik(0 : 1))
print(karthik(1:3))
