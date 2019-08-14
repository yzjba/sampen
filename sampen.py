# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 15:46:08 2019

@author: yzj
"""

import numpy as np
import math

def sampen(sig,ordr,tor):
    # sig: the input signal or series, it should be numpy array with type float
    # ordr: order, the length of template
    # tor: percent of standard deviation
    
    n = len(sig)
    tor = np.std(sig)*tor
    
    matchnum = 0.0
    for i in range(n-ordr):
        tmpl = sig[i:i+ordr]
        for j in range (i+1,n-ordr+1):
            ltmp = sig[j:j+ordr]
            diff = tmpl-ltmp
            if all(diff<tor):
                matchnum+=1
    
    allnum = (n-ordr+1)*(n-ordr)/2
    if matchnum<0.1:
        sen = 1000.0
    else:
        sen = -math.log(matchnum/allnum)
    return sen

if __name__=="__main__":
    sig = np.random.random(100)
    sen = sampen(sig,10,0.01)
    print(sen)
