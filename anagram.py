cases = int(input().rstrip())

firstsigma = []

secondsigma = []

for i in range(cases):
    line = input().strip()
    
    firstsigma.append(line +  " =")
    
    first, second = line.split("|")
    
    if first == second:
        secondsigma.append("NOT AN ANAGRAM")
    else:
        first = sorted(first)
        second = sorted(second)
        
        if first == second:
            secondsigma.append("ANAGRAM")
        else:
            secondsigma.append("NOT AN ANAGRAM")
            
    
#print
for i in range(len(firstsigma)):
    print(firstsigma[i], secondsigma[i])
