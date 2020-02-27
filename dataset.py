import pandas as pd
import numpy as np
import math

import tensorflow


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, InputLayer

# d = pd.read_csv("aguah_row_small.csv")
c=0
d = pd.read_csv("aguah_row.csv")

X = []
y = []

data2 = np.array(d)

# features=d[0:-1][:]
# classes=d[-1:][:]
# features=d['USO2013':'Year']
# classes=d['Consumption']

# print('features',features)
# print('classes',classes)


USO2013 =["AVD", "CU", "EQ", "H1", "H2", "H3", "IN", "IRA", "IRB", "IRM", "MX", "RG", "RHC", "RIC"] #  ['H3', 'IRM', 'MX', 'H2', 'AVD', 'RG', 'EQ']
TU = ['DOMESTICO MEDIO', 'DOMESTICO RESIDENCIAL', 'SOCIAL', 'COMERCIAL', 'INDUSTRIAL', 'DOMESTICO BAJA', 'ESPECIAL']
# M = ['MSDELAUNET', 'CICASA MMD-15 S', 'BADGERMETER', 'Cicasa NG 1/2', 'AZTECA', 'CICASA / DE LA UNET', 'ACTARIS',
#      'Otras / desconocida', 'SHLUMBERGER', 'ELSTER', 'Delaunet MD-100', 'SENSUS', 'ADCOM', 'DOROT', 'KENT',
#      'TONHY']

M = ["ABB", "ACTARIS", "ADCOM", "ALFA", "AQUARIUS", "ARAD", "AV3STARS", "AZTECA", "Azteca 3VM", "BADGERMETER", "BAR-METERS 1\"", "Badger M25 Bronce", "Badger RCDLL-25", "Badger combinado", "CICASA / DE LA UNET", "CICASA MMD-15 S", "Cicasa NG 1/2", "Cicasa NG 3/4", "DOROT", "Delaunet Aurus 3UM-15", "Delaunet MD-100", "Delaunet MD-15", "Delaunet MD-19", "Delaunet MD-40", "Delaunet MD-50", "Delaunet MMD-19", "Delaunet UD-15", "Delaunet WD-100", "ELSTER", "ENDRESS-HOUSER", "EWE", "GENERICA", "IESA", "INVENSYS", "INVERCONTA", "Iberconta", "KENT", "Kent ABB", "MASTER", "MENECKE", "MEXICANO", "MSDELAUNET", "NEPTUNE", "Otras / desconocida", "PRECISA II", "RECORDAL", "SAPPEL AQUARIUS", "SAPPEL", "SENSUS", "SHLUMBERGER", "TONHY", "Y-T MD-15", "ZENNER 1/2"]

# categories = [
#     [1, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 1, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 1, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 1, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 1]
# ]

cat_ranges = [10, 20, 30, 40, 50, 60, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000,
              6500, 7000, 200000]
num_cats = len(cat_ranges)
categories = []

for i in range(num_cats):
    arr = [0] * num_cats
    arr[i] = 1
    categories.append(arr)

for i in range(len(categories)):
    print(categories[i])

count=0

for d in data2:
    count += 1
    if count>100000:

        break
    if(d[7]>10000):
        data2.remove(d)
        c=c+1
    # if (d[0] in USO2013):
    d[0] = USO2013.index(d[0])
    # for d in data2:
    # if (d[1] in TU):
    d[1] = TU.index(d[1])
    # for d in data2:
    # if (d[3] in M):
    d[3] = M.index(d[3])
    # print(data2[0])

    X.append(d[0:-1])
    c = d[-1]

    for i in range(num_cats):
        # print('c',c)
        if c <= cat_ranges[i]:
            c = categories[i]
            break
    y.append(np.array(c))


# print('features', X)
# print('classes', y)
print(c)
model = Sequential()
model.add(InputLayer(input_shape=(len(X[0]))))
model.add(Dense(128, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(num_cats, activation='softmax'))

# model.compile(loss='mean_squared_error', optimizer='sgd', metrics=['accuracy'])
optimizer=tensorflow.keras.optimizers.Adam(learning_rate=.0001) #, decay= 0.001)
model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])


X = np.array(X, dtype=float)
y2 = np.array(y, dtype=float)

print(X.shape)
print(y2.shape)


model.fit(X, y2, epochs=10000, validation_split=.05, shuffle=True, batch_size=65536, validation_freq=10)
