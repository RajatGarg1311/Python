#Fibonacci Series
def fibonacci(ip_no):
    num1 = 0;
    num2 = 1
    print("Fibonacci Number series is: ")
    for x in range(1,ip_no+1):
        print(num1);
        temp=num1;
        num1 = num2;
        num2 +=temp;
test_ip=int(input("Enter a number : "));
fibonacci(test_ip);
