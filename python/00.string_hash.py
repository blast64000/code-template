#no refactoring

class hash_test:    
    participant = ["leo","kiki","eden"]
    completion = ["leo","kiki"]

    p = 31
    m = 0xfffff
    x = 0
    hash_table = list([0 for i in range(m)])
    unfinished = list()
    
    
    # polynomial rolling hash function.
    for i in participant:
        print(i)
        mod_value=0
        for j in i:
            mod_value = mod_value + ord(j)*pow(p,x)
            x+=1
        hash_table[mod_value % m] = 1    
    
    #hash for completion
    for k in completion:
        print(k)
        mod_value=0
        for j in i:
            mod_value = mod_value + ord(j)*pow(p,x)
            x+=1
        if hash_table[mod_value % m] != 1:
            unfinished.append(i)
            print("unfinished="+i)

                
