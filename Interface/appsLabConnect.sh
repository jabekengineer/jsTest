#!/bin/sh


# ssh IFOS@192.168.125.210 "cd ~/jswip/IFOS-WIP/AUTO/;./connection0.sh" 

ssh IFOS@192.168.125.210 "/usr/bin/timeout 10s curl -N http://192.168.125.210:8081/chans/resample/1.00/csv" 
