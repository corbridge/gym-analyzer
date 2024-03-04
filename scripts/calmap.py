import numpy as np; np.random.seed(sum(map(ord, 'calmap')))
import pandas as pd
import calmap
import matplotlib.pyplot as plt

all_days = pd.date_range('1/15/2014', periods=700, freq='D')
days = np.random.choice(all_days, 500)
events = pd.Series(np.random.randn(len(days)), index=days)
print(events)
# print(np.random.randn(len(days)))

# ax = calmap.yearplot(events)
# plt.show()
# print(plt.pyplot(ax))