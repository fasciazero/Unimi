from calendar import isleap, weekday

# Punto 3
year = 2019
while not isleap(year):
	year += 1
print('Next leap year is', year)

# Punto 4
print('Number of leap years from 2000 to 2050 is', len([x for x in range(2000,2051) if isleap(x)]) )

# Punto 5
days_names = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
wd = weekday(2016,7,29)

print('Day of the week of 29th July 2016 is',days_names[wd])