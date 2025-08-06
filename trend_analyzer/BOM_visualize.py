
import pandas as pd
import matplotlib.pyplot as plt
import os

def visualizations(dataset):
    # Ensure folder exists
    os.makedirs("graphs", exist_ok=True)

    # Convert 'Date' to datetime
    dataset["Date"] = pd.to_datetime(dataset["Date"])
    new_df = dataset[["Date", "Polarity", "Subjectivity"]]
    new_df.set_index("Date", inplace=True)

    # Resample weekly
    weekly_avg = new_df.resample("W").mean().dropna()

    polarity_threshold = 0
    subjectivity_threshold = 0.5

    # Set style once
    plt.style.use('seaborn-v0_8-whitegrid')

    # --- Plot 1 & 2: Subplots ---
    fig, axs = plt.subplots(2, 1, figsize=(12, 12), dpi=100, sharex=True)

    # Polarity plot
    axs[0].plot(weekly_avg.index, weekly_avg["Polarity"], linewidth=1.5, marker="o",
                markerfacecolor='white', markeredgewidth=2, label="Polarity")
    axs[0].axhline(y=polarity_threshold, color='red', linestyle='--', linewidth=1.5,
                   label='Positive/Negative Sentiment Boundary')
    axs[0].set_title("Weekly Trends in Positive vs. Negative Sentiment", fontsize=16, fontweight='bold')
    axs[0].set_ylabel("Average Sentiment Score", fontsize=12)
    axs[0].legend(fontsize=10)
    axs[0].grid(True, linestyle='--', alpha=0.7)

    # Subjectivity plot
    axs[1].plot(weekly_avg.index, weekly_avg["Subjectivity"], linewidth=1.5, marker="o",
                markerfacecolor='white', markeredgewidth=2, label="Subjectivity")
    axs[1].axhline(y=subjectivity_threshold, color='red', linestyle='--', linewidth=1.5,
                   label='Minimum Required')
    axs[1].set_title("How Emotional Are the Reviews? Weekly Trend Analysis", fontsize=16, fontweight='bold')
    axs[1].set_xlabel("Review Date (Weekly)", fontsize=12)
    axs[1].set_ylabel("Average Emotional Tone Score", fontsize=12)
    axs[1].legend(fontsize=10)
    axs[1].grid(True, linestyle='--', alpha=0.7)
    axs[1].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    fig.savefig("graphs/sample_graph1.png")

    # --- Plot 3: Combined Polarity & Subjectivity ---
    fig2, ax = plt.subplots(figsize=(12, 6), dpi=100)
    ax.plot(weekly_avg.index, weekly_avg["Polarity"], label="Polarity", marker='o', linewidth=1.5)
    ax.plot(weekly_avg.index, weekly_avg["Subjectivity"], label="Subjectivity", marker='o', linewidth=1.5)

    ax.set_title("Emotional vs. Factual Tone in Reviews: Weekly Comparison", fontsize=16, fontweight='bold')
    ax.set_xlabel("Review Date (Weekly)", fontsize=12)
    ax.set_ylabel("Average Scores", fontsize=12)
    ax.legend(fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.tick_params(axis='x', rotation=45)

    plt.tight_layout()
    fig2.savefig("graphs/sample_graph2.png")
    plt.show()
    plt.close(fig2)



