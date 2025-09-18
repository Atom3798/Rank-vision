import matplotlib.pyplot as plt

class ReportGenerator:
    def __init__(self, processed_data):
        self.df = processed_data

    def generate_plot(self, save_path="rank_trend.png"):
        plt.plot(self.df["salesRank"])
        plt.title("Amazon Sales Rank Over Time")
        plt.xlabel("Time")
        plt.ylabel("Sales Rank")
        plt.savefig(save_path)

    def summary(self):
        return {
            "avg_rank": self.df["salesRank"].mean(),
            "best_rank": self.df["salesRank"].min(),
            "worst_rank": self.df["salesRank"].max(),
        }
