class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ''.join(filter(str.isalnum, s)).lower()
        start = 0
        end = len(s2) - 1
        for i in range(len(s2)):
            if s2[start] != s2[end]:
                return False
            else:
                start += 1
                end -= 1
        return True