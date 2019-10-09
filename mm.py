import sys
print(sys.argv)
file_name = sys.argv('airbnb/first_10.csv')
f = open(file_name)
lines = f.readlines()
for line in lines[1:]:
    columns = line.split(',')
    price = columns[9]
    print(price)