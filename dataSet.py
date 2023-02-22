import pandas as pd
import matplotlib.pyplot as plt

# 1    Find the top most installed apps (top 10? top 20?) Plot them.
data = pd.read_csv("googleplaystore.csv");
df = pd.DataFrame(data)
sorted_installs = df.sort_values(by=['Installs'], ascending=False).head(11)
"""yaxis = sorted_installs['Installs']
xaxis = sorted_installs['App']
plt.bar(xaxis, yaxis)
plt.xticks(fontsize=10, rotation=90)
plt.yticks(fontsize=10)
plt.title("Top 10 Installed Apps")
plt.show()"""
# 2    Find the most installed categories by average number of installs by category. Which are the most installed categories?

categories = sorted_installs['Category']

categories=sorted_installs.drop(sorted_installs[sorted_installs['Rating'] == 1.9].index, inplace = True)
gp = sorted_installs.groupby('Category').mean()
plt.plot(gp)
plt.xticks(fontsize=10, rotation = 90)
plt.show()
print(gp)
