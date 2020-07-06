def reverseDigit(n):
    x=str(n)[::-1]
    return int(x)
def palindrome(n):
    return reverseDigit(n)==n
n=int(input())
x=0
while(palindrome(n)==False):
    x=reverseDigit(n)
    n+=x
print(n)
