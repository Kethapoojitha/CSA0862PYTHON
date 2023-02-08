s = input ("enter string s: ")
t = input ("enter string t: ")
result = is_isomorphic(s, t)
if result:
    print("the strings are isomorphic.")
else:
    print("the strings are not isomorphic.")

def is_isomorphic(s, t):
    if len(s) != len(t):
        return false
    char_map = {}
    for i in range(len(s)):
        if s[i] in char_map11:
            if char_map[s[i]] != t[i]:
                return false
            elif t[i] in char_map.values():
                return false
            else:
                char_map[s[i]] = t[i]
        return True
                  
