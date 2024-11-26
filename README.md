# NBA Fantasy Calculator (Connelly Calculator)
A Python-based tool for calculating and ranking NBA players based on fantasy basketball performance.

## Overview
Connelly Calculator processes NBA player statistics and generates fantasy basketball scores using the Sleeper scoring system. It includes optional adjustments for age-based potential, injury risk, and positional scarcity, providing a comprehensive evaluation system for fantasy basketball drafts and player analysis.

## Files
* Connelly.py - Main Python script for calculating fantasy scores
* 2023-24 NBA REGULAR SEASON DATA.xlsx - Excel file containing player statistics for the 2023-24 NBA regular season
  *Please note that Double Double, Triple Double, 40-Point Game, and 50-Point Game are not actual official NBA per game statistics. If you wish to use a different NBA season, the excel sheet will not come with those.*

## Features
* Sleeper league fantasy scoring system
* Interactive user interface with clear explanations
* Optional multipliers for:
  * Age-based potential
  * Injury risk assessment
  * Positional scarcity analysis
* Rankings output for top 50 players

## Scoring System
The scoring system uses my Sleeper league's settings:  
*Make sure to change this to your Sleeper league's settings in the Python code*
### Standard Stats
* Points: 0.75
* Rebounds: 1.00
* Assists: 1.00
* Steals: 2.00
* Blocks: 2.00
* Turnovers: -1.00
* 3-Pointers Made: 0.75  
### Bonus Stats
* Double-Double: 2.00
* Triple-Double: 5.00
* 40-Point Game: 4.00
* 50-Point Game: 10.00

## Optional Multipliers

### Age-Based Potential
* Young stars (≤25): 1.1x boost for future potential
* Prime years (26-30): 1.0x standard rating
* Veterans (>30): 0.9x adjustment for age-related decline

### Injury Risk
* Low Risk: 1.1x boost for consistent availability
* Medium Risk: 1.0x standard rating for typical NBA player
* High Risk: 0.9x adjustment for injury-prone players
* Very High Risk: 0.8x adjustment for major injury concerns

### Positional Scarcity
* Elite: 1.15x boost (>50% better than position average)
* Above Average: 1.05x boost (15-50% above position average)
* Others: 1.0x standard rating

## Requirements
* Python 3.x
* pandas
* numpy
* openpyxl (for Excel file handling)

## Installation
1. Clone the repository:
```bash
git clone https://github.com/ljmakaronica/Fantasy-Draft-Tool-for-Sleeper
```

2. Install required packages:
```bash
pip install pandas numpy openpyxl
```

## Usage
1. Ensure your Excel file is in the same directory as the script
2. Run the script:
```bash
python Connelly.py
```
3. Follow the interactive prompts to select which multipliers you want to apply
4. View the ranked list of the top 50 NBA players based on your selected criteria

## Notes
* Positional scarcity is calculated using players with 20+ minutes per game
* Injury risk ratings are manually assigned based on player history and reputation
* Double-doubles, triple-doubles, and 40/50-point games are calculated by dividing season totals by games played

## Contributing
Feel free to fork this repository and submit pull requests with improvements or bug fixes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
