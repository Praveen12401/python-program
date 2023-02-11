
status=True
while status:
    try:
        n = (input("enter a binary number:  "))

        t = int(n)
        c = {'0', '1'}
        p = set(n)

        if c == p or p == {'0'} or p == {'1'}:
            print("number is binary ")
            # n = int(input("enter a binary number"))
            print("-" * 30)
            n = t
            pow = 0
            sum = 0
            while n > 0:
                r = n % 10
                sum = sum + (2 ** pow) * r
                n = n // 10
                pow += 1
            print(t, "of decimal number ", sum)
            print("-" * 30)
            if sum % 2 == 0:
                print("this number ", sum, " is even !")
                status = False
            else:
                print("this number ", sum, " is odd !")
                status = False
        else:

            print("not binary number: 10101110 : please  enter this formet ")
    except:
        print("invalid input please inter only binary number")
        continue
