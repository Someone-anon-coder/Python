for i in range(1, 11, 1):
    if i == 3:
        continue
    
    print(f"i = {i}")


for i in range(1, 11, 1):
    if i == 3:
        break
    
    print(f"i = {i}")


for i in range(1, 11, 1):
    if i == 3:
        pass
    
    print(f"i = {i}")


for i in range(3):
    for j in range(3):
        if j == 2:
            continue
        
        print(f"i: {i}, j: {j}")