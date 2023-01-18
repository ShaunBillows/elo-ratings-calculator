# Elo Ratings Calculator

This package allows you to calculate Elo ratings for a football league using match data. The Elo rating system is a method for calculating the relative skill levels of players in two-player games such as chess, Go, and football. This package can be used to predict the outcome of matches between teams, and track the performance of teams over the course of a season.

**Note**: The match data also contains the average and max odds for each match based on a range of bookmakers odds. The project will be extended to use these to test and optimize the algorithm in order to create a betting system app.

## Features

- Initializes Elo ratings for all teams in a league
- Iterates through each game and updates Elo ratings for both teams
- User can specify the number of weeks into the season to calculate the Elo ratings up to.
- User can calculate the Elo ratings for each week in a season.
- Can also import data from multiple seasons
- Save the results as a csv file

## Requirements

- pandas

## Usage

### calculate_elo_ratings_for_one_week(csv_file, output_file, weeks)

This function takes a csv file containing match results, a file name for the output csv file, and an integer representing the week number. The function then calculates the Elo ratings for each team at the specified week and outputs the results to the specified output file.

- If no week is specified, the function will calculate the Elo ratings for the whole season
- If too many weeks are specified, the function will prompt the user

### calculate_elo_ratings_for_each_week(csv_file, output_folder)

This function takes a csv file containing match results and a folder name for the output csv files. The function then calculates the Elo ratings for each team for each week of the dataset and outputs the results to the specified output folder, creating a new file for each week with the format "week-X.csv" where X is the week number.

### elo_rating(rating, k_factor, score, opponent_rating, is_home)

This function takes a team's current Elo rating, the K-factor to use for the calculation, the team's score, the opponent's rating, and a Boolean representing whether the team is playing at home or away. The function then calculates and returns the team's new Elo rating based on the input data.

## Author

Shaun Billows
