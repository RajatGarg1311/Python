def prime_no(ip_no):
    div = ip_no // 2;
    
    for x in range(2,div+1):
        test= ip_no % x;
        if test == 0:
            return False;
        else:
            continue;
    return True;

test_ip=int(input("Enter a number to check if it is prime: "));
test_op=False;
#to check if the number given is greater than 1
if test_ip > 0 and test_ip != 1:
    test_op=prime_no(test_ip);
    if test_op == True:
        print("The given Number ",test_ip," is Prime Number.");
    else:
        print("The given Number ",test_ip," is a Composite Number.");
elif test_ip == 1:
    print("The number ",test_ip," is neither prime nor composite.");
elif test_ip == 0:
    print("The given Number ",test_ip," is a Composite Number.");
else:
    print("Primes are integers greater than one. Negative numbers are excluded.");
