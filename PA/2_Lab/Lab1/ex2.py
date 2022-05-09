alkaline_earth_metals = [('Barium',56),('Beryllium',4),('Calcium',20),('Magnesium',12),('Radium',88),('Strontium',38)]

# Punto 1
highest_material =  sorted(alkaline_earth_metals,key=lambda x : x[1],reverse=True)[0]
print( 'Material with the highest atomic number is {0} with {1}'.format(highest_material[0],highest_material[1]) )

# Punto 2
print( sorted(alkaline_earth_metals,key=lambda x : x[1]) )

# Punto 3
alkaline_earth_metals_dict = dict(alkaline_earth_metals)
print( alkaline_earth_metals_dict )

# Punto 4
noble_gases = {'Helium':2, 'Neon':10, 'Argon':18, 'Krypton':36, 'Xenon':54, 'Radon':86}

# Punto 5
all_togheter = [(name,n) for name,n in alkaline_earth_metals_dict.items()]
all_togheter += [(name,n) for name,n in noble_gases.items()]
print( sorted(all_togheter) ) 