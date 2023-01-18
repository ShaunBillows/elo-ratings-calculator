# Elo Ratings Calculator

This package allows you to calculate Elo ratings for a football league using match data. The Elo rating system is a method for calculating the relative skill levels of players in two-player games such as chess, Go, and football. This package can be used to predict the outcome of matches between teams, and track the performance of teams over the course of a season.

**Note**: The match data also contains the average and max odds for each match based on a range of bookmakers odds. The project will be extended to use these to test and optimize the algorithm in order to create a betting system app.

## Features

- Initializes Elo ratings for all teams in a league
- Iterates through each game and updates Elo ratings for both teams
- User can specify the number of weeks into the season to calculate the Elo ratings up to.
- Can also import data from multiple seasons
- Save the results as a csv file

## Requirements

- pandas

## Usage

navigate to main.py and run the following:

```
from elo_ratings_calculator import calculate_elo_ratings

calculate_elo_ratings(csv_file='./processed-data/19-20.csv', output_file='./elo-ratings/19-20-full-season.csv')
calculate_elo_ratings(csv_file='./processed-data/19-20.csv', output_file='./elo-ratings/19-20-weeks-35.csv', weeks=35)
calculate_elo_ratings(csv_file='./processed-data/19-20.csv', output_file='./elo-ratings/19-20-weeks-30.csv', weeks=30)
calculate_elo_ratings(csv_file='./processed-data/19-20.csv', output_file='./elo-ratings/19-20-weeks-25.csv', weeks=25)
```

**Note**:

- If no week is specified, the function will calculate the Elo ratings for the whole season
- If too many weeks are specified, the function will prompt the user

## Author

Shaun Billows
