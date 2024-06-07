import numpy as np 
import argparse
import time 

parser = argparse.ArgumentParser(description='constantly generate fake data, under one distribution')
parser.add_argument('-f', '--freq',
                    required=True,
                    type=int,
                    help='frequency to generate the random number in unit of seconds. it should be an interger.' )
parser.add_argument('-d', '--distribution',
                    # required=True,
                    default='uniform',
                    type=str,
                    help='type of distribution to generate random number. it should be one of: uniform, normal, binominal, poisson, exponential, beta, gamma' )

args = parser.parse_args()

freq = args.freq 
distribution = args.distribution

file = open('fakedata.txt','w')
file.close()

while True: 
    file = open('fakedata.txt','a')
    if distribution=='uniform':
        rdm_number = np.random.uniform(0,1)
    elif distribution=='normal':
        rdm_number = np.random.normal(0,1)
    elif distribution=='binominal':
        rdm_number = np.random.binomial(10,0.5)
    elif distribution=='poisson':
        rdm_number = np.random.poisson(5)
    elif distribution=='exponential':
        rdm_number = np.random.exponential(1)
    elif distribution=='beta':
        rdm_number = np.random.beta(1,1)
    elif distribution=='gamma':
        rdm_number = np.random.gamma(1,1)
    
    file.write(str(rdm_number)+'\n')
    print(rdm_number)
    file.close()
    time.sleep(freq)
