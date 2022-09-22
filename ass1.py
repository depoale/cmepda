# Copyright (C) 2022 Alessia De Ponti
#
# For the license terms see the file LICENSE, distributed along with this
# software.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

'''
First assignment CMEPDA
'''
import argparse
from typing import List, Dict
from matplotlib import pyplot as plt


NUM_LETT=26
CHAR_A=97 #ASCII lowecase a

def read_file(file_path:str)-> List[str]:
    '''
    Opens and reads the file, returns a lower case string
    '''
    print(f'Opening input file {file_path}...')
    with open(file_path, 'r') as input_file:
        text = input_file.read().lower()
    return text

def count(text:str, lett:str)-> int:
    '''
    Counts how many times a letter appears
    '''
    return text.count(lett)

def create_set(text:str)-> Dict[str, int]:
    '''
    Creates a dictionary with the letters as keys and their frequency as values
    '''
    set={}
    for i in range(CHAR_A, CHAR_A+NUM_LETT):
        set[chr(i)]=count(text, chr(i))
    return set

def graph(set:Dict[str, int]):
    '''
    Histogram
    '''
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


