CurStr = input('Please Input USD or RMB' )
if CurStr[0:3] == "RMB":
    print("USD{:.2f}".format(eval(CurStr[3:])/6.78))
elif CurStr[0:3] == "USD":
    print("RMB{:.2f}".format(eval(CurStr[3:])*6.78))
