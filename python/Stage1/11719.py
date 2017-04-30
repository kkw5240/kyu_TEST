import re

for i in range(100) :
    s = input()
    if(s == "") :
        print(s)
    else :
        if(len(s) < 101) :
            p = re.compile('[a-zA-Z0-9 ]')
            m = p.match(s)
            if m:
                print(s)
            else:
               break;
        else :
            break

