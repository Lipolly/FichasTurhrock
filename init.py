import pickle
import os
from GrimorioDeTurhrock import grimorioTotal

flag_path = os.path.join("bin", "flag.pickle")

def initGrimorio():
    try:
        with open(flag_path, "rb") as f:
            flag = pickle.load(f)
    except FileNotFoundError:
        flag = False

    if not flag:
        grimorioTotal()
        flag = True
        with open(flag_path, "wb") as f:
            pickle.dump(flag, f)