'''
First assignment CMEPDA
'''
import argparse

def process(file,path):
    '''

    '''
    print(f'Opening input file()')


if __name__== '__main__':
    parser = argparse.ArgumentParser(description='Print some books statistics.')
    parser.add_argument('infile', type=str, )

    args = parser.parse_args()
    print(args.accumulate(args.integers))