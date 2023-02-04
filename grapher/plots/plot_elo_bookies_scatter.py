import logging
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from scipy.stats import linregress
from matplotlib.lines import Line2D

def plot_elo_bookies_scatter(dataframe, title, show, output_file):
    """
    This function creates four subplots visualising the comparison between Elo probabilities and bookmaker probabilities for home wins, home losses, away wins, and away losses in a given season.
    
    Args:
        - dataframe (pd.DataFrame): A pandas DataFrame containing the processed match results data for a season.
        - title (str, optional): A title to display on the plot. If not provided, the plot will be displayed without a title.
        - show (bool, optional): If True, the plot will be displayed. If False, the plot will be saved to a file.
        - output_file (str, optional): If `show` is False, the file path where the plot will be saved.

    # TODO: make the last n games a parameter
    # TODO: make profit line and linear regression line optional parameters 
    """
    # Read data for matches in a season from a csv file
    matches = dataframe.to_dict('records')

    # initialise coordinate lists 
    home_win_elo_probability = []
    home_win_bookies_probability = []
    away_win_elo_probability = []
    away_win_bookies_probability = []
    home_loss_elo_probability = []
    home_loss_bookies_probability = []
    away_loss_elo_probability = []
    away_loss_bookies_probability = []

    # Calculate the scatter plot data points
    for i, match in enumerate(matches[-180:]): # choose only the last half of the matches
        if match['home-result'] > match['away-result']:
            home_win_elo_probability.append(match['home_win_elo_bookies_draw_odds'])
            away_loss_elo_probability.append(1 - match['home_win_elo_bookies_draw_odds']- match['draw_elo_bookies_draw_odds'])
            home_win_bookies_probability.append(match['home-win-odds'])
            away_loss_bookies_probability.append(match['away-win-odds'])
        else:
            away_win_elo_probability.append(match['away_win_elo_bookies_draw_odds'])
            home_loss_elo_probability.append(1 - match['away_win_elo_bookies_draw_odds']- match['draw_elo_bookies_draw_odds'])
            away_win_bookies_probability.append(match['away-win-odds'])
            home_loss_bookies_probability.append(match['home-win-odds'])

    # Create four subplots
    fig, axes = plt.subplots(2, 2)
    # Add a title
    if title:
        fig.suptitle(title)
    # Create home wins subplot
    axes[0, 0].scatter(x=home_win_elo_probability, y=home_win_bookies_probability, marker='+', c='green', s=20)
    axes[0, 0].set_title('Home')
    # Create home losses subplot
    axes[0, 1].scatter(x=home_loss_elo_probability, y=home_loss_bookies_probability, marker='+', c='red', s=20)
    axes[0, 1].set_title('Home')
    # Create away wins subplot
    axes[1, 0].scatter(x=away_win_elo_probability, y=away_win_bookies_probability, marker='+', c='green', s=20)
    axes[1, 0].set_title('Away')
    # Create away losses subplot
    axes[1, 1].scatter(x=away_loss_elo_probability, y=away_loss_bookies_probability, marker='+', c='red', s=20)
    axes[1, 1].set_title('Away')

    for row in axes:
        for ax in row:
            # Add x and y labels to all subplots
            ax.set_xlabel(r'P$_{Elo}$')
            ax.set_ylabel(r'P$_{bookies}$')
            # Remove unnecessary boarders 
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            # Add y=x profit line
            ax.axline([0.1,0.1],[0.8,0.8], color='black', linewidth=0.5)

    # Add data and linear regression line to each subplot
    for i, (x, y, title) in enumerate(zip([home_win_elo_probability, home_loss_elo_probability, away_win_elo_probability, away_loss_elo_probability],[home_win_bookies_probability, home_loss_bookies_probability, away_win_bookies_probability, away_loss_bookies_probability],['Home', 'Home', 'Away', 'Away'])):
        ax = axes.flatten()[i]
        slope, intercept, r_value, p_value, std_err = linregress(x, y)
        line = slope*np.array(x) + intercept
        # ax.plot(x, line, '-', color='grey', linewidth=0.7)

    # Add a common legend
    green_patch = mpatches.Patch(color='green',label='Win')
    red_patch = mpatches.Patch(color='red', label='Loss')
    # lin_reg = Line2D(x, line, color='grey', linewidth=0.7, label='Lin Reg')
    y_equals_x_line = Line2D(x, line, color='black', linewidth=0.5, label='Profit')
    fig.legend(handles=[green_patch, red_patch], loc = 'upper right')

    plt.tight_layout()

    # save the figure
    if output_file:
        plt.savefig(output_file)
        logging.info(f'Elo vs bookies probabilities scatter graph has been created saved to {output_file}')

    # open the figure 
    if show:
        plt.show()
        plt.close()
