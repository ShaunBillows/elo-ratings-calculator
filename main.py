from elo_ratings_calculator import calculate_elo_ratings

calculate_elo_ratings(csv_file='./processed-data/19-20.csv', output_file='./elo-ratings/19-20-full-season.csv')
calculate_elo_ratings(csv_file='./processed-data/19-20.csv', output_file='./elo-ratings/19-20-week-35.csv', weeks=35)
calculate_elo_ratings(csv_file='./processed-data/19-20.csv', output_file='./elo-ratings/19-20-week-30.csv', weeks=30)
calculate_elo_ratings(csv_file='./processed-data/19-20.csv', output_file='./elo-ratings/19-20-week-25.csv', weeks=25)
