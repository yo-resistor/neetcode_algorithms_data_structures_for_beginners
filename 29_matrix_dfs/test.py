def plus(a, b):
    result = []
    def plus_function(a, b):
        c = a + b
        result.append(c)
        
    plus_function(1, 2)
    print(result)
    
plus(1,2)