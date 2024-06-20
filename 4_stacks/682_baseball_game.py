class Solution:
    def calPoints(self, operations: list[str]) -> int:
        scores = []
        for operation in operations:
            if operation == "D":
                scores.append(2 * scores[-1])
            elif operation == "C":
                scores.pop()
            elif operation == "+":
                scores.append(scores[-1] + scores[-2])
            else:
                try:
                    scores.append(int(operation))
                except:
                    print("The operation is not recognizable")
                    
        return sum(scores)
        
sol = Solution()

case_1 = ["5","2","C","D","+"]
case_2 = ["5","-2","4","C","D","9","+","+"]
case_3 = ["1","C"]

print(sol.calPoints(case_1))
print(sol.calPoints(case_2))
print(sol.calPoints(case_3))