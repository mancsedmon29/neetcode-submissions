class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. iba na agad length, di na anagram
        if len(s)!= len(t):
            return False

        # 2. bilangin bawat letter
        count = [0] * 26

        for c in s:
            count[ord(c) - ord('a')] += 1

        for c in t:
            count[ord(c) - ord('a')] -= 1

        # 3. pag may hindi 0, may kulang/sobra
        for val in count:
            if val!= 0:
                return False

        return True