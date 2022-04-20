from matplotlib.cbook import report_memory
import pyvisa
import os
import time
from datetime import datetime, timedelta
import uuid
import pandas as pd
def sine(frequency, amplitude, offset):
    """
    Sine Function
        Syntax: sine frequency amplitude offset
        Description: Command Sine Wave with: 
                        -- Freq 'HZ, KHZ' 
                        -- Amplitude 'VPP'
                        -- Offset  'V'. 
        Returns:
            string: formatted command string for 33120A device.
    """
    cmd = "APPLy:SINusoid " + str(frequency) + ", " + str(amplitude)\
            + ", " + str(offset)
    
    return cmd

def errQry():
    """
    Error Query
        Syntax: errQry
        Description: Check status of gpib error line.
        Returns:
            string: formatted command string for 33120A device. 
    """
    cmd = "SYSTem:ERRor?"
    return cmd

def testReport(cmdArr, timing, timeStamps, testDir, fileRootName):
    freq = []
    amplitude = []
    offset = []
    timestamps = []
    j=0
    for cmd in cmdArr:
        params = str.split(cmd, "APPLy:SINusoid ")[1]
        params = list(filter(None,str.split(params, " ")))
        freq.append(params[0])
        amplitude.append(params[2])
        offset.append(params[4])
    data = list(zip(timing, timeStamps, freq, amplitude, offset))
    dDF = pd.DataFrame(data, columns=['Time Delta', 'TimeStamps', 'Frequency (HZ)', 'Amplitude (VPP)', 'Offset(V)'])
    
    pathCSV = testDir + fileRootName + str(uuid.uuid4()) + ".csv"
    pathXL = testDir + fileRootName + str(uuid.uuid4()) + ".xlsx"
    dDF.to_csv(pathCSV, index=True)
    dDF.to_excel(pathXL)
    return pathCSV, pathXL

def excel_date(date1):
    temp = datetime(1899, 12, 30)    # Note, not 31st Dec but 30th!
    delta = date1 - temp
    return float(delta.days) + (float(delta.seconds) / 86400)