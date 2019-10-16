S=[[],[],[],[],[],[],[],[],[],[]]

def put(S:list, name:str):
    #Calculate wich bucket to use
    bucket = 0
    for index in range(len(name)):
        bucket += ord(name[index])
    bucket = bucket % 10
    #Check if name is already in bucket
    index = len(S[bucket]) - 1
    while index >= 0:
        if S[bucket][index] == name:
            #Do nohing if name is already in the bucket
            return
        index -= 1
    #If code reaches this point we should insert name in the bucket
    S[bucket].append(name)

def isin(S:list, name:str) -> bool:
    # Calculate wich bucket to use
    bucket = 0
    for index in range(len(name)):
        bucket += ord(name[index])
    bucket = bucket % 10
    # Check if name is in bucket
    index = len(S[bucket]) - 1
    while index >= 0:
        if S[bucket][index] == name:
            # It is!
            return True
        index -= 1
    #It is not
    return False

def remove(S:list, name:str) -> bool:
    # Calculate wich bucket to use
    bucket = 0
    for index in range(len(name)):
        bucket += ord(name[index])
    bucket = bucket % 10
    # Check if name is in bucket
    index = len(S[bucket]) - 1
    while index >= 0:
        if S[bucket][index] == name:
            #name is in bucket, let's crop it
            S[bucket] = S[bucket][:index]+S[bucket][index+1:]
            return True
        index -= 1
    #If code reaches this point the name was not in the bucket
    return False

if __name__ == "__main__":
    put(S, "juan")
    put(S, "anna")
    put(S, "pedro")
    put(S, "arturo")
    put(S, "pedro")
    put(S, "oscar")
    put(S, "pepa")
    put(S, "maria")
    put(S, "veronica")
    put(S, "daniel")
    put(S, "pepa")
    print(S)
    print(isin(S,"juan"))
    print(isin(S,"daniela"))
    remove(S, "veronica")
    remove(S, "pepa")
    remove(S, "maria")
    print(S)