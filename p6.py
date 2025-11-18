# Reversed number is a number the order of digits is reversed. The first digit becomes last and vice versa. Note that all the leading zeros are omitted. That means if the number ends with a zero, the zero is lost by reversing (e.g. 1200 gives 21). Also, note that the reversed number never has any trailing zeros.

# Jones needs to calculate with reversed numbers. Your task is to add two reversed numbers and output their reversed sum. Of course, the result is not unique because any particular number is a reversed form of several numbers (e.g. 21 could be 12, 120 or 1200 before reversing). Thus we must assume that no zeros were lost by reversing (e.g. assume that the original number was 12).

# Input:
# The input consists of N cases. The first line of the input contains only positive integer N. Then follow the cases. Each case consists of exactly one line with two positive integers separated by space. These are the reversed numbers you are to add.

# Constraints:
# 1 <= N <= 10^5
# 1 <= a <= 10^18
# 1 <= b <= 10^18

# Output:
# The reversed sum of two reversed numbers. Omit any leading zeros in the output.

# Example:
# Sample input:
# 3
# 24 1
# 4358 754
# 305 794

# Sample output:
# 34
# 1998
# 1

a= int(input("Enter num1: "))
b= int(input("Enter num2: "))
 
reversed_a = 0
reversed_b =0 
while (a>0) :
    digit = a % 10
    reversed_a = reversed_a * 10 + digit
    a //= 10
print(f"Reverse of num1 is {reversed_a}")
while (b>0) :
    digit = b % 10
    reversed_b = reversed_b * 10 + digit
    b //= 10
print(f"Reverse of num2 is {reversed_b}")

sum = reversed_a + reversed_b
print(f"Sum of reversed number is {sum}")
reversed_sum=0
while (sum>0) :
    digit = sum % 10
    reversed_sum = reversed_sum * 10 + digit
    sum //= 10
print(f"Reverse of sum is {reversed_sum}")
