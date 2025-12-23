def longest_substring_with_max_two(s):
    freq = {}
    left = 0
    max_len = 0
    result = ""

    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1

        while freq[s[right]] > 2:
            freq[s[left]] -= 1
            left += 1
        print(right,'--------',left,'------------', max_len ,'-------',s[right])
        if (right - left + 1) > max_len:
            max_len = right - left + 1
            result = s[left:right+1]

    return result




# res = longest_substring_with_max_two('absdfabebrb')
# print(res)


students = [
    {"name": "Amit", "marks": 85},
    {"name": "Riya", "marks": 92},
    {"name": "Kunal", "marks": 85},
    {"name": "Sara", "marks": 92},
    {"name": "John", "marks": 78}
]
new_dict  = {}

for item in students:
    if not new_dict.get(item['marks'],None):
        new_dict[item['marks']] = []

    new_dict[item['marks']].append(item['name'])

print(new_dict)