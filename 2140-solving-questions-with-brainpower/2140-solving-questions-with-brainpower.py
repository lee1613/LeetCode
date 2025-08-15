class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # maxPoints = [0] * len(questions)

        # choose_max = [0] * len(questions)
        
        # max_point = questions[-1][0]
        # maxPoints[-1] = max_point
        # prev_max_index = len(questions) - 1
        # choose_max[-1] = max_point
        # for i in range(len(questions) -2, -1, -1):
        #     question = questions[i]
        #     curr_point = question[0]

        #     next_question = question[1] + i + 1
        #     if next_question < len(questions):
        #         curr_point += choose_max[next_question]

        #     maxPoints[i] = curr_point
        #     if curr_point > max_point:
        #         max_point = curr_point
        #         for j in range(i, prev_max_index):
        #             choose_max[j] = max_point
        #         prev_max = i
        
        # return max_point

        dp = [0] * len(questions)

        def max_point(start, questions, dp):
            if start >= len(questions):
                return 0
            question = questions[start]
            if start + question[1] + 1 >= len(questions):
                return max(question[0], max_point(start + 1, questions, dp))

            else:
                if dp[start] != 0:
                    return dp[start]
                else:
                    dp[start] = max(question[0] + max_point(start + question[1] + 1, questions, dp), max_point(start + 1, questions, dp))
                    return dp[start]

        return max_point(0, questions, dp)