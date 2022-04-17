from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: [str]) -> str:
        n = len(paragraph)
        ban = set(banned)
        count = Counter()
        word = ""
        for i in range(n + 1):
            if i < n and paragraph[i].isalpha():
                word += paragraph[i].lower()
            elif word != "":
                if word not in ban:
                    count[word] += 1
                word = ""
        maxCount = max(count.values())
        return next(strs for strs, v in count.items() if v == maxCount)


s = Solution()
print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
