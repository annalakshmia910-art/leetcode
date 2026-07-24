class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        d = {
            "2":"abc", "3":"def", "4":"ghi", "5":"jkl",
            "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"
        }

        res = [""]

        for digit in digits:
            temp = []
            for s in res:
                for ch in d[digit]:
                    temp.append(s + ch)
            res = temp

        return res