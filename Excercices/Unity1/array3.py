more_whales= [5,4,7,3,2,3,2,6,4,2,1,7,1,3]

more_whales2=more_whales.copy()

for row in range(len(more_whales)):
    
   more_whales2[row]+=1

    
    
print("Original: ",more_whales)
print("Append 1: ",more_whales2)
