import pyvisa
import os
import time

def connection():
    """ 
    GPIB Connection Utility -- Single Device
        Syntax: gpib.connection()
        Returns:
        pvisa_instrument_object -- active gpib
        estring -- no gpib found string
    """
    rm = pyvisa.ResourceManager()
    devArr = rm.list_resources() #type tuple
    if len(devArr) > 0:
        for i in range(0,(len(devArr))):
            subStr = devArr[i]
            ind = 0
            splat = str.split(subStr, '::')
            for ssub in splat:
                if ssub.find("GPIB") != -1:
                    print("GPIB device found on Port # ", splat[ind+1], os.linesep)
                    # time.sleep(1)
                    # print("Connecting", os.linesep, ".......")
                    # time.sleep(.5)
                    # print(" .......")
                    # time.sleep(.5)
                    # print("Connected to: ")
                    my_instrument = rm.open_resource(devArr[i])
                    print(my_instrument.query('*IDN?'), os.linesep)
                ind +=1
    else:
        my_instrument = []
        print("No GPIB Devices Found")

    
    return my_instrument
