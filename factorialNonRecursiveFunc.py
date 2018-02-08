#factorial using Non recursive function
def factorial(ip_no):
    fact_result=1;
    for x in range(1,ip_no+1):
        fact_result *= x;
    return fact_result;
test_ip=int(input("Enter a number for getting its factorial value: "));
if test_ip > 0:
    test_op = factorial(test_ip);
    print("The factorial of given Number ",test_ip," is ",test_op);
elif test_ip == 0:
   print("The factorial of given Number ",test_ip," is ",1);
else:
    print("The invalid number!");
