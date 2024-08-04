
rounds=[]
roundsnum=int(input("enter the number of points:"))
for i in range(roundsnum):
    point=tuple(eval(input("enter:")))
    rounds.append(point)

def manage_scoreboard(rounds:list[tuple[int,int]])->dict:
    scores={}
    for player ,score in rounds:
        scores[player]=scores.get(player,0)+score
    return scores
result=manage_scoreboard(rounds)
print(result)

