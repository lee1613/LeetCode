class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:


        # Solution 2 (36% Time)
        # dp = [0] * len(questions)

        # def max_point(start, questions, dp):
        #     if start >= len(questions):
        #         return 0
        #     question = questions[start]
        #     if start + question[1] + 1 >= len(questions):
        #         return max(question[0], max_point(start + 1, questions, dp))

        #     else:
        #         if dp[start] != 0:
        #             return dp[start]
        #         else:
        #             dp[start] = max(question[0] + max_point(start + question[1] + 1, questions, dp), max_point(start + 1, questions, dp))
        #             return dp[start]

        # return max_point(0, questions, dp)


        
        dp = [0] * len(questions)
        for i in range(len(questions) - 1, -1, -1):
            index = i + questions[i][1] + 1
            if index < len(questions):
                dp[i] = dp[index] + questions[i][0]
            else:
                dp[i] = questions[i][0]
            if i < len(questions) - 1:
                dp[i] = max(dp[i + 1], dp[i])
        return dp[0]