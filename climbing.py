def climbingLeaderboard(scores, alice):
    
    # create board position:
    leaderboard = []
    for i, score in enumerate(scores):
        if i==0:
            pos = 1    
        elif score<scores[i-1]:
            pos += 1
        leaderboard.append(pos)

    reversed_scores = scores[::-1]
    reversed_leaderboard = leaderboard[::-1]
    length = len(scores)

    alice_position = []
    # run through all alice points
    for score_alice in alice:
        vec_greater_eq = [reversed_leaderboard[i] if score_alice>=reversed_scores[i] else length for i in range(len(scores))]
        if sum(vec_greater_eq) == length*length:
            alice_pos = reversed_leaderboard[0]+1
        else:
            alice_pos = min(vec_greater_eq)

        #print(vec_greater_eq,' -> ', alice_pos)
        alice_position.append(alice_pos)
    
    #print(alice_position)
    return alice_position
        



if __name__ == '__main__':
    str_inp = '''
    1
    1
    2
    1 1
    '''
    inp = list(map(int,str_inp.split()))
    n_scores = inp[0]
    scores = inp[1:1+n_scores]
    n_alice = inp[n_scores+1]
    alice = inp[-n_alice:]
    climbingLeaderboard(scores, alice)
    