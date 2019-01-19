a=int(input('enter time:'))

if a<12:
    print('good morning')

if 12>a and a<=17:
    print('good afternoon')


elif a>18 and a<=20:
    print('good evening')


elif a>20 and a<=24:
    print('good night')


elif a>24:
    print('time format is not ok')