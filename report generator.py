import matplotlib.pyplot as plt
import pandas as pd

class ReportGenerator:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def generate_plot(self, save_path: str = "rank_trend.png"):
        plt.figure()
        plt.plot(self.df["timestamp"], self.df["salesRank"])
        plt.title("Amazon Sales Rank Over Time")
        plt.xlabel("Time")
        plt.ylabel("Sales Rank (lower is better)")
        plt.tight_layout()
        plt.savefig(save_path)

    def summary(self) -> dict:
        s = self.df["salesRank"].describe()
        return {
            "avg_rank": float(s["mean"]),
            "best_rank": float(self.df["salesRank"].min()),
            "worst_rank": float(self.df["salesRank"].max()),
            "observations": int(s["count"]),
        }
