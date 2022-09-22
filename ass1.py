'''
First assignment CMEPDA
'''
from typing import List, Dict, Tuple, Optional
from matplotlib import pyplot as plt
import argparse

NUM_LETT=26
CHAR_A=97 #ASCII lowecase a

def read_file(file_path:str)-> List[str]:
    """Opens and reads the file, returns a lower case string
    """
    print(f'Opening input file {file_path}...')
    with open(file_path, 'r') as input_file:
        text = input_file.read().lower()
    return text

def count(text:str, lett:str)-> int:
    return text.count(lett)

def create_set(text:str)-> Dict[str, int]:
    set={}
    for i in range(CHAR_A, CHAR_A+NUM_LETT):
        set[chr(i)]=count(text, chr(i))
    return set

def graph(set:Dict[str, int]):
    print(set)
    plt.bar(list(set.keys()), set.values(), color='g')
    plt.show()



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print some book statistics')
    parser.add_argument('--infile', type=str, help='path to the input file', default="siddhartha.txt")
    parser.add_argument("--verbose", type=int, choices=[0, 1], default=1)
    args = parser.parse_args()
    text = read_file(args.infile)
    if bool(args.verbose):
        graph(create_set(text))
        #set={'a':0.5, 'b':0.6,'c':1}
        #graph(set)

