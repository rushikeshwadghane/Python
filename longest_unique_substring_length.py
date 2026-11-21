"""Finds the length of a longest substring without repeated characters."""




def lengthOfLongestSubstring(s: str) -> int:
    ml = 0
    seen  ={}
    left = 0
    for r in range(len(s)):
        if s[r] in seen and seen[s[r]] >= left:
            left = seen[s[r]] + 1

        seen[s[r]] = r
        ml = max(ml,(r-left) + 1)

    return ml

print(lengthOfLongestSubstring('abcabcbb'))
