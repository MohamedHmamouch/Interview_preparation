def remove_null(input_string):
    substrings = input_string.split(',')
    substrings = [substring for substring in substrings if substring.strip().lower() != 'null']
    return ','.join(substrings)


if __name__=='__main__':

    s="2076,3B,19C,138D,NULL,Null"
    print(remove_null(s))


    
