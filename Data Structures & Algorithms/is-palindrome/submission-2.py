class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        for char in s:
            if char.isalnum():
                word += char
        word2 = ""
        for i in range(len(word) - 1, -1, -1):
            word2 += word[i]
        if word.lower() == word2.lower():
            return True
        else:
            return False