import numpy_financial as npf
import numpy as np
import matplotlib.pyplot as plt
from fontTools.misc.cython import returns

rate = 0.05
years = 5
pv = 120000
interest_rate = 0.12
freq = 12

rate /= freq
nper = freq * years
periods = np.arange(1, nper + 1, dtype=int)

# cena mieszkania za  5 lat
f_price = np.around(npf.fv(rate, periods, nper, -pv), decimals=2)
# print(f_price)
print("Wartość mieszkania za 5 lat wyniesie: " + str("{:.2f}".format(f_price.sum())))
#

#
print('---')
deposit = np.around(npf.pmt(interest_rate/12, nper, periods, -f_price), decimals=2)
rata = (deposit.sum()/60)
print("Miesięcznie należy wpłacać do banku: " + str("{:.2f}".format(rata)))

# wykres danych
plt.plot(f_price.cumsum(),label='cena mieszkania')
plt.plot(deposit.cumsum(),label='wartość lokaty')
plt.legend(loc='upper left')
plt.xlabel('Liczba okresów')
plt.ylabel('Skumulowana wartość odsetek')
plt.show()











