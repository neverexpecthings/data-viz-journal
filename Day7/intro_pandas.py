import numpy as np
import pandas as pd 
import numpy as np
# from pandas import Series, DataFrame

obj = pd.Series([4, 7, -5, 3])

obj2 = pd.Series([4, 7, -5, 3], index=["d", "b", "a", "c"])

np.exp(obj2)

sdata = {'Ohio': 35000,'Texas': 71000,'Oregon': 16000,'Utah': 5000,}

obj3 = pd.Series(sdata)

obj3.to_dict()

states = ['California', 'Ohio', 'Oregon', 'Texas', ]

obj4 = pd.Series(sdata, index=states)

data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2001, 2002, 2003],
        "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}

frame = pd.DataFrame(data)
frame.head()
frame.tail()

frame2 = pd.DataFrame(data, columns=["year", "state", "pop", "debt"])
frame2

frame2.loc[1]
frame2.iloc[2]

frame2["debt"] = np.arange(6.)

frame2["debt"]

val = pd.Series([-1.2, -1.5, -1.7], index=["two", "four", "five"])

frame2["debt"] = val

frame2["eastern"] = frame2["state"] == "Ohio"

del frame2["eastern"]

populations = {"Ohio": {2000: 1.5, 2001: 1.7, 2002: 3.6,},
               "Nevada": {2001: 2.4, 2002: 2.9}}

frame3 = pd.DataFrame(populations)
frame3
frame3.T

