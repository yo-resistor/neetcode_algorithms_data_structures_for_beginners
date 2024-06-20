def main():
    print(climbStairs_fibonacci(44))
    # print(factorial(4))
    
def climbStairs_fibonacci(n: int) -> int:
    steps = []
    for i in range(n + 1):
        if i <= 1:
            steps.append(1)
        else:
            steps.append(steps[i - 1] + steps[i - 2])
    return steps[-1]
    
def climbStairs_factorial(n: int) -> int:
    if n <= 1:
        return n
    
    count = 0
    quotient = int(n / 2)
    print(quotient)
    for i in range(quotient + 1):
        print(n, i, (n - 2 * i))
        count += factorial(n - i) / (factorial(i) * factorial(n - 2 * i))
        
    return int(count)
        

def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
main()