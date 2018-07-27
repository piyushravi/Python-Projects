#https://app.codesignal.com/challenge/DfQ3jYW9sKJj6r4Pv

def word(n):
    t0 = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    
    t3 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    k = n%100
    p1 = n%10
    
    n = n//10
    p2 = n%10
    n = n//10
    
    
    if n!=0:
        res = t0[n]+" hundred"
        if k!=0:
            res += ' '
    else:
        res = ''
    
    last = ''
    if k<20:
        last = t0[k]
    else:
        s = k-20
        s = s//10
        last = t3[s]
        if (k%10)!=0:
            last +='-'+t0[k%10]
        
                
    return res+last        
            
            
    
    

def numberInWords(n):
    p1 = n%1000
    n = n//1000
    p2 = n%1000
    n = n//1000
    p3 = n%1000
    
    res = []
    
    print p1, p2, p3
    if p3!=0:
        res.append(word(p3)+' million')
    
    if p2!=0:
        res.append(word(p2)+' thousand')
    
    if p1!=0:
        res.append(word(p1))
    
    print res
    res = " ".join(res)
    res = res.capitalize()
    
    return (res)
        
        
    

