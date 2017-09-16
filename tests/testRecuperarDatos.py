import pandas as pd
import pytest
import numpy as np
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from utils import recuperar_superficie,recuperar_precio_usd,recuperar_ppm2


def testRecuperarPrecioPorM2ConInformacionSuficiente():
	df = pd.read_csv('datos.csv')
	df['price_usd_per_m2'] = df.apply(lambda row: recuperar_ppm2(row),axis=1)
	dato1 = df.loc[(df["id"] == 3),"price_usd_per_m2"].values[0]
	assert dato1 == float(1503921)/43281

def testRecuperarSuperficieTotalConInformacionSuficiente():
	df = pd.read_csv('datos.csv')
	df['surface_total_in_m2'] = df.apply(lambda row: recuperar_superficie(row),axis=1)
	dato1 = df.loc[(df["id"] == 1),"surface_total_in_m2"].values[0]
	assert dato1 == float(3829421)/2350

def testRecuperarPrecioTotalConInformacionSuficiente():
	df = pd.read_csv('datos.csv')
	df['price_aprox_usd'] = df.apply(lambda row: recuperar_precio_usd(row),axis=1)
	dato1 = df.loc[(df["id"] == 2),"price_aprox_usd"].values[0]
	assert dato1 == 25392*1980

def testRecuperarPrecioPorM2SinInfoSuficiente():
	df = pd.read_csv('datos.csv')
	df['price_usd_per_m2'] = df.apply(lambda row: recuperar_ppm2(row),axis=1)
	dato1 = df.loc[(df["id"] == 4),"price_usd_per_m2"].values[0]
	assert pd.isnull(dato1)

def testRecuperarSuperficieTotalSinInformacionSuficiente():
	df = pd.read_csv('datos.csv')
	df['surface_total_in_m2'] = df.apply(lambda row: recuperar_superficie(row),axis=1)
	dato1 = df.loc[(df["id"] == 4),"surface_total_in_m2"].values[0]
	assert pd.isnull(dato1)

def testRecuperarPrecioTotalSinInformacionSuficiente():
	df = pd.read_csv('datos.csv')
	df['price_aprox_usd'] = df.apply(lambda row: recuperar_precio_usd(row),axis=1)
	dato1 = df.loc[(df["id"] == 5),"price_aprox_usd"].values[0]
	assert pd.isnull(dato1)
