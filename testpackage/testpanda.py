import pandas as pd
import numpy as np
def returnlist():
    return ["a", "b"]

if __name__ == '__main__':
    a = {"a": 1, "b": 2}
    b = {"a": 2, "b": 3}
    c = {"a": 3, "b": 4}
    d = {"a": 4, "b": 5}
    a1 = []
    a1.append(a)
    a1.append(b)
    a2 = []
    a2.append(c)
    a2.append(d)
    a3 = []
    a3.append(a1)
    a3.append(a2)
    print(pd.DataFrame.from_dict(a2))
    pa = pd.DataFrame.from_dict(a2)
    print(list(pa["a"].values))
    returna, returnb = returnlist()
    print(returna)
    print(returnb)
    #--------------------------------
    print(np.zeros(3, dtype="float32"))