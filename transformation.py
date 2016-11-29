# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 14:28:41 2016

@author: vorreiterv
"""
import numpy as np
import pandas as pd 

col = ['temps','objet','valeur']
data = pd.read_csv('document.csv',names=col ,sep=';')
data['temps'] = pd.to_datetime(data['temps'])
data['valeur'] = data['valeur'].map(lambda x: x.lstrip('').rstrip('W').rstrip('°C').rstrip('Lux').rstrip(' '))
data['valeur'] = data['valeur'].replace(['on','off'],[0,1])
data['valeur'] = data['valeur'].replace('\.',',')

data['valeur'] = data['valeur'].astype(float)


test = data.groupby(['temps','objet'])['valeur'].sum()

colonne =['date','temp','lux','conso reelle', 'conso','conso_elec','prise']
df = pd.DataFrame(columns=colonne)
df['date']=data.groupby(['temps'])

toto = pd.pivot_table(data,index=["temps"],columns=['objet'],values=["valeur"], aggfunc=np.mean)
toto['time'] = toto.index


#print(type(toto.index))
#times = toto.to_datetime(toto.time)
#times = pd.DatetimeIndex(toto.time)
#toto2 = toto.groupby([times.hour]).mean()
#toto2 = toto.groupby('time').mean()
#print(toto2)