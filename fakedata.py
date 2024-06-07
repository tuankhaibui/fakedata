#!/opt/homebrew/bin/python3.11
from fileinput import nextfile
import numpy as np 
import argparse
import time 
import datetime
import os 

parser = argparse.ArgumentParser(description='constantly generate random numbers, under one distribution. The data are stored in to text files with filename based on timestamp.')
parser.add_argument('-f', '--freq',
                    required=True,
                    type=int,
                    help='frequency to generate the random number in unit of seconds. it can be input with float.' )
parser.add_argument('-d', '--distribution',
                    default='uniform',
                    type=str,
                    help='type of distribution to generate random number. it should be one of: uniform, normal, binominal, poisson, exponential, beta, gamma' )
parser.add_argument('-s', '--silent',
                    action='store_true',
                    help='keep silent and no print out the random numbers.')
parser.add_argument('-b', '--file-break',
                    required=False,
                    type=int,
                    default=60,
                    help='New files will be created after n seconds. it should be an integer' )


args = parser.parse_args()

freq = args.freq 
distribution = args.distribution

def init_filename():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime('%Y%m%d_%H%M%S')
    _filename_ = f'fakedata_{formatted_time}.txt'
    print(f'{_filename_} will be opened for new data storage')
    return _filename_

filename = init_filename()

# def file_init():
#     current_time = datetime.datetime.now()
#     formatted_time = current_time.strftime('%Y%m%d_%H%M%S')
#     filename = f'fakedata_{formatted_time}.txt'
#     file.open(filename, 'w')
#     file.close()
#     print(f'{filename} is opened for new data storage')
#     return filename

while True: 
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

    current_time = datetime.datetime.now()
    if current_time.second % args.file_break == 0:
        filename = init_filename()
    
    if not os.path.isfile(filename):
        file = open(filename, 'w')
    else:
        file = open(filename, 'a')
    # filename = file.name
    # file = open(filename,'a')
    
    file.write(str(rdm_number)+'\n')
    if args.silent==False:
        print(rdm_number)
    file.close()
    time.sleep(freq)
