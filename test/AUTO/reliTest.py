#!/usr/local/bin/python3.9
from lib2to3.pgen2.pgen import DFAState
import subprocess
import argparse
import glob
import os
import pandas as pd
import numpy as np

parser=argparse.ArgumentParser(description="Run Automated GPIB - D*Sense Reliability Test.")
parser.add_argument('-p',
                    metavar="PROC",
                    type=str, 
                    help="Test Procedure")


args = parser.parse_args()


def connection():
    """connect to DSense via Apps Lab Host 
    calls appsLabConnect Shell Script in Same Directory

    Returns:
        tuple: stdout from shell script 
    """
    #path to DSense connection shell script
    cmd = ["./appsLabConnect.sh"] 
    #open shell and set shell to True to commands maay be daisy chained
    tmp = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    #capture stdout, stderr tuple
    output = tmp.communicate()
    return output

def trialNum(dataPath):
    """Identify trial number and generate distinct, ordered name for log file

    Args:
        dataPath (string): path to folder containing current test data

    Returns:
        fn: absolute path to new log file 
    """
    list_of_files = glob.glob(dataPath + '*.csv')
    latest_file = max(list_of_files, key=os.path.getctime)
    substr = (latest_file.rsplit('/', 1)[1]).rsplit('.csv', 1)[0]
    num = int(substr.rsplit("_", 1)[1]) + 1
    fn = dataPath + "log_" + str(num) + ".csv"
    return fn

def DsenseDataserverChans(stream):
    """formats DSense local host curl byte stream 
    
    Args:
        stream (tuple): byte list at index 0   

    Returns:
        pd.Dataframe: formatted 
    python pixel values as columns and samples as rows
    """
    #decode and split values from pipe tuple
    stream = stream[0].decode()
    streamNL = stream.split('\n')
    
    #capture data in list
    streamList = []
    columns = []
    packetsize = 511
    #make dataframe column list
    for i in range(0,packetsize):
        columns.append("Pixel {}".format(i))
    
    #clip incomplete packets (not 511)
    for sample in streamNL:
        streamPXL = sample.split(',')
        #make matching columns and pack in
        if np.size(streamPXL) == packetsize:
            streamList.append(streamPXL)
    df = pd.DataFrame.from_records(streamList, columns=columns)
    return df

# TODO: correct WL peak reading or abandon approach and convert chans
def DsenseWLPeaks(stream):

    print(os.linesep, stream)
    print(os.linesep, stream[0].decode())
    print(stream)
    df = []
    return df

def main():
    #data out from DSense
    stream = connection()
    streamDF = DsenseDataserverChans(stream)
    # streamDF = DsenseWLPeaks(stream)

    
    #Save DSense Data to new log file
    dataPath = "./log/"
    fn = trialNum(dataPath)
    streamDF.to_csv(fn)
    return

if __name__ == "__main__":
    main()


