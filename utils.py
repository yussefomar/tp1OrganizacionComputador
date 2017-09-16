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

