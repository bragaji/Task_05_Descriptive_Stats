import pandas as pd

# URL of the sports stats page
url = 'https://cuse.com/sports/womens-lacrosse/stats/2024/'

# Extract tables from the page
tables = pd.read_html(url)  # Requires lxml or html5lib

# View table count and structure
print(f"Found {len(tables)} tables")
for i, table in enumerate(tables):
    print(f"\nTable {i} Preview:")
    print(table.head())

# Save the desired table (e.g., the first one)
tables[0].to_csv(r"C:\Users\pspra\PycharmProjects\Task_05_Descriptive_Stats\data\game_stats.csv", index=False)
