import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mtp

plt.close("all")
ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2024", periods=1000))
ts = ts.cumsum()

mtp.pyplot.show(ts.plot())

