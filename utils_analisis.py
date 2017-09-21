from math import cos, asin, sqrt
def calcular_distancia(origen, destino):
    lat1 = origen[0]
    lon1 = origen[1]
    lat2 = destino[0]
    lon2 = destino[1]
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a)) 

def _stringToInt(num):
    x,y = num.split(".")
    res = 10**len(y)*int(x)
    if res < 0:
        res = res - int(y)
    else:
        res = res + int(y)
    return res*(10**-len(y))

def latLonToInt(latlon):
	try:
    		latlon = latlon.split(",")
    
   		lat = latlon[0]
    		lon = latlon[1]
    		res = (_stringToInt(lat),_stringToInt(lon))
    		return res
	except:
		return (-50.788796, -70.777773) #Si esta mal formateado lat-lon devuelvo un punto muy lejano 
