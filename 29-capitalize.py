import string

def cap(full_name):
    # cap_full_name = [str(i).capitalize() for i in full_name]
    # return ' '.join(cap_full_name)
    return string.capwords(full_name, ' ')


if __name__ == '__main__':
    '''
        sample input : hossein davoodi
    '''
    s = input('Please enter a name: ')
    result = cap(s)
    print(result)
