import numpy as np

player_names = np.array([])
player_scores = np.array([30, 50, 70, 80, 90])
i = 0

while i < 5:
    i = i + 1
    temp_name = input("Enter Name:")
    player_names = np.append(player_names, temp_name)
    print(player_names)

processed_scores = np.where(player_scores < 50, 0, player_scores)
Scores_Above_60 = np.where((player_scores <= 75) & (player_scores >= 50), processed_scores+10, processed_scores)
Final_List = list(map(lambda x: x[0], filter(lambda x: x[1] >= 75, zip(player_names, Scores_Above_60))))
Final_List = np.array(Final_List).astype(str).tolist()

print("\n\n\n")
print(f'Player Names: {player_names}')
print(f'Static Scores: {player_scores}')
print(f'Processed Scores: {processed_scores}')
print(f'Scores Above 60: {Scores_Above_60}')
print(f'Players with scores above 75: {Final_List}')


