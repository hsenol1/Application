def isPrime(number):
    for i in range(2,int(number**0.5) +1):
        if (number % i == 0):
            return True;
        
        
    return False;


## True means that it is not a prime. False means it is.





def pyramideWalker(piworks):
   
    
    elements = piworks.split(" ") ## All elements listed here, without any restriction. 
    numElt = len(elements) ## to indicate where we stop.
  
    result = 0   ## will be used the return of pyramideWalker.
    
    count = 1 ## Skipping 0 because I added that manually. If starter point is not valid, no need of using this function.
    row = 2  ## We skip the first row, it only has 1 element and it is added manually.
    
    ## As a note, we can find how many rows are there by simple solution of quadratic function. However, unnecessary.
    
    
    location = 0 ## Indicating the position of last selected item.
    
    alarm = False ## Case when both options are prime. We stop the process.

    result += int(elements[0])
    
    ## Main idea of this function and location variable, if you think each row as a separate list, then from list to list
    ## you only can reach the same previous index or plus one. Because of adjacent number rule.

    while (count != numElt and alarm != True):
        
        
        temp = []
    
        
        for i in range(row):
            candidate = int(elements[count])  
            
            temp.append(candidate)
                
            count += 1
            
        
     
        if (isPrime(temp[location]) == True and isPrime(temp[location +1 ])  == False):
                result += temp[location]
                
             
                
        elif (isPrime(temp[location]) == False and isPrime(temp[location +1 ])  == True):
                result += temp[location+1]
                
                location += 1
                
                
        elif (isPrime(temp[location]) == True and isPrime(temp[location +1 ])  == True and temp[location] >= temp[location +1]):
                result += temp[location]
                
                
        elif (isPrime(temp[location]) == True and isPrime(temp[location+1])== True and temp[location] <= temp[location +1] ):
            result += temp[location +1]
            
            location += 1
             
        elif (isPrime(temp[location]) == False and isPrime(temp[location +1 ]) == False):
            alarm = True
            
            
                
        row += 1
    
    

        
     
    return result


## Used the input given in the Techinal Questionnaire Form.

piwork = "215 193 124 117 237 442 218 935 347 235 320 804 522 417 345 229 601 723 835 133 124 248 202 277 433 207 263 257 359 464 504 528 516 716 871 182 461 441 426 656 863 560 380 171 923 381 348 573 533 447 632 387 176 975 449 223 711 445 645 245 543 931 532 937 541 444 330 131 333 928 377 733 017 778 839 168 197 197 131 171 522 137 217 224 291 413 528 520 227 229 928 223 626 034 683 839 053 627 310 713 999 629 817 410 121 924 622 911 233 325 139 721 218 253 223 107 233 230 124 233"
print(pyramideWalker(piwork))



        
        
        
