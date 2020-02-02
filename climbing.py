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
    min_board = reversed_scores[0]
    max_board = reversed_scores[-1]

    alice_position = []
    # run through all alice points
    for score_alice in alice:
        
        if score_alice < min_board:
            pos_alice = reversed_leaderboard[0]+1
        elif score_alice == min_board:
            pos_alice = reversed_leaderboard[0]
        elif score_alice >= max_board:
            pos_alice = 1
        else: 
            for ind, score_board in enumerate(reversed_scores):
                
                if score_alice<score_board:
                    pos_alice = reversed_leaderboard[ind]+1
                    break
                elif score_alice==score_board:
                    pos_alice = reversed_leaderboard[ind]
                    break
                
        alice_position.append(pos_alice)
    
    print(alice_position)
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
    