import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns





df = pd.read_csv('dataset/train.csv')



# df = df.drop(['Id','MSSubClass','MSZoning',
# 	'LotFrontage','Street','LotShape','LandContour','Utilities','LandSlope','Condition1',
# 	'Condition2','OverallQual','OverallCond','YearBuilt','YearRemodAdd','RoofStyle','RoofMatl','Exterior1st',
# 	'Exterior2nd','MasVnrType','MasVnrArea','ExterQual','ExterCond','Foundation','BsmtQual','BsmtCond','BsmtExposure',
# 	'BsmtFinType1','BsmtFinSF1','BsmtFinType2','BsmtFinSF2','BsmtUnfSF','HeatingQC','Electrical','1stFlrSF',
# 	'2ndFlrSF','LowQualFinSF','BsmtFullBath','KitchenQual','Functional','FireplaceQu','Fireplaces',
# 	'GarageYrBlt','GarageYrBlt','GarageFinish','GarageArea','GarageQual',
# 	'GarageCond','WoodDeckSF','OpenPorchSF','EnclosedPorch','3SsnPorch','ScreenPorch','PoolArea',
# 	'PoolQC','Fence','MiscFeature','MiscVal','MoSold','YrSold','SaleType','SaleCondition','Alley','PavedDrive','CentralAir','LotConfig','Heating'], axis = 1) 



# print(df.head())
# print(list(df.columns))



# df['SalePrice'].hist(bins=50).show()





# print ("The skewness of SalePrice is {}".format(df['SalePrice'].skew()))
# target = np.log(df['SalePrice'])
# print ('Skewness is', target.skew())
# plt.hist(target)
# plt.show()



numeric_data = df.select_dtypes(include=[np.number])
cat_data = df.select_dtypes(exclude=[np.number])
# print ("There are {} numeric and {} categorical columns in data frame (train) ".format(numeric_data.shape[1],cat_data.shape[1]))



# corr = numeric_data.corr()
# plt.heatmap(corr)
# plt.show()


# df['OverallQual'].unique()
# # array([ 7,  6,  8,  5,  9,  4, 10,  3,  1,  2])

# pivot = df.pivot_table(index='OverallQual', values='SalePrice', aggfunc=np.median)
# print(pivot)
# pivot.plot(kind='bar', color='red')
# plt.show()

# sns.jointplot(x=df['YearBuilt'], y=df['SalePrice'])
# plt.show()



# sp_pivot = df.pivot_table(index='SaleCondition', values='SalePrice', aggfunc=np.median)
# print(sp_pivot)
# sp_pivot.plot(kind='bar',color='red')
# plt.show()









# cat = [f for f in df.columns if df.dtypes[f] == 'object']
# def anova(frame):
# 	anv = pd.DataFrame()
# 	anv['features'] = cat
# 	pvals = []
# 	for c in cat:
# 		samples = []
# 		for cls in frame[c].unique():
# 			s = frame[frame[c] == cls]['SalePrice'].values
# 			samples.append(s)
# 		pval = stats.f_oneway(*samples)[1]
# 		pvals.append(pval)
# 	anv['pval'] = pvals
# 	return anv.sort_values('pval')

# cat_data['SalePrice'] = df.SalePrice.values
# k = anova(cat_data) 
# k['disparity'] = np.log(1./k['pval'].values) 
# sns.barplot(data=k, x = 'features', y='disparity') 
# plt.xticks(rotation=90) 
# plt.show()