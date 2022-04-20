import gpibLib
import hp33120aLib as tb
import libDoc
import cmdParse
import time
import gpibRun
import instrProfiles as prof
import unpackDF as load
import datetime


import os

testDir = r"C:\Users\js\linux\jsAuto\gpibLibrary"
fileRootName = "sineSweep_"
inp = "sine 2 HZ 2 VPP 0 V"
units = "HZ"
profile = prof.monotonicRamp('1 HZ', '1000 HZ', '100 HZ', '5 HZ') #must properly designate needed values


dev = gpibLib.connection() #dev is device
func, args = cmdParse.cmdHandling(inp)
procedure = load.oneByOne(profile, func)

timing = procedure.loc[:, "Time"]
commands = procedure.loc[:, "Commands"]
timeStamps = []
startTime = datetime.datetime.now().time()

print("started test at ", startTime, os.linesep) 
j = 0
for cmd in commands:
    try:
        time.sleep(timing[j+1]  - timing[j])
    except:
        time.sleep(timing[j] - timing[j-1])
    gpibRun.run2(dev, cmd)
    timeStamp = datetime.datetime.now()
    timeStamp = tb.excel_date(timeStamp)
    timeStamps.append(timeStamp)
    j+=1

reportCSV, reportXL = tb.testReport(commands, timing, timeStamps, testDir, fileRootName)
os.startfile(reportXL)
time.sleep(100)