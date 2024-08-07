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
        




    if len(player_history) >= 2 and opponent_history[2:-1] == [responses[x] for x in player_history[:-2]]:
        print("Kris")
        guess = responses[player_history[-1]]

    elif is_quincy:
        print('Quincy')
        guess = quincy_pattern[index]

    elif len(player_history) >= 2 and opponent_history[-1] == responses[max(set(last_ten), key=last_ten.count)] and opponent_history[1] != "P":
        print('Mrguesh')
        last_ten = player_history[-10:]
        guess = responses[max(set(last_ten), key=last_ten.count)]

    elif len(player_history) >=2:
        print('abbey')
        window_size = min(10, len(player_history))  # Use the last 10 moves or the length of the history if shorter
        recent_history = player_history[-window_size:]

        move_pairs = [recent_history[i] + recent_history[i + 1] for i in range(len(recent_history) - 1)]

        if move_pairs:
            most_frequent_move_pair = max(set(move_pairs), key=move_pairs.count)
            last_move = most_frequent_move_pair[-1]
        else:
            last_move = player_history[-1]

        guess = responses[last_move]

        
        
        

    
    
    player_history.append(responses[guess])
    return responses[guess]
