# Santiago Nunez-Corrales and Eric Jakobsson
# Illinois Informatics and Molecular and Cell Biology
# University of Illinois at Urbana-Champaign
# {nunezco,jake}@illinois.edu

# A simple tunable model for COVID-19 response
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from covidmodel import CovidModel


plt.figure(figsize = (11.7, 8.27))
df_00 = pd.read_csv("cu_il_no_testing.csv")
df_05 = pd.read_csv("cu_il_05pc_testing.csv")
df_10 = pd.read_csv("cu_il_10pc_testing.csv")
df_20 = pd.read_csv("cu_il_20pc_testing.csv")
df_40 = pd.read_csv("cu_il_40pc_testing.csv")
df_50 = pd.read_csv("cu_il_50pc_testing.csv")
df_75 = pd.read_csv("cu_il_75pc_testing.csv")
df_90 = pd.read_csv("cu_il_90pc_testing.csv")
df_all = pd.read_csv("cu_il_all_testing.csv")

df = pd.DataFrame()
df["Step"] = df_00["Step"]/96
df["Iteration"] = df_00["Iteration"]
df["0%"] = df_00["Severe"]
df["5%"] = df_05["Severe"]
df["10%"] = df_10["Severe"]
df["20%"] = df_20["Severe"]
df["40%"] = df_40["Severe"]
df["50%"] = df_50["Severe"]
df["75%"] = df_75["Severe"]
df["90%"] = df_90["Severe"]
df["all"] = df_all["Severe"]

df_melt = df.melt(id_vars=['Step','Iteration'])
#print(df_melt)
ax = sns.lineplot(x="Step", y="value", hue="variable", data=df_melt, ci=None, palette=sns.color_palette('YlOrRd_r', n_colors=9))
ax.legend(title="C-U, Severe", fontsize='small')
ax.set_xlabel("Days")
ax.set_ylabel("Fraction of the population")
#ax.set(yscale="log")
plt.axvline(x=40, linestyle="--", color='black')
plt.savefig("cu_il_severe.png", dpi=300)

