from itertools import accumulate

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
f_price = np.around(npf.fv(rate, nper, 0, -pv), decimals=2)
print("Wartość mieszkania za 5 lat wyniesie: " + str("{:.2f}".format(f_price.sum())))

fv_list = []
for i in range(1, nper+1):
    fv = (npf.fv(rate, i, 0, pv )) * -1
    fv_list.append(fv)

fv_list_np = np.array(fv_list)
fv_list_np.sum()

print('---')
# miesięczna rata
pmt = np.around(npf.pmt(interest_rate/12, nper, 0,-max(fv_list), 1), decimals=2)

# wartość lokaty z procentem składanym dla każdego miesiąca
deposite_value = []
accumulated = 0
for i in range(1, nper+1):
    accumulated = accumulated * (1 + interest_rate/12) + pmt
    deposite_value.append(accumulated)

    deposite = np.array(deposite_value)
    rata = pmt
    print("Miesięcznie należy wpłacać do banku: " + str("{:.2f}".format(rata)))


# wykres danych
plt.plot(fv_list_np,label='cena mieszkania')
plt.plot(deposite_value,label='wartość lokaty')
plt.legend(loc='upper left')
plt.xlabel('Liczba okresów')
plt.ylabel('wartość w zł')
plt.show()











