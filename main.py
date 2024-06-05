# Example
# 1:
#
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example
# 2:
#
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example
# 3:
#
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""

# string1 = "ABCABC"
# string2 = "ABC"
# #
# string1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
# string2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
# #
# string1 = "aaataaataaataaat"
# string2 = "aaataaat"

# string1 = "LEET"
# string2 = "CODE"

string1 = "ABABAB"
string2 = "ABAB"


# following solution finds the shortest common substring
def longest_common_substring(str1, str2):
    if str1 + str2 != str2 + str1:
        return ""

    short_string = min(str2, str1, key=len)
    longer_string = max(str2, str1, key=len)

    if short_string in longer_string:
        gcd = shortest_repeating_substring(short_string)
        return gcd
    return ""


def shortest_repeating_substring(string):
    n = len(string)

    for i in range(1, n // 2 + 1):
        if n % i == 0:
            substring = string[:i]
            if substring * (n // i) == string:
                return substring

    return string


# following is the solution to find the longest common substring
# def gcdOfStrings(self, str1: str, str2: str) -> str:
#     if str1 + str2 != str2 + str1:
#         return ""
#     if len(str1) == len(str2):
#         return str1
#     if len(str1) > len(str2):
#         return self.gcdOfStrings(str1[len(str2):], str2)
#     return self.gcdOfStrings(str1, str2[len(str1):])


print(longest_common_substring(string1, string2))
