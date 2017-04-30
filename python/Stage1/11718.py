import re

for i in range(100) :
    s = input()
    if(s != "" and len(s) < 101 and s[0] != " "  and  s[len(s) -1] != " ") :
        p = re.compile('[a-zA-Z0-9 ]')
        m = p.match(s)
        if m:
            print(s)
        else:
           break;
    else :
        break

