# -*- coding: utf-8 -*-
import pandas as pd
def recuperar_superficie(rowProperati):
    if pd.isnull(rowProperati['surface_total_in_m2']):

        if (not((pd.isnull(rowProperati['price_aprox_usd']))) and (not(pd.isnull(rowProperati['price_usd_per_m2'])))):
            
            return rowProperati['price_aprox_usd']/rowProperati['price_usd_per_m2']
           
        else:
            return rowProperati['surface_total_in_m2']
    else:
        return rowProperati['surface_total_in_m2']

def recuperar_precio_usd(rowProperati):
    
    if pd.isnull(rowProperati['price_aprox_usd']):
    
        if (not(pd.isnull(rowProperati['surface_total_in_m2'])) and (not(pd.isnull(rowProperati['price_usd_per_m2'])))):
            
            return rowProperati['surface_total_in_m2']*rowProperati['price_usd_per_m2']
           
        else:
            return rowProperati['price_aprox_usd']
    else:
        return rowProperati['price_aprox_usd']

def recuperar_ppm2(rowProperati):
    if pd.isnull(rowProperati['price_usd_per_m2']):
        
        if (not(pd.isnull(rowProperati['price_aprox_usd'])) and (not(pd.isnull(rowProperati['surface_total_in_m2'])))):
        
            try:
                return rowProperati['price_aprox_usd']/rowProperati['surface_total_in_m2']
                
            except ZeroDivisionError:
                #Despues se filtra
                return 0
        else:
            return rowProperati['price_usd_per_m2']
    else:
        return rowProperati['price_usd_per_m2']


#Hay bastantes registros de capital federal que tienen como 'place_name' a 'Capital Federal'
#Se intenta recuperar la verdadera localidad usando geopy.
from geopy.geocoders import Nominatim
barrios_capital = [u' Agronomía',
    u' Almagro',
    u' Balvanera',
    u' Barracas',
    u' Belgrano',
    u' Boedo',
    u' Caballito',
    u' Chacarita',
    u' Coghlan',
    u' Colegiales',
    u' Constitución',
    u' Flores',
    u' Floresta',
    u' La Boca',
    u' La Paternal',
    u' Liniers',
    u' Mataderos',
    u' Monte Castro',
    u' Monserrat',
    u' Nueva Pompeya',
    u' Núñez',
    u' Palermo',
    u' Parque Avellaneda',
    u' Parque Chacabuco',
    u' Parque Chas',
    u' Parque Patricios',
    u' Puerto Madero',
    u' Recoleta',
    u' Retiro',
    u' Saavedra',
    u' San Cristóbal',
    u' San Nicolás',
    u' San Telmo',
    u' Vélez Sársfield',
    u' Versalles',
    u' Villa Crespo',
    u' Villa del Parque',
    u' Villa Devoto',
    u' Villa General Mitre',
    u' Villa Lugano',
    u' Villa Luro',
    u' Villa Ortúzar',
    u' Villa Pueyrredón',
    u' Villa Real',
    u' Villa Riachuelo',
    u' Villa Santa Rita',
    u' Villa Soldati',
    u' Villa Urquiza',
 ]
geolocator = Nominatim()

def recuperar_barrio_capital(row):
	"""PRE: row es un registro de capital federal con barrio incorrecto
	POST: devuelve el place_name corregido o el original si no hacia falta corregir.
	Si no se puede corregir porque no se tiene la lat-lon, devuelve 'Capital Federal'"""
	
	if not(pd.isnull(row["lat-lon"])):
		
		info = geolocator.reverse(row["lat-lon"])
		a = info.address
		if (a != None):
			direccion = a.split(",")
		else:
			return row["place_name"]
			
		for b in barrios_capital:
			if b in direccion:
				
				return b
	return row["place_name"]

