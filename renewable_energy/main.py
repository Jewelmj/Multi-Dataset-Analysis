import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway
from scipy.stats import chi2_contingency
import warnings

warnings.filterwarnings("ignore")

df_01 = pd.read_csv(r"archive\01.csv")
df_02 = pd.read_csv(r"archive\02.csv")
df_03 = pd.read_csv(r"archive\03.csv")
df_04 = pd.read_csv(r"archive\04.csv")
df_05 = pd.read_csv(r"archive\05.csv")
df_06 = pd.read_csv(r"archive\06.csv")
df_07 = pd.read_csv(r"archive\07.csv")
df_08 = pd.read_csv(r"archive\08.csv")
df_09 = pd.read_csv(r"archive\09.csv")
df_10 = pd.read_csv(r"archive\10.csv")
df_11 = pd.read_csv(r"archive\11.csv")
df_12 = pd.read_csv(r"archive\12.csv")
df_13 = pd.read_csv(r"archive\13.csv")
df_14 = pd.read_csv(r"archive\14.csv")
df_15 = pd.read_csv(r"archive\15.csv")
df_16 = pd.read_csv(r"archive\16.csv")
df_17 = pd.read_csv(r"archive\17.csv")

df_list = [df_01,df_02,df_03,df_04,df_05,df_06,df_07,df_08,df_09,df_10,df_11,df_12,df_13,df_14,df_15,df_16,df_17]
for df in df_list:
    df.drop(['Code'], axis=1, inplace=True)
    print(df.columns)

