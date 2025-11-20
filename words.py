def num_letters(num_rows,num_columns):
    return (num_rows*num_columns)-((num_rows-2)*(num_columns-2))
assert num_letters(3,4)==10
assert num_letters(13,4)==30
assert num_letters(4,4)==12
assert num_letters(6,4)==16
assert num_letters(6,7)==22
    
