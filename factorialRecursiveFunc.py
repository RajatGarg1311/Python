#factorial using recursive function
def factorial(ip_no):
    if ip_no == 0:
        return 1;
    else:
        return (factorial(ip_no-1)*ip_no);
test_ip=int(input("Enter a number for getting its factorial value: "));
if test_ip >= 0:
    test_op = factorial(test_ip);
    print("The factorial of given Number ",test_ip," is ",test_op);
else:
    print("The invalid number!");
