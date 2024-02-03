def winner_prediction(team_a_score, team_b_score, time_left, possession_of_ball):
    
    #check which team is leading by these conditions 
    if team_a_score > team_b_score: #if team a has more score then ahead team is team a
        leading_team = "Team A" #leading team is team A then 
        score_difference = team_a_score 
    elif team_b_score > team_a_score: #if team b has more score then ahead team is team b
        leading_team = "Team B" #leading team is teams B then
        score_difference = team_b_score 
    else: # this is the third case when scores are equal
        
        return "Both teams have equal winning chances."

    
    ##applying the prediction algorithm 
    score_difference -= 3
    score_difference += 0.5 if leading_team == possession_of_ball else -0.5
    predicted_score = score_difference ** 2

    # Determine the winning possibility
    if predicted_score > time_left:
        return f"{leading_team} has the winning possibility."
    else:
        return "The algorithm cannot determine the winning team. Both teams have equal chances."

def main():
    # User input for the current scores
    team_a_score = int(input("Enter the current score of Team A: "))
    team_b_score = int(input("Enter the current score of Team B: "))

    # User input for the time left in the match (in seconds)
    time_left = int(input("Enter the time left in the match (in seconds): "))

    # User input for the team with the ball
    possession_of_ball = input("Which team has the ball (Team A or Team B)? ").strip()

    # Predict and display the result
    result = winner_prediction(team_a_score, team_b_score, time_left, possession_of_ball)
    print(result)

main()
