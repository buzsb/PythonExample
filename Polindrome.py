#Ask string and say is you strin a polindrome

def reversing_string(string):
    rv_string = string[::-1]
    return rv_string

def polindrome():
    string = raw_input("Type you string: ")
    if len(string) == 0:
        print "you dont type enything"
    else:
        if reversing_string(string) == string:
            print "sring is poindrome"
        else:
            print "string NOT a polindrome"
            
if __name__ == '__main__':
    polindrome()