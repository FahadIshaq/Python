import os


fname = 'infile.txt' 
fname2 = 'outfile.txt'


path = os.path.abspath(fname) 
path2 = os.path.abspath(fname2)

print('Copying', path, 'to', path2)

blocksize = 16

totalsize = 0

data = bytearray(blocksize)

with open(fname, 'rb') as file, open(fname2, 'wb') as file2:
    while True:
        num = file.readinto(data)

        totalsize += num

        print(num, data)

        if num == blocksize:
            file2.write(data)
        else:
            data2 = data[0:num]
            file2.write(data2)
            break

print('Read', totalsize, 'bytes')
