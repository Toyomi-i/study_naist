import pandas as pd

# input data
df = pd.read_excel("BNA_subregions.xlsx")
#df2 = pd.read_excel("../../All_subjects_T1w/stat/Results/BN_MR_A_M_T_G/BN_MR_Ag_Mr_Ti_Ge.xlsx")
df2 = pd.read_excel("../../All_subjects_T1w/stat/Results/BN_MR_A_S_T_G/BN_MR_Ag_Sb_Ti_Ge.xlsx")

##extract BN ROI number
BN_names = df2[[3]]
BN_names = BN_names.drop(BN_names.index[[0]])

BN_nums = BN_names.iloc[:,0].str[-3:]
# confirm
#print(BN_nums)
#print(type(BN_nums))

#add new colum
df2['BA_name'] = ''
# confirm
print(df2)

# correspond BN and BA
i = 1
for BN_num in BN_nums:
    BA_name = df.loc[(df['Label ID.L'] == int(BN_num)) | (df['Label ID.R'] == int(BN_num))]
    BA_name = BA_name.iloc[0,5]

    df2.iloc[i,4] = BA_name
    i = i+1

print(df2)

#df2.to_excel('cBN_MR_Ag_Mr_Ti_Ge.xlsx', index=False, header=False)
df2.to_excel('cBN_MR_Ag_Sb_Ti_Ge.xlsx', index=False, header=False)