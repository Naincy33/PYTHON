def is_mnemonic_correct(solar_system, mnemonic):
    filtered_planets = [planet for planet in solar_system if planet != "Asteroid"]
    
    
    
    mnemonic_letters = [word[0].upper() for word in mnemonic.split()]
    
    
    planet_letters = [planet[0].upper() for planet in filtered_planets]
    
     
    return mnemonic_letters == planet_letters


solar_system = ["Mercury", "Venus", "Earth", "Mars", "Asteroid", "Jupiter", "Saturn", "Uranus", "Neptune"]
mnemonic = "My Very Efficient Mother Just Served Us Nuts"

print(is_mnemonic_correct(solar_system, mnemonic))
