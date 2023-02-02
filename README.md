# Elo Ratings Calculator (WIP)

This package allows you to calculate Elo ratings for a football league using match data. The Elo rating system is a method for calculating the relative skill levels of players in two-player games such as chess, Go, and football. This package can be used to predict the outcome of matches between teams, and track the performance of teams over the course of a season.

Scatter plots showing the Elo rating probabilities vs the bookmakers probabilities for the last half of each season have been recently added! You can find them in the elo_ratings folder.

**Note**: The match data also contains the average and max odds for each match based on a range of bookmakers odds. This project will be extended to use these to test the Elo rating model. Additionally, this project will be extended to compare the performance of a wide range of models, from the basic Poisson distrubution to the modern machine learning approach.

## Features

- Initializes Elo ratings for all teams in a league
- Iterates through each game and updates Elo ratings for both teams
- User can specify the number of weeks into the season to calculate the Elo ratings up to.
- User can calculate the Elo ratings for each week in a season.
- User can calculate the Elo ratings for each match in a season, and compare the Elo predicted probabilities to the bookmakers probabilities.
- Can also import data from multiple seasons.
- Save the results as a csv file or png file.
- User can create a scatter plot showing the Elo vs the bookmakers probabilities for a season, with subplots showing the comparing the difference between home and away games for both win and loss outcomes. User can also add a linear regression line or y=x 'profit' line.

## Requirements

- pandas
- numpy
- scipy
- matplotlib

## Usage

- To generate the graphs, run main.py.

- To generate the elo ratings, follow these instructions. Delete all the csv and png files in the 'elo-ratings' folder, but do not delete the directories (folders). Navigate to main.py. Run only section 2. Next, run only section 3. Finally, run only section 4.

### Elo Rating Calculator Module

A module that calculates Elo ratings for each match in a Premier League season. The module provides the following functions:

#### Class EloCalculator

This class contains the following methods:

##### Method: calculate_individual_elo_ratings

Takes in home and away scores, home and away Elo ratings, and returns the new Elo ratings for both teams.

###### Inputs:

- home_score (int): The home team's score in the match.
- away_score (int): The away team's score in the match.
- home_elo (int): The home team's Elo rating before the match.
- away_elo (int): The away team's Elo rating before the match.

###### Outputs:

- home_elo (int): The home team's updated Elo rating after the match.
- away_elo (int): The away team's updated Elo rating after the match.

##### Method: calculate_elo_ratings_for_one_week

Takes in a CSV file of match data and calculates the Elo ratings for a single week. The results are saved to an output CSV file.

###### Inputs:

- csv_file (str): The path to the CSV file containing the match data.
- output_file (str): The path to the output CSV file to save the results.
- weeks (int, optional): The number of weeks to calculate the Elo ratings for. If not specified, all matches in the CSV file are processed.

##### Method: calculate_elo_ratings_for_each_week

Takes in a CSV file of match data and calculates the Elo ratings for each week of the season. The results are saved to separate output CSV files, one for each week.

###### Inputs:

csv_file (str): The path to the CSV file containing the match data.
output_dir (str): The directory to save the output CSV files.
nb_weeks_in_season (int): The number of weeks in the season.

##### Method: calculate_elo_ratings_for_each_match

Takes in a CSV file of match data and calculates the Elo ratings for each match. The results are saved to an output CSV file.

####### Inputs:

csv_file (str): The path to the CSV file containing the match data.
output_file (str): The path to the output CSV file to save the results.

### Logger Module (WIP)

The Logger module provides logging functionality for the project.

### Grapher Module (WIP)

The Logger module provides logging functionality for the project.

- ##### Method: plot_elo_bookies_scatter

The function reads the data from a match results csv file and calculates a scatter plot of Elo vs bookmakers probabilities. It then creates four subplots, each with the Elo rating on the x-axis and the bookies probabilities on the y-axis. The subplots are split into Home Wins, Home Losses, Away Wins, and Away Losses. It also adds a legend, x and y labels, and a y=x profit line to each subplot. Finally, the graph is saved to the specified output file.

### Generate Match Results Module (WIP)

The Generate Match Results module generates the match results data for a season.

## Author

Shaun Billows
