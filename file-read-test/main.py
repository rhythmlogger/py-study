import sys
print("Output #139: " );
input_file = sys.argv[1]
filereader = open(input_file,'r')
for row in filereader:
    print(row.strip())
filereader.close()