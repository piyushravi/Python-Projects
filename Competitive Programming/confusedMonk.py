#Code Monk, Number Theory, HackerEarth
#The Confused Monk
#https://www.hackerearth.com/practice/math/number-theory/basic-number-theory-1/practice-problems/algorithm/the-confused-monk/

def gcd(num1, num2):
    if num1==0:
        return num2
    return gcd(num2%num1, num1)
    
def gcdL(L):
    res=0
    for x in L:
        res=gcd(res, x)
        
    return res
    

def mul(L, m):
    res=1
    
    for x in L:
        res*=x
        res%=m
        
    return res%m
    
def sqam(num, exp, m):
    if num==0:
        return 0
    
    if exp==0:
        return 1
        
    if exp%2==1:
        return (num*sqam(num, exp-1, m))%m
        
    return sqam((num*num)%m, exp/2, m)%m
    

def ans(L):
    mod=10**9+7
    exp=gcdL(L)
    num=mul(L, mod)
    
    
    
    return sqam(num, exp, mod)
    
    
n=input()

L=map(int, raw_input().split())

print ans(L)
    
