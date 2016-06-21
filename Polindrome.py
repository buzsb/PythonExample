#Ask string and tey is you strin a  polindrome

def polindrome():
    string = str(raw_input("Type you string: "))
    if len(string) == 0:
        print "you dont type enything"
    else:
        revers_string = string[::-1]
        if revers_string == string:
            print "sring is poindrome"
        else:
            print "string NOT a polindrome"

polindrome()