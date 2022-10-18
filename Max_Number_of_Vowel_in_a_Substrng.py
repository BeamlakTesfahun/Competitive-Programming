class Solution(object):
    def maxVowels(self, s, k):
        vowels = {"a", "e", "i", "o", "u"}
        vowel_count = 0
        for i in range(k):
            if s[i] in vowels:
                vowel_count += 1
        left = 0
        right = k-1
        max_vowel = vowel_count
        while right < len(s) - 1:
            if s[left] in vowels:
                vowel_count -= 1
            left += 1
            right += 1
            if s[right] in vowels:
                vowel_count += 1
            max_vowel = max(max_vowel, vowel_count)
        return max_vowel
