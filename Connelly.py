'''
MARKO LJUBOJA - The Connelly Calculator
Named after Tim Connelly, former GM of the Denver Nuggets - Current GM of the Minnesota Timberwolves

This program provides a customizable NBA fantasy score calculator that can incorporate various
factors beyond basic fantasy points, including age-based potential, injury risk, and positional scarcity.
'''
import pandas as pd
import numpy as np
from time import sleep

def welcomeStatement():
    print("\n" + "="*80)
    print("Welcome to The Connelly Calculator".center(80))
    print("Your Advanced NBA Fantasy Basketball Analysis Tool".center(80))
    print("="*80 + "\n")
    sleep(1)
    print("This calculator uses NBA data to evaluate players based on:\n")
    
    # Sleeper Scoring
    print("📊 Sleeper fantasy scoring metrics")
    print("   ├─ Standard Stats:")
    print("   ├─ PTS: 0.75  |  REB: 1.0  |  AST: 1.0  |  STL: 2.0  |  BLK: 2.0  |  TOV: -1.0  |  3P: 0.75")
    print("   └─ Double-Double: 2.0  |  Triple-Double: 5.0  |  40PT Game: 4.0  |  50PT Game: 10.0\n")
    
    # Age-based
    print("⏳ Optional age-based potential adjustments")
    print("   ├─ Young stars (≤25): 1.1x boost for future potential")
    print("   ├─ Prime years (26-30): 1.0x standard rating")
    print("   └─ Veterans (>30): 0.9x adjustment for age-related decline\n")
    
    # Injury Risk
    print("🏥 Optional injury risk considerations")
    print("   ├─ Low Risk: 1.1x boost for consistent availability")
    print("   ├─ Medium Risk: 1.0x standard rating for typical NBA player")
    print("   ├─ High Risk: 0.9x adjustment for injury-prone players")
    print("   └─ Very High Risk: 0.8x adjustment for major injury concerns\n")
    
    # Positional Scarcity
    print("💎 Optional positional scarcity analysis")
    print("   ├─ Elite: 1.15x boost (>50% better than position average)")
    print("   ├─ Above Average: 1.05x boost (15-50% above position average)")
    print("   └─ Others: 1.0x standard rating\n")
    
    print("All data is based on the 2023-24 NBA regular season.\n")
    sleep(2)

def getPreferences():
    print("\nPlease select which factors you'd like to include in your analysis:")
    agePreference = input("Include age-based potential multiplier? (y/n): ").lower() == 'y'
    injuryPreference = input("Include injury risk multiplier? (y/n): ").lower() == 'y'
    scarcityPreference = input("Include positional scarcity multiplier? (y/n): ").lower() == 'y'
    return agePreference, injuryPreference, scarcityPreference

def caluclateFantasyScore(playerData, scoringSystem, agePreference=False, injuryPreference=False, scarcityPreference=False):
    # Base fantasy score calculation
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

    if scarcityPreference:
        # Calculate position-based scarcity
        usefulPlayers = playerData[playerData['MP'] >= 20]
        positionAverages = usefulPlayers.groupby('Pos')['FantasyScore'].mean()
        
        playerData['Position_Value'] = playerData.apply(
            lambda x: ((x['FantasyScore'] - positionAverages[x['Pos']]) / positionAverages[x['Pos']]) * 100, 
            axis=1
        )
        
        # Apply scarcity multiplier
        playerData['FantasyScore'] *= np.where(playerData['Position_Value'] > 50,
            1.15,  # 15% boost for elite
            np.where(playerData['Position_Value'] > 15,
            1.05,  # 5% boost for above average
            1))    # no adjustment for others

    if agePreference:
        # Age-based potential multiplier
        playerData['FantasyScore'] *= np.where(playerData['Age'] <= 25, 1.1,
            np.where(playerData['Age'] <= 30, 1.0, 0.9))

    if injuryPreference:
        # Injury risk multiplier
        playerData['FantasyScore'] *= np.where(playerData['INJ'] == 1, 1.1,
            np.where(playerData['INJ'] == 2, 1.0,
            np.where(playerData['INJ'] == 3, 0.9,
            0.8)))  # Default for injuryRiskScore == 4

    return playerData

def displayResults(playerData):
    sortedPlayerData = playerData.sort_values(by='FantasyScore', ascending=False)
    
    print("\nTop 50 Players by Fantasy Score:\n")
    print("-" * 60)
    print(f"{'Rank':<6}{'Player':<30}{'Score':<10}{'Position':<8}")
    print("-" * 60)
    
    for rank, (index, row) in enumerate(sortedPlayerData[['Player', 'FantasyScore', 'Pos']].head(50).iterrows(), start=1):
        print(f"{rank:<6}{row['Player']:<30}{f'{row['FantasyScore']:.2f}':<12}{row['Pos']:<8}")

def main():
    # Scoring system
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
    
    try:
        # Load data
        playerData = pd.read_excel('2023-24 NBA REGULAR SEASON DATA.xlsx')
        
        # Welcome and get preferences
        welcomeStatement()
        agePreference, injuryPreference, scarcityPreference = getPreferences()
        
        print("\nCalculating scores...")
        sleep(1)
        
        # Calculate scores with selected multipliers
        results = caluclateFantasyScore(
            playerData,
            scoringSystem,
            agePreference,
            injuryPreference,
            scarcityPreference
        )
        
        # Display results
        displayResults(results)
        
        if agePreference or injuryPreference or scarcityPreference:
            print("\nMultipliers applied:")
            if agePreference:
                print("✓ Age-based potential")
            if injuryPreference:
                print("✓ Injury risk")
            if scarcityPreference:
                print("✓ Positional scarcity")
        else:
            print("\nNo multipliers applied - showing raw fantasy scores")
            
    except FileNotFoundError:
        print("Error: Could not find the NBA data file. Please ensure '2023-24 NBA REGULAR SEASON DATA.xlsx' is in the same directory.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
