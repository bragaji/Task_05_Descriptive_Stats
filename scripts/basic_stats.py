import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load data
team_df = pd.read_csv(r"C:\Users\pspra\PycharmProjects\Task_05_Descriptive_Stats\data\team_results.csv")
player_df = pd.read_csv(r"C:\Users\pspra\PycharmProjects\Task_05_Descriptive_Stats\data\player_stats.csv")

# Create folder for output
os.makedirs("output_charts", exist_ok=True)

# 1. Basic Counts
num_games = team_df.shape[0]
num_players = player_df.shape[0]

print(f"Number of Games: {num_games}")
print(f"Number of Players: {num_players}")

# 2. Top Scorers
top_scorers = player_df.sort_values(by='G', ascending=False)[['Player', 'G']].head(5)
print("\nTop Scorers:\n", top_scorers)

# 3. Best Defenders (by Caused Turnovers - CT)
best_defenders = player_df.sort_values(by='CT', ascending=False)[['Player', 'CT']].head(5)
print("\nBest Defenders:\n", best_defenders)

# 4. Scoring Trend Over Time
team_df['Date'] = pd.to_datetime(team_df['Date'], format='%m/%d/%y', errors='coerce')
team_df = team_df.sort_values('Date')
team_df['SU_Score'] = team_df['Score'].str.split('-').str[0].astype(int)
team_df['OPP_Score'] = team_df['Score'].str.split('-').str[1].astype(int)

plt.figure(figsize=(10, 5))
sns.lineplot(data=team_df, x='Date', y='SU_Score', marker='o', label='SU Score')
sns.lineplot(data=team_df, x='Date', y='OPP_Score', marker='o', label='Opponent Score')
plt.title('Scoring Trend Over Games')
plt.xlabel('Game Date')
plt.ylabel('Goals')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig("output_charts/scoring_trend.png")
plt.close()

# 5. Save Top Stats as CSVs
top_scorers.to_csv("output_charts/top_scorers.csv", index=False)
best_defenders.to_csv("output_charts/best_defenders.csv", index=False)
