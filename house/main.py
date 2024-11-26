import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway
from scipy.stats import chi2_contingency
df = pd.read_csv(r"data\train.csv")

df = df[['OverallQual' ,'GrLivArea', 'GarageCars', 'TotalBsmtSF', '1stFlrSF' ,'YearBuilt', 'FullBath', 'TotRmsAbvGrd' ,'GarageArea', 'Foundation', 'ExterCond' ,'ExterQual' , 'Neighborhood', 'KitchenQual' ,'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2','SalePrice','LotArea','GarageArea','WoodDeckSF','OpenPorchSF','EnclosedPorch','3SsnPorch','ScreenPorch','MiscVal','PoolArea','SaleType','Functional']]

print(df.info())