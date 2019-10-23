# -*- coding: utf-8 -*-
"""
version 0.1

@author: @manobarssa
"""
#!python3

import argparse, hashlib

def stringHasher(txt,algo):
    if algo.lower() == 'shake_256':
        return getattr(hashlib, algo.lower())(txt.encode()).hexdigest(256)
    elif algo.lower() == 'shake_128':
        return getattr(hashlib, algo.lower())(txt.encode()).hexdigest(128)    
    else:
        return getattr(hashlib, algo.lower())(txt.encode()).hexdigest()


def main():
    algs = ', '.join(hashlib.algorithms_guaranteed) + '. Or all.'
    parser = argparse.ArgumentParser(description= ''' 
    Calculate the hash for a file, a list of files, a string or list of strings.
                                                                           ''')
    parser.add_argument('-a', dest='alg', metavar='Algorithm', type=str, 
                        help=algs, required=True)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('-f', dest='files', metavar='File(s)', 
                      help='Path to file or * to all under current Work Directory.',)
    mode.add_argument('-s', dest='string', metavar='String', 
                      help='String to hash.')
    args = parser.parse_args()
    
    if args.string is not None and args.alg.lower() != 'all':
        alg = args.alg.lower()
        string = args.string
        print('{}: {}'.format(alg, stringHasher(string, alg)))
    elif args.string is not None and args.alg == 'all':
        string = args.string
        for a in hashlib.algorithms_guaranteed:            
            print('{}: {}'.format(a, stringHasher(string, a)))
        
        

if __name__ == '__main__':
    main()


    

    
