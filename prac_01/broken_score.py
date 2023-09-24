score = float(input(" score:"))

if score >= 0 and score <= 100 :
    if score >= 90 :
        print('excellent')
    elif score >= 50 :
        print('pass')
    else:
        print('bad')
else:
    print('Invalid')