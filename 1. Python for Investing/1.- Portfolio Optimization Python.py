# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=9GA2WlYFeBU&list=PLPe-_ytPHqyg4ap7hysD4pOBJMz0mnLly&index=2
"""
Como encontrar dentro de mi cartera con diferentes contratos: valores, bonos etc.
la cartera optima, que maximice mi beneficio y minimice el riesgo.

Para eso usaremos un enfoque que se llama Sharpe Ratio; la metrica de rendimiento 
de cartera más popular
"""

# ---------------------------- IMPORTS ---------------------------- 
import yfinance as yf
import pandas as pd
from pandas_datareader import data as pdr
import datetime as dt
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.optimize import minimize

# ---------------------------- DEFINIR TICKERS Y TEMPORALIDAD  ---------------------------- 

tickers = ['SPY', 'BND', 'GLD', 'QQQ', 'VTI']

# definicion temporalidad de datos
anios_datos = 2
fin  = dt.datetime.now()
inicio = fin - dt.timedelta(365*anios_datos)

# creamos dataframe con los precios ajustados y descargar datos
adj_close_df = pd.DataFrame()

for ticker in tickers:
    data = yf.download(ticker, start= inicio, end= fin)
    adj_close_df[ticker] = data['Adj Close']
    
    # adj_close_df['Log Return '+ticker] = np.log(adj_close_df[ticker]/adj_close_df[ticker].shift(1))
    # adj_close_df['Log Return '+ticker].dropna(inplace=True)

# calcular los beneficios logaritmicos y borrar columnas vacias
log_returns = np.log(adj_close_df/adj_close_df.shift(1))
log_returns = log_returns.dropna()

"""
    Matriz de covarianza: La matriz de covarianza permite entender cómo 
    variables diferentes se relacionan entre sí, siendo esencial para 
    analizar patrones y relaciones en los datos.

    Si la covarianza entre dos variables es positiva, significa que 
    cuando una variable aumenta, es probable que la otra también 
    aumente. Por otro lado, si la covarianza es negativa, indica que 
    cuando una variable aumenta, es probable que la otra disminuya. 
    En resumen, la covarianza positiva sugiere una relación directa 
    entre las variables, mientras que la covarianza negativa sugiere 
    una relación inversa.

"""

cov_matrix = log_returns.cov()*252 # multiplico por 252 para anualizar la covarianza

# ---------------------------- PORTFOLIO PERFOMANCE METRICS  ---------------------------- 

def standard_deviation(weights, cov_matrix):
    variance = weights.T @ cov_matrix @weights



























