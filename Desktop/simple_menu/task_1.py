def solution(s):
    splitting = [s[i]+'_' if len(s[i:]) == 1 else s[i:i+2] for i in range(0, len(s), 2)]
    print(splitting)
solution('ads')
