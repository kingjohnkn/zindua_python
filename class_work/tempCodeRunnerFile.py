.txt', 'r') as f:
    contents = f.read()
    
    matches = pattern.finditer(contents)

    for match in matches:
        print(ma