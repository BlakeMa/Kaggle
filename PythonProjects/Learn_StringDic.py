import Learn_Booleans as LB
print("hello\"")
print('"Hello"')
print("Hello\nWorld!")

claim = "Pluto is a planet!"

print(claim.split())

pluto_mass = 303 * 10**2
print(pluto_mass)

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)

print(planet_to_initial.keys())
print(planet_to_initial.values())

LB.inspect(110)