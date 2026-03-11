def find_not_finished(participant, completion):
    player = {}

    for name in participant:
        player[name] = player.get(name, 0) + 1

    for name in completion:
        player[name] -= 1
    
    for name in player:
        if player[name] > 0:
            return name

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
rslt = find_not_finished(participant, completion)

print("완주하지 못한 선수: ", rslt)