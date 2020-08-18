def substrinsgk(s, k):
    if not s or k == 0:
        return []

    letter, res = {}, list()
    start = 0
    for i in range(len(s)):
        if s[i] in letter and letter[s[i]] >= start:
            start = letter[s[i]]+1
        letter[s[i]] = i
        # if i-start+1 == k:
        res.append(s[start:i+1])
        start += 1
    return res


s = "pqpqs"
k = 2
print(substringk(s, k))
d
