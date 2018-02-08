def palindrome(ip_no):
    temp=ip_no;
    sum_result=0;
    while temp>0:
        mod = temp % 10;
        sum_result = (sum_result * 10) + mod;
        temp = temp // 10;
    if sum_result == ip_no:
        return True;
    else:
        return False;
test_ip=int(input("Enter a number to check if it is palindrome: "));
test_op=False;

test_op = palindrome(test_ip);
if test_op == True:
   print("The given Number ",test_ip," is Palindrome.");
else:
   print("The given Number ",test_ip," is not a Palindrome.");
