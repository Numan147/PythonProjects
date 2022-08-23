#program to check file size via python.
import os.path
def size_convert(sz): #Convert bytes to KB, or MB or GB
    for i in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if sz < 1024.0:
            return "%3.1f %s" % (sz, i)
        sz /= 1024.0

def get_file_size(filepath): #
    size = os.path.getsize(filepath)
    print(f'The {filepath} size is', size, 'bytes')
    convert_size = size_convert(size)
    #print('actual file size is ', convert_size) // Programer Can print Directly without assigning a variable.
    return convert_size

file_size = get_file_size(r'C:\Users\admin\Desktop\NiravsTesting\mSociety Documentation v2 (1).pdf')
print('Actual file size is ', file_size)

