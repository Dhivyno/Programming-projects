nums = [1, 2, 3, 4, 5, 6]

for number in nums:
    a = number
    for number2 in nums:
        b = number2
        for number3 in nums:
            c = number3
            for number4 in nums:
                d = number4
                for number5 in nums:
                    e = number5
                    for number6 in nums:
                        f = number6
                        if ((100*e+40+f)-(100*c+50+d)) == ((100*c+50+d)-(10*a+b)):
                            if a!=b!=c!=d!=e!=f:
                                print(a,b, "  ", c,"5",d, "  ", e,"4",f, "  ", a, b, c, d, e, f,"  ", "d = ", (100*e+40+f)-(100*c+50+d), "= ", (100*c+50+d)-(10*a+b), "  ", "product = ", (100*e+40+f)*(100*c+50+d)*(10*a+b)*3.8/10**6)