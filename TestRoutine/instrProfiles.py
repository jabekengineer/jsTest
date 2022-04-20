
from turtle import st
from matplotlib.pyplot import step
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def monotonicRamp(start, end, stepSize = None , stepFreq = '1 HZ'):
    """ Monotonic Ramp Up or Down. *Must Specify Units and Units must match*

    Args:
        start string: '<start> <unit>'
        end string: '<end> <unit>'
        stepSize (str, optional): <stepSize> <unit> Defaults to 100th of total range.
        stepFreq (str, optional): <stepFreq> <unit> Defaults to '1 HZ'.
    """
    try: 
        startVal, unit = str.split(start, " ")[:] #debug
        startVal = int(startVal)
        endVal = int(str.split(end, " ")[0])
    except:
        print("Non integer value set for ramp endpoints! Default set to 0 - 100")
        startVal = 0
        endVal = 100

    if not stepSize: #(start - end) / 100
        stepSizeVal = abs(startVal - endVal)/100
        stepSize = str(stepSizeVal) + " " + unit
    else:
        try:
            stepSizeVal, ssUnit = str.split(stepSize, " ")[:] #debug
            stepSizeVal = int(stepSizeVal)
        except:
            print("Non integer value set for ramp stepSize! Set to Default")
            stepSizeVal = abs(startVal - endVal)/100
            ssUnit = unit
            stepSize = str(stepSizeVal) + " " + ssUnit
    
    if stepFreq == '1 HZ':
        stepFreqVal, unit = str.split(stepFreq)[:] #debug
        stepFreqVal = int(stepFreqVal)
    else:
        try:
            stepFreqVal, sfUnit = str.split(stepFreq)[:]
            stepFreqVal = int(stepFreqVal)
        except:
            print("Non integer value set for ramp stepFreq! Set to Default")
            stepFreqVal = 1
            sfUnit = 'HZ'

    stepNum = int(np.ceil(abs(endVal - startVal)/stepSizeVal))
    ramp = np.linspace(startVal, endVal, stepNum, True)

    timelist = np.linspace(0, stepNum / stepFreqVal, stepNum + 1)

    sigList = list(zip(timelist, ramp))
    sigDF = pd.DataFrame(sigList, columns = ['Time', 'Steps'])

    print("Ramping from {} to {} in {} steps at frequency of {}.".format(start, end, stepSize, stepFreq))


    return sigDF