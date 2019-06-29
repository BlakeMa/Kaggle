primes = [2,4,5,7]
print(primes)

plants = [[1,2,3,4],[3,4,5,6]]
print(plants)

newplants = [
    [1,3,4,5],
    [6,7,89,0]
]
print(newplants)


my_favourite = [32,newplants]
print(my_favourite);

data_plants = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

print(data_plants[0])
print(data_plants[2])
print(data_plants[-2])
print(data_plants[-1])
print(data_plants[0:3])
print(data_plants[3:])
print(data_plants[1:-1])
print(data_plants[-3])

data_plants[:3] = ['Mur', 'Vee', 'Ur']
print(data_plants)
data_plants[:4] = ['Mercury', 'Venus', 'Earth', 'Mars']
print(data_plants)
print(len(data_plants))
print(sorted(data_plants))
data_plants.append("Hello")
print(data_plants)

number = 2
print(number.bit_length())
print(data_plants.pop())
print(data_plants)
print("Mars" in data_plants)

x=0.45
a,b =x.as_integer_ratio()
print(a)
print(b)
