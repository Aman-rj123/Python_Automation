#count Digits (No str)  
#Count digits in a number without converting to string.  
#python
def count_digits(n):
    n = abs(n)
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count

print(count_digits(123459999))  # 

def Count_Digit1(n):
    n =abs(n)
    count=0
    while n>0:
        n=n//10
        count=count+1
    return count

print(Count_Digit1(123))
        
    
