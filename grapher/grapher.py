from .plots import plot_elo_bookies_scatter

class Grapher:

    @staticmethod
    def plot_elo_bookies_scatter(csv_file, output_file, title):
        plot_elo_bookies_scatter(csv_file, output_file, title)
        
    # @staticmethod
    # def plot_poisson_bookies_scatter(csv_file, output_file, title):
    #     plot_poisson_bookies_scatter(csv_file, output_file, title)






# this is for the next stage, which is allowing the data to be optionally saved to an SQL db

# class Grapher:
#     def __init__(self, save_to_file=True, upload_to_db=False):
#         self.save_to_file = save_to_file
#         self.upload_to_db = upload_to_db

#     def plot_elo_bookies_scatter(self, csv_file, output_file, title):
#         # code to plot the graph using csv_file, output_file, and title
#         result = ... # data for the graph

#         if self.save_to_file:
#             # save the result to a CSV file
#             ...
#         if self.upload_to_db:
#             # upload the result to an SQL database
#             ...

