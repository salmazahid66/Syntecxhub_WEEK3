import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("netflix.csv")

# 1. Type Distribution
sns.countplot(x="type", data=df)
plt.title("Movies vs TV Shows")
plt.savefig("../outputs/netflix_type.png")
plt.close()

# 2. Year Trend
df["release_year"].value_counts().sort_index().plot()
plt.title("Content Growth Over Time")
plt.savefig("../outputs/netflix_year.png")
plt.close()

# 3. Top Genres
top_genres = df["listed_in"].value_counts().head(10)
top_genres.plot(kind="bar")
plt.title("Top Genres")
plt.savefig("../outputs/netflix_genres.png")
plt.close()

# 4. Country Distribution
top_countries = df["country"].value_counts().head(10)
top_countries.plot(kind="bar")
plt.title("Top Countries Producing Content")
plt.savefig("../outputs/netflix_country.png")
plt.close()

print("Netflix Premium EDA Done")