class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        # Test out different possibilities by doing permutation on the numbers and difference operator
        combinations = []

        def find_combination(start):
            if start == len(cards):
                combinations.append([i for i in cards])

            for i in range(start, len(cards)):
                cards[i], cards[start] = cards[start], cards[i]
                find_combination(start + 1)
                cards[i], cards[start] = cards[start], cards[i]

        find_combination(0)


        operators = ["+", "-", "*", "/"]

        operations = []

        def find_operator_combination(combi):
            if len(combi) == 3:
                operations.append([i for i in combi])
            else:
                for operator in operators:
                    combi.append(operator)
                    find_operator_combination(combi)
                    combi.pop(-1)
        
        find_operator_combination([])

        def operate(n1, n2, operator):
            if operator == "+":
                return n1 + n2
            elif operator == "-":
                return n1 - n2
            elif operator == "*":
                return n1 * n2
            else:
                if n2 == 0:
                    return 200000000
                else:
                    return n1 / n2
        
        sequences = [[[0, 1, 0], [2, 4, 1], [3, 5, 2]], [[0, 1, 0], [2, 3, 2], [4, 5, 1]], [[1, 2, 1], [0, 4, 0], [3, 5, 2]], [[1, 2, 1], [3, 4, 2], [0, 5, 0]], [[2, 3, 2], [1, 4, 1], [0, 5, 0]]]


        
        for combination in combinations:
            combination.extend([100000, 100000])
            for operation in operations:
                for sequence in sequences:
                    for i in range(3):
                        step = sequence[i]
                        res = operate(combination[step[0]], combination[step[1]], operation[step[2]])
                        if i == 0:
                            combination[4] = res
                        elif i == 1:
                            combination[5] = res
                        else: 
                            if abs(res - 24) < 0.00000001:
                                return True


        return False








