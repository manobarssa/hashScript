# hashScript
A command line Python script to hash strings and files.

usage: python.exe hashscript.py [-h] -a Algorithm [-o Out File]
                     [-f File | -s String | -fL File List | -sL String List]
Hash a file, a list of files, a string or list of strings.

optional arguments:
  -h, --help       show this help message and exit
  -a Algorithm     sha224, sha384, sha3_224, sha3_256, shake_128, shake_256,
                   sha1, sha3_512, md5, sha256, sha512, blake2s, blake2b,
                   sha3_384. Two or more separated by comas (ex sha1,sha256).
                   Or all.
  -o Out File      File path to write the hashes.
  -f File          Path to file or * to all under current Work Directory.
  -s String        String to hash.
  -fL File List    Path to text file with files (paths) to hash. -o
                   flag and a filepath to write results are required.
  -sL String List  Path to text file with strings (lines) to hash. -o
                   flag and a filepath to write results are required.
