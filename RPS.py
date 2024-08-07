# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[],player_history=[]):
    responses = {"R":"P","P":"S","S":"R"}
    opponent_history.append(prev_play)
    guess = "R"
    is_abbey = False
    last_ten = player_history[-10:]
    quincy_pattern = "RRPPSRRPPS"

    is_quincy = False
    if len(opponent_history) > 5:
        history = opponent_history[-5:]
        index=quincy_pattern.find("".join(history[:2]))
        if "".join(opponent_history[-3:]) == quincy_pattern[index+2:index+5]:
            is_quincy = True

    if len(player_history) >= 2 and opponent_history[2:-1] == [responses[x] for x in player_history[1:]]:
        print("Kris")
        guess = responses[player_history[-1]]

    elif is_quincy:
        print('Quincy')
        guess = quincy_pattern[index]

    elif len(player_history) >= 2 and opponent_history[-1] == responses[max(set(last_ten), key=last_ten.count)] and opponent_history[-1] == opponent_history[-2]:
        print('Mrguesh')
        last_ten = player_history[-10:]
        guess = responses[max(set(last_ten), key=last_ten.count)]

    elif len(player_history) >=2:
        last_play = player_history[-1]
        probable_moves = [last_play+"R", last_play+"S", last_play+"P"]
        times_played = []
        for move in probable_moves:
            times_played.append(len("".join(player_history).split(move)))
        guess = probable_moves[times_played.index(max(times_played))][-1]
        
        
    
        
        
        
        

    
    
    player_history.append(responses[guess])
    return responses[guess]
