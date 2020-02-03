def binary_search(board_score, alice_score, i_min):

    # start algorithm
    i_max = len(board_score)-1
    i_mid = (i_min+i_max)//2
    d = i_max - i_min

    while d>2:
        score_mid = board_score[i_mid]
        if alice_score<=score_mid:
            i_max = i_mid
        else:
            i_min = i_mid
        i_mid = (i_min+i_max)//2
        d = i_max - i_min
 
    score_min, score_mid, score_max = board_score[i_min], board_score[i_mid], board_score[i_max]
    if score_min <= alice_score < score_mid:
        ind = i_min
    elif score_mid <= alice_score < score_max:
        ind = i_mid
    elif alice_score == score_max:
        ind = i_max
    pos = len(board_score) - ind

    return ind, pos


def climbingLeaderboard(scores, alice):
    
    # create unique sore in ascending order:
    board_score = sorted(set(scores))
    alice_position = []

    ind = 0
    for alice_score in alice:    
        if alice_score < min(board_score):
            pos = len(board_score)+1
        elif alice_score > max(board_score):
            pos = 1
        else:
            ind, pos = binary_search(board_score, alice_score, ind)
        alice_position.append(pos)

    return alice_position


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
    