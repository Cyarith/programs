username = ["Carl", "Tamsin", "Eric", "Zoe", "Alan", "Mark"]
numitems = len(username)

while username == username:
    for i in range(0,numitems-2):
        for j in range(0,numitems-i-1):
            if username[j] > username[j+1]:
                name1 = username[j]
                name2 = username[j+1]
                username[j] = name2
                username[j+1] = name1
                print(username)

print(username)
            
        
            
