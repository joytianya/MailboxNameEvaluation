import pandas as pd
import numpy as np


def getBin(var, n=10):
    k = 100 / n
    p = []
    for i in range(n):
        p.append(i * k / 100.0)
    p.append(1.0)
    return p


def info_val(label, var, n=10):
    uv = var.unique()
    # return pct
    # print pct
    label = pd.Series(label)
    tab = label.value_counts()

    good_tot = tab[0] + 0.0

    bad_tot = tab[1] + 0.0
    # print good_tot, bad_tot
    ll = len(uv)
    if (ll < 4):
        iv = np.array([0.0] * ll)
        for i in range(ll):
            g = sum((var == uv[i]) & (label == 0))
            g = g / good_tot
            b = sum((var == uv[i]) & (label == 1))
            b = b / bad_tot
            if ((g == 0) | (b == 0)):
                iv[i] = 0.0
            else:
                iv[i] = (g - b) * np.log(g / b)
    else:
        p = getBin(var=var, n=n)
        pct = list(var.quantile(p).unique())
        l = len(pct)

        iv = np.array([0.0] * (l - 1))
        for i in range(l - 2):
            # print 1
            # print pct[i], pct[i + 1]
            g = sum((var >= pct[i]) & (var < pct[i + 1]) & (label == 0))
            # print g
            g = g / good_tot
            # good[i] = g

            b = sum((var >= pct[i]) & (var < pct[i + 1]) & (label == 1))
            # print b
            b = b / bad_tot
            # bad[i] = b
            if ((g == 0) | (b == 0)):
                iv[i] = 0.0
            else:
                iv[i] = (g - b) * np.log(g / b)

        i = l - 2
        # print 2
        # print pct[i], pct[i + 1]
        g = sum((var >= pct[i]) & (var <= pct[i + 1]) & (label == 0))
        # good[i] = g
        # print g
        g = g / good_tot
        b = sum((var >= pct[i]) & (var <= pct[i + 1]) & (label == 1))
        # bad[i] = b
        # print b
        b = b / bad_tot
        if ((g == 0) | (b == 0)):
            iv[i] = 0.0
        else:
            # print g-b
            iv[i] = (g - b) * np.log(g / b)

    return sum(iv)
