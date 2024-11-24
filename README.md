# NBA Fantasy Calculator

A Python-based tool for calculating and ranking NBA players based on fantasy basketball performance, inspired by Tim Connelly's player evaluation methods.

## Overview

This tool processes NBA player statistics and generates fantasy basketball scores using customizable scoring systems. It includes adjustments for injury risk and player age, providing a comprehensive evaluation system for fantasy basketball drafts and player analysis.

## Files

* Connelly.py - Main Python script for calculating fantasy scores
* 2023-24 NBA REGULAR SEASON DATA.xlsx - Excel file containing player statistics for the 2023-24 NBA regular season
  * *Please note that Double Double, Triple Double, 40-Point Game, and 50-Point Game are not actual official NBA per game statistics. If you wish to use a different NBA season, the excel sheet will not come with those.*

## Features

* Custom fantasy point calculation based on Sleeper league scoring system
* Injury risk adjustment (scale of 1-4)
* Age-based potential adjustment
* Rankings output for top 50 players
* Easily modifiable scoring system

## Scoring System

The default scoring system (based on my personal Sleeper league's settings):

| Statistic | Points |
|-----------|--------|
| Points | 0.75 |
| Rebounds | 1.00 |
| Assists | 1.00 |
| Steals | 2.00 |
| Blocks | 2.00 |
| Turnovers | -1.00 |
| 3-Pointers Made | 0.75 |
| Double-Double | 2.00 |
| Triple-Double | 5.00 |
| 40-Point Game | 4.00 |
| 50-Point Game | 10.00 |

## Modifiers
These modifiers are OPTIONAL. If you just want objective data, only use the scoring system. Injury risk was manually determined for the 2023-24 NBA season. 
Age is an objective measure, but if you are not playing in a dynasty league, it may be less useful for you.

### Injury Risk Modifier

| Risk Level | Multiplier |
|------------|------------|
| Level 1 (Lowest) | 1.1x |
| Level 2 | 1.0x |
| Level 3 | 0.9x |
| Level 4 (Highest) | 0.8x |

### Age Modifier

| Age Range | Multiplier |
|-----------|------------|
| 25 and under | 1.1x |
| 26-30 | 1.0x |
| Over 30 | 0.9x |

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

The script will output a ranked list of the top 50 NBA players based on their calculated fantasy scores.

## Customization

To modify the scoring system, edit the `scoringSystem` dictionary in `Connelly.py`:

```python
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
```


## Notes

* Injury risk ratings are manually assigned based on player history and reputation
* Double-doubles, triple-doubles, and 40/50-point games are calculated by dividing season totals by games played

## Contributing

Feel free to fork this repository and submit pull requests with improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
