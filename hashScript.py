# -*- coding: utf-8 -*-
"""
version 0.2

@author: @manobarssa
"""
#!python3

import argparse, hashlib, os

def stringHasher(txt,algo):
    if algo.lower() == 'shake_256':
        return getattr(hashlib, algo.lower())(txt.encode()).hexdigest(256)
    elif algo.lower() == 'shake_128':
        return getattr(hashlib, algo.lower())(txt.encode()).hexdigest(128)    
    else:
        return getattr(hashlib, algo.lower())(txt.encode()).hexdigest()

def fileHasher(path, algo):       
    block = 52428800 
    file_hash = getattr(hashlib, algo.lower())()
    with open(path, 'rb') as f: 
        fb = f.read(block) 
        while len(fb) > 0: 
            file_hash.update(fb) 
            fb = f.read(block) 
    
    if algo.lower() == 'shake_256':
        return file_hash.hexdigest(256)
    elif algo.lower() == 'shake_128':
        return file_hash.hexdigest(128)    
    else:
        return file_hash.hexdigest()  
    
def main():
    algs = ', '.join(hashlib.algorithms_guaranteed) + '''. Two or more separated
    by comas (ex sha1,sha256). Or all.'''
    parser = argparse.ArgumentParser(description= ''' 
    Calculate the hash for a file, a list of files, a string or list of strings.
                                                                           ''')
    parser.add_argument('-a', dest='alg', metavar='Algorithm', type=str, 
                        help=algs, required=True)
    parser.add_argument('-o', dest='outfile', metavar='Out File',
                        help='File path to write the hashes.')
    
    #add a muttyally exclusive group
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('-f', dest='file', metavar='File', 
                      help='Path to file or * to all under current Work Directory.',)
    mode.add_argument('-s', dest='string', metavar='String', 
                      help='String to hash.')
    mode.add_argument('-fL', dest='fileList', metavar='File List', 
                      help='''Path to text file with files (paths) to hash.
                      Required -o flag and a filepath to write results.''')
    mode.add_argument('-sL', dest='stringList', metavar='String List', 
                      help='''Path to text file with strings (lines) to hash.
                      Required -o flag and a filepath to write results.''')
        
    args = parser.parse_args()
    if args.alg.lower() == 'all':
        algList = list(hashlib.algorithms_guaranteed)
        algList.sort()
    else:
        algList = args.alg.lower().split(',')
        algList.sort()
    #Hash string
    if args.string is not None and args.outfile is not None:     
        string = args.string
        with open(args.outfile,'w') as f:
            for alg in algList:
                f.write('{}:{}:{}'.format(string, alg, stringHasher(string, alg))+'\n')
        
    elif args.string is not None and args.outfile is None:
        string = args.string        
        for alg in algList:            
            print('{}:{}:{}'.format(string, alg, stringHasher(string, alg)))
    
    #Hash a list of strings from a file
    if args.stringList is not None:
        with open(args.stringList) as fr:
            stringList = fr.readlines()
        
        with open(args.outfile, 'w') as fw:
            for string in stringList:
                for alg in algList:
                    fw.write('{}:{}:{}'.format(string.replace('\n',''), alg, stringHasher(string, alg))+'\n')
    
    #Hash files
    if args.file == '*':
        fileList = [x for x in os.listdir() if os.path.isfile(x)]
    elif args.file is not None:
        fileList = [args.file]
    
    if args.outfile is not None:        
        with open(args.outfile, 'w') as f:
            for alg in algList:
                for file in fileList:
                    try:
                        f.write('{}:{}:{}'.format(file, alg, fileHasher(file, alg))+'\n')
                    except:
                        pass #to do ----> print error msgs to file
    else:         
        for alg in algList:
            for file in fileList:
                try:
                    print('{}:{}:{}'.format(file, alg, fileHasher(file, alg)))
                except:
                    pass #to do ----> print error msgs to file
    
    
if __name__ == '__main__':
    main()


    

    
