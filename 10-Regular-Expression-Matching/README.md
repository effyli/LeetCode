# Regular Expression Matching
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true

# Solution
Solution 1. Recursion: 
1. Check if the first letter in pattern is equal to the first letter in s or '.' (first_match)
2. Check if the second letter in pattern is '*', if it is, and the first_match is true, 
then remove the first letter in s, recursion with (s[1:], p). If it is and the first_match is not true,
then recursion with the left part in p -> (s, p[2:]). If it is not and the first_match is true, 
recursion with (s[1:], p[1:]). Other condition is false. 
3. If the last check, p is empty, then return bool(s).

Solution 2. Dynamic Programming:
1. create a dp table filled with false
2. init the first corner, first row and column
3. follow the dp rules to update the table 


