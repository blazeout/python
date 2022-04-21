class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        arr = sentence.split(" ")
        char = "ma"
        index = 1
        res = ""
        a = "a"
        for i in range(len(arr)):
            if arr[i][0] in vowels:
                temp = arr[i]
                temp += char +  a * index
                res += temp + " "
            else:
                temp = arr[i]
                temp = temp[1:] + temp[0] + char + a * index
                res += temp + " "
            index += 1
        return res[:len(res)-1]


s = Solution()
s.toGoatLatin("I speak Goat Latin")