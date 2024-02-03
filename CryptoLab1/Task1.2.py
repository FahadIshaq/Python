import os

fname = 'infile.txt'
fname2 = 'outfile1.txt'

path = os.path.abspath(fname)
path2 = os.path.abspath(fname2)

print('Copying', path, 'to', path2)

blocksize = 16
totalsize = 0

with open(fname, 'r') as file, open(fname2, 'w') as file2:
    while True:
        text_block = file.read(blocksize)

        totalsize += len(text_block)

        file2.write(text_block)

        if len(text_block) < blocksize:
            break

print('Read and copied', totalsize, 'characters')
