import os
import hp33120aLib as tb

def spill():
    for name, val in tb.__dict__.items():
        if callable(val):

            print(val.__doc__)
    pass