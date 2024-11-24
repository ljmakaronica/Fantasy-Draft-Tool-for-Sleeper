#MARKO LJUBOJA
#This project allows you to 

import pandas as pd
import numpy as np

# Load the 2023-24 regular season data
playerData = pd.read_excel('2023-24 NBA REGULAR SEASON DATA.xlsx')

#Sleeper league's fantasy basketball scoring system
#You will need to alter this to line up with your Sleeper league's scoring system.
#Update each stat accordingly
scoringSystem = {
    'PTS': 0.75,
    'TRB': 1,
    'AST': 1,
    'STL': 2,
    'BLK': 2,
    'TOV': -1,
    '3P': 0.75,
    'DD2': 2,
    'TD3': 5,
    '40PTS': 4,
    '50PTS': 10
}



# Check if all necessary columns exist in the data
required_columns = ['PTS', 'TRB', 'AST', 'STL', 'BLK', 'TOV', '3P', 'DD2', 'TD3', '40PTGAME', '50PTGAME', 'INJ', 'Age', 'Player']
missing_columns = [col for col in required_columns if col not in playerData.columns]
if missing_columns:
    raise ValueError(f"Missing columns in the dataset: {missing_columns}")




# Calculate fantasy scores
playerData['FantasyScore'] = (
    playerData['PTS'] * scoringSystem['PTS'] +
    playerData['TRB'] * scoringSystem['TRB'] +
    playerData['AST'] * scoringSystem['AST'] +
    playerData['STL'] * scoringSystem['STL'] +
    playerData['BLK'] * scoringSystem['BLK'] +
    playerData['TOV'] * scoringSystem['TOV'] +
    playerData['3P'] * scoringSystem['3P'] +
    playerData['DD2'] * scoringSystem['DD2'] +
    playerData['TD3'] * scoringSystem['TD3'] +
    playerData['40PTGAME'] * scoringSystem['40PTS'] +
    playerData['50PTGAME'] * scoringSystem['50PTS'] 
)



#The following two sections are subjective. Injury risk was calculated based on injury history/reputation.
#If you would like objective measurements, feel free to omit both injury risk and age from your calculation.

#Adjust FantasyScore based on injury risk
playerData['FantasyScore'] *= np.where(playerData['INJ'] == 1, 1.1,
    np.where(playerData['INJ'] == 2, 1.0,
    np.where(playerData['INJ'] == 3, 0.9,
    0.8))  # Default for injuryRiskScore == 4
)


# Add potential growth adjustment (younger players get a small boost)
playerData['FantasyScore'] *= np.where(playerData['Age'] <= 25, 1.1,
    np.where(playerData['Age'] <= 30, 1.0, 0.9))




# Sort players by fantasy score
sortedplayerData = playerData.sort_values(by='FantasyScore', ascending=False)



# Define the number of characters for formatting
name_width = 30
score_width = 10



# Create a header
separator = f"------{'-' * 4}-{'-' * (name_width + 2)}-{'-' * (score_width + 2)}-"

print(separator)

# Display the top 50 players with rankings
for rank, (index, row) in enumerate(sortedplayerData[['Player', 'FantasyScore']].head(50).iterrows(), start=1):
    print(f"| {rank:<2} |{' ' * 4}{row['Player'].ljust(name_width)} | {row['FantasyScore']:<{score_width}.6f} |")
    print(separator)
    
