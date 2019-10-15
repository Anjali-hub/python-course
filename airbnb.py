import sys
file_name = 'airbnb/complete.csv'
f = open(file_name)
lines = f.readlines()
for line in lines[1:]:
    or line in lines[1:]:
    columns = line.split(',')
    clean_columns = [] 
    in_quote = False  
    for x in columns: 
        clean_x = x.replace('""', '') 
        n_quotes = clean_x.count('"')
            if not in_quote:
            clean_columns += [ clean_x ] 
            if n_quotes % 2 != 0:  
                in_quote = True
                for x in columns: 
        clean_x = x.replace(' : ', '') 
        n_quotes = clean_x.count('"')
            if not in_quote:
            clean_columns += [ clean_x ] 
            if n_quotes % 2 != 0:  
                in_quote = True
        else:
            clean_columns[-1] += clean_x  
            if n_quotes % 2 != 0:  
                in_quote = False