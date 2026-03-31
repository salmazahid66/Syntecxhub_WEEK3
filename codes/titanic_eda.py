import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("titanic.csv")

# Basic info
print(df.info())
print(df.isnull().sum())

# Fill missing Age
df["Age"] = df["Age"].fillna(df["Age"].median())

# Create Age Groups
df["AgeGroup"] = pd.cut(df["Age"],
                       bins=[0,12,18,35,60,100],
                       labels=["Child","Teen","Adult","Mid","Senior"])

# 1. Survival by Gender
sns.countplot(x="Sex", hue="Survived", data=df)
plt.title("Survival by Gender")
plt.savefig("../outputs/titanic_gender.png")
plt.close()

# 2. Survival by Class
sns.countplot(x="Pclass", hue="Survived", data=df)
plt.title("Survival by Class")
plt.savefig("../outputs/titanic_class.png")
plt.close()

# 3. Age Distribution
sns.boxplot(x="Survived", y="Age", data=df)
plt.title("Age vs Survival")
plt.savefig("../outputs/titanic_age.png")
plt.close()

# 4. Age Group Analysis
sns.countplot(x="AgeGroup", hue="Survived", data=df)
plt.title("Survival by Age Group")
plt.savefig("../outputs/titanic_agegroup.png")
plt.close()

print("Titanic Premium EDA Done")