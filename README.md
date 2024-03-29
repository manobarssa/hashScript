# hashScript
<p>A command line Python script to hash strings and files.</p>
<p>usage: python.exe hashscript.py [-h] -a Algorithm [-o Out File]
                     [-f File | -s String | -fL File List | -sL String List]</p>
<p>Hash a file, a list of files, a string or list of strings.</p>

<p>optional arguments:</p>
<p>-h, --help       show this help message and exit</p>
<p>-a <b>Algorithm</b>     sha224, sha384, sha3_224, sha3_256, shake_128, shake_256,
                   sha1, sha3_512, md5, sha256, sha512, blake2s, blake2b,
                   sha3_384. Two or more separated by comas (ex sha1,sha256).
                   Or all.</p>
<p>-o <b>Out File</b>      File path to write the hashes.</p>
<p>-f <b>File</b>          Path to file or * to all under current Work Directory.</p>
<p>-s <b>String</b>        String to hash.</p>
<p>-fL <b>File List</b>    Path to text file with files (paths) to hash. -o
                   flag and a filepath to write results are required.</p>
<p>-sL <b>String List</b>  Path to text file with strings (lines) to hash. -o
                   flag and a filepath to write results are required.</p>
