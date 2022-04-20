
import pandas as pd
from gpibRun import cmdCheck

def oneByOne(profile, func):
    cmds = []
    steps = profile.loc[:,"Steps"].values
    for step in steps:
        argSub = "%f, HZ, 2, VPP, 0, V" % (step)
        argSub = str.split(argSub, ",")
        cmdSub = cmdCheck(func, argSub)[3]
        cmds.append(cmdSub)
    profile['Commands'] = cmds

    return profile
