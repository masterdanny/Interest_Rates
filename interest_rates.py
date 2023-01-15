# TODO: Next step is to use machine learning to predict future rates.

import os
import pandas as pd
import matplotlib.pyplot as plt 

filepath = "/Users/daniele/Downloads"
filename = "DP_LIVE_15012023073235274.csv" 
df = pd.read_csv(os.path.join(filepath, filename))

ger = df[df.LOCATION=="DEU"]
aut = df[df.LOCATION=="AUT"]
it = df[df.LOCATION=="ITA"]
us = df[df.LOCATION=="USA"]
jpn = df[df.LOCATION=="JPN"]

plt.plot(ger.TIME, ger.Value, label="GER")
plt.plot(aut.TIME, aut.Value, label="AUT")
plt.plot(it.TIME, it.Value, label="ITA")
plt.plot(us.TIME, us.Value, label="USA")
plt.plot(jpn.TIME, jpn.Value, label="JPN")
plt.xlabel("Quarter")
plt.ylabel("Interest Rate [%]")
plt.title(f"Interest rates Comparison ({min(ger.TIME)}, {max(ger.TIME)})")
plt.legend()
plt.xticks(ger.TIME[::3], rotation=45)
plt.show()
