def climbingLeaderboard(scores, alice):
    
    # create unique sore in ascending order:
    board_score = sorted(list(set(scores)))
    n_board = len(board_score)
    alice_position = []

    # Look for minimum value
    flag_minimum = [i if alice[0]>board_score[i] else -999 for i in range(n_board)]

    pos_inv = max(max(flag_minimum),0)
    for alice_score in alice:
        if alice_score >= max(board_score):
            position = 1
        else:
            while pos_inv < n_board:
                score = board_score[pos_inv]
                if alice_score < score:
                    position = n_board - pos_inv + 1
                    break
                elif alice_score == score:
                    position = n_board - pos_inv
                    break
                pos_inv += 1
        
        alice_position.append(position)
    
    return alice_position
            


if __name__ == '__main__':
    str_inp = '''
    7
    100 100 50 40 40 20 10
    4
    15 25 50 120
    '''
    inp = list(map(int,str_inp.split()))
    n_scores = inp[0]
    scores = inp[1:1+n_scores]
    n_alice = inp[n_scores+1]
    alice = inp[-n_alice:]
    climbingLeaderboard(scores, alice)
    