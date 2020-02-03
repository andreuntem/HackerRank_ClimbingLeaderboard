def climbingLeaderboard(scores, alice):
    unique_scores = list(reversed(sorted(set(scores))))

    i = len(alice)-1
    j = 0
    ans = []

    while i >= 0:
        if j >= len(unique_scores) or unique_scores[j] <= alice[i]:
            ans.append(j+1)
            i -= 1
        else:
            j += 1

    return reversed(ans)



if __name__ == '__main__':
    str_inp = '''
    6
    100 90 90 80 75 60
    5
    50 65 77 90 102
    '''
    inp = list(map(int,str_inp.split()))
    n_scores = inp[0]
    scores = inp[1:1+n_scores]
    n_alice = inp[n_scores+1]
    alice = inp[-n_alice:]
    climbingLeaderboard(scores, alice)
    