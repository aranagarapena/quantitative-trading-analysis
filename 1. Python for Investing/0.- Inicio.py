# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# ---------------------------- IMPORTS ---------------------------- 
import yfinance as yf
import pandas as pd
from pandas_datareader import data as pdr
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt

# definicion temporalidad de datos
anios_datos = 5
fin  = dt.datetime.now()
inicio = fin - dt.timedelta(365*anios_datos)

# bajada de datos
tickers = ['MSFT','SPY','QQQ']
df = yf.download(tickers, start=inicio , end=fin)


# filtramos los datos que nos interesan
adj_close_price = df['Adj Close']

# ---------------------------- CALCULO DE RENDIMIENTOS ---------------------------- 
"""
1.- Rendimiento Simple (Aritmético) - Lo mide en porcentaje
    
    - Formula: rt = Pt-Pt-1/pt-1
    - Descipción: Este tipo de rendimiento mide el cambio porcentual en el 
        precio de un activo entre dos períodos consecutivos. Es el tipo más 
        básico de rendimiento.
    - Ejemplo: Si una acción pasa de $100 a $105, el rendimiento simple es
        105-100/100=0,05 o 5%

2.- Rendimiento Logarítmico

    - Formula: log return = ln(Pt/Pt-1)
    - Descripción: Mide el efecto acumulado de los rendimientos sobre un período
        más largo. Por propiedades de logartimos
    - Ejemplo:  Si una acción pasa de $100 a $105, el rendimiento logaritmico es
        ln(105/100)=0.04879
        
Por que usar uno u optro: para encontrar el rendimeinto total los logaritmicos se 
    pueden sumar, en el simple habria que aplicar los facotres de crecimiento y restar 1.

"""

# calculamos los rendimientos
simple_returns = (adj_close_price-adj_close_price.shift(1))/adj_close_price.shift(1)
log_returns = np.log(adj_close_price/adj_close_price.shift(1))

# otros retornos
absolute_difference =  adj_close_price-adj_close_price.shift(1) # diferencia absoluta

"""
Rendimientos acumulativos: 
    
   Los rendimientos acumulativos muestran cómo ha evolucionado la inversión a lo 
    largo del tiempo. Cada valor en la serie representa el rendimiento total 
    desde el inicio de la serie de datos hasta ese punto en el tiempo.
    
    Por ejemplo, si tienes una serie de rendimientos logarítmicos diarios, 
    los rendimientos acumulativos te mostrarán cómo ha crecido (o disminuido) el 
    valor de tu inversión en cada día, tomando en cuenta todos los días anteriores.

"""

cumulative_returns = log_returns.cumsum()


# Añadir las columnas de los retornos al DataFrame original
df['MSFT Simple Returns'] = simple_returns['MSFT']
df['SPY Simple Returns'] = simple_returns['SPY']
df['QQQ Simple Returns'] = simple_returns['QQQ']

df['MSFT Log Returns'] = log_returns['MSFT']
df['SPY Log Returns'] = log_returns['SPY']
df['QQQ Log Returns'] = log_returns['QQQ']

df['MSFT Absolute Difference'] = absolute_difference['MSFT']
df['SPY Absolute Difference'] = absolute_difference['SPY']
df['QQQ Absolute Difference'] = absolute_difference['QQQ']

df['MSFT Cumulative Returns'] = cumulative_returns['MSFT']
df['SPY Cumulative Returns'] = cumulative_returns['SPY']
df['QQQ Cumulative Returns'] = cumulative_returns['QQQ']





























