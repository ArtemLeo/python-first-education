# Converting miles to km

def miles_to_km(miles):
    return str(miles) + ' miles = ' + str((miles * 1.6)) + ' km'


mile_distance = 2.3
km_distance = miles_to_km(mile_distance)
print(km_distance)
