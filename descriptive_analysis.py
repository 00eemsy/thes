import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
from scipy.stats import chisquare, chi2_contingency
import numpy as np

df = pd.read_csv('thesis_data.csv')
df = df.dropna(axis=1, how='all') # gets rid of empty columns,,, which the csv somehow came w?

# ---------------- AVERAGES ----------------
# per website!
avg_speed_per_website = df.groupby('Website')['Speed'].mean()
avg_mr_per_website = df.groupby('Website')['Misclick_Rate'].mean()

# print('avg speed per website: ')
# print(avg_speed_per_website)
# print('avg misclick rate per website:')
# print(avg_mr_per_website)

# per website w age
avg_speed_per_website_and_age = df.groupby(['Website', 'Age'])['Speed'].mean()
avg_mr_per_website_and_age = df.groupby(['Website', 'Age'])['Misclick_Rate'].mean()

# print('avg speed per website and age:')
# print(avg_speed_per_website_and_age)
# print('avg misclick rate per website and age:')
# print(avg_mr_per_website_and_age)

# - across all 6 websites!
avg_total_speed = df.groupby('Maze_ID')['Speed'].sum().mean()
avg_total_mr = df.groupby('Maze_ID')['Misclick_Rate'].mean().mean()

# print('avg total speed (sum across 6 websites): ' + str(avg_total_speed))
# print('avg total misclick rate (sum across 6 websites): ' + str(avg_total_mr))
#FIXME:
# print('avg total speed variance: ' + str(df.groupby('Maze_ID')['Speed'].sum().var()))
# print('avg total misclick rate variance: ' + str(df.groupby('Maze_ID')['Misclick_Rate'].mean().var()))

# across... w age 
avg_total_speed_per_age = df.groupby(['Maze_ID', 'Age'])['Speed'].sum().groupby('Age').mean()
avg_total_mr_per_age = df.groupby(['Age'])['Misclick_Rate'].mean()

# print('avg total speed per age (summed across 6 websites): ' + str(avg_total_speed_per_age))
# print('avg total misclick per age (summed across 6 websites): ' + str(avg_total_mr_per_age))



# ---------------- PER ICON TYPE ----------------
# with data from both age groups
speed_per_icon_type = df.groupby('Icon')['Speed'].mean()
mr_per_icon_type = df.groupby('Icon')['Misclick_Rate'].mean()

# print('speed per icon type: ')
# print(speed_per_icon_type)
# print('misclick rate per icon type: ')
# print(mr_per_icon_type)

# with data split b/t age groups
speed_per_icon_type_and_age = df.groupby(['Icon', 'Age'])['Speed'].mean()
mr_per_icon_type_and_age = df.groupby(['Icon', 'Age'])['Misclick_Rate'].mean()

# print('speed per icon type and age: ')
# print(speed_per_icon_type_and_age)
# print('misclick rate per icon type and age: ')
# print(mr_per_icon_type_and_age)

# also per website too
speed_per_icon_type_and_age_and_website = df.groupby(['Website', 'Icon', 'Age'])['Speed'].mean()
mr_per_icon_type_and_age_and_website = df.groupby(['Website', 'Icon', 'Age'])['Misclick_Rate'].mean()

# print('speed per icon type and age and website: ')
# print(speed_per_icon_type_and_age_and_website)
# print('misclick rate per icon type and age and website: ')
# print(mr_per_icon_type_and_age_and_website)

# ---------------- DROP-OFFS ----------------
# 393 total, 240 finished = 153 drop offs (.389)
# should've been 131 per icon group w the 393 total
# % of each icon type per 240 ppl (and probs distr b/t age groups too)
icon_type_distr = df.groupby('Icon')['Maze_ID'].nunique()
icon_type_distr_percentages = icon_type_distr / 240
icon_type_distr_per_age = df.groupby(['Icon', 'Age'])['Maze_ID'].nunique()
icon_type_distr_per_age_percentages = icon_type_distr_per_age / 240

# print('icon type distribution:')
# print(icon_type_distr_percentages)
# print('icon type distribution per age:')
# print(icon_type_distr_per_age)
# print(icon_type_distr_per_age_percentages)

# ok sick
# IO = missing 52
# IWTL = missing 56
# TO = missing 45
# total missing 153


# ok so drop off rate (calculated from the )
# expected missing per group = 25.5
# IO 18-35 = missing 26.5
# IO 60+ = missing 25.5
# IWTL 18-35 = missing 27.5
# IWTL 60+ = missing 28.5
# TO 18-35 = missing 26.5
# TO 60+ = missing 18.5 (!!!!!)

# chi square test to see if observed drop-off matches expected drop-off (a.k.a. if not infl by icon type or age)
res1 = chisquare([26.5,25.5,27.5,28.5,26.5,18.5], [25.5,25.5,25.5,25.5,25.5,25.5])
# print(res1.statistic, res1.pvalue) # not sig! so it is ~relatively equal distr of data, not effected by anything rlly.

# chi square test to see if finished vs not finished for icon/age have =-ish proportions
table = [
    [39, 47, 39, 40, 38, 37],  # Finished (TO 18-35, 60+; IO...; IWTL)
    [4, 20, 6, 17, 6, 23]      # Not Finished
]

chi2, p, dof, expected = chi2_contingency(table)

# print("chi2 =", chi2)
# print("p-value =", p)

# i must also add that 76 ppl were "mission unfinished" & 77 were "drop off" (didn't even make it to the figma)

# ---------------- VARIANCE/STDS ----------------
# variance per website (speed, mr)
speed_var = df.groupby('Website')['Speed'].std()
mr_var = df.groupby('Website')['Misclick_Rate'].std()

# print('speed std per website: ')
# print(speed_var)
# print('misclick rate std per website: ')
# print(mr_var)

# variance per age groups
speed_age_var = df.groupby(['Website', 'Age'])['Speed'].std()
mr_age_var = df.groupby(['Website', 'Age'])['Misclick_Rate'].std()

# print('speed std per website and age group: ')
# print(speed_age_var)
# print('misclick rate std per website and age group: ')
# print(mr_age_var)

# i also want variance for total speed
total_speed_var = df.groupby('Maze_ID')['Speed'].sum().std()
total_speed_age = df.groupby(['Maze_ID', 'Age'])['Speed'].sum().reset_index()
total_speed_age_var = total_speed_age.groupby('Age')['Speed'].std()

# print('total speed std: ')
# print(total_speed_var)
# print('total speed std per age group: ')
# print(total_speed_age_var)



# ---------------- PLOTS PLOTS PLOTS ----------------
# user_df = df.groupby('Maze_ID').agg({
#     'Speed': 'sum',
#     'Misclick_Rate': 'mean',
#     'Age': 'first'
# }).reset_index()

# for age in user_df['Age'].unique():
#     subset = user_df[user_df['Age'] == age]
#     plt.scatter(
#         subset['Speed'],
#         subset['Misclick_Rate'],
#         label=f'Age {age}'
#     )

# plt.legend()
# plt.xlabel('Speed (s)')
# plt.ylabel('Misclick Rate (%)')
# plt.title('Total Speed vs Average Misclick Rate by Age Group')
# ax = plt.gca()
# ax.xaxis.set_major_locator(tck.MultipleLocator(10))
# ax.yaxis.set_major_locator(tck.MultipleLocator(5))
# plt.xticks(rotation=45)
# plt.plot([0,200], [80,80], color='red', linestyle='--')
# plt.plot([200,200],[80,0], color='red', linestyle='--')
# plt.show()

# user_df = df.groupby('Maze_ID').agg({
#     'Speed': 'sum',
#     'Misclick_Rate': 'median',
#     'Age': 'first'
# }).reset_index()

# for age in user_df['Age'].unique():
#     subset = user_df[user_df['Age'] == age]
#     plt.scatter(
#         subset['Speed'],
#         subset['Misclick_Rate'],
#         label=f'Age {age}'
#     )

# plt.legend()
# plt.xlabel('Speed (s)')
# plt.ylabel('Misclick Rate (%)')
# plt.title('Total Speed vs Median Misclick Rate by Age Group')
# ax = plt.gca()
# ax.xaxis.set_major_locator(tck.MultipleLocator(10))
# ax.yaxis.set_major_locator(tck.MultipleLocator(5))
# plt.xticks(rotation=45)
# plt.show()

# # for avgs
# avg_speed_per_website_plot = avg_speed_per_website.plot(kind='bar', ylabel='Speed (s)', title='Average Speed per Website')
# plt.show()
# avg_mr_per_website_plot = avg_mr_per_website.plot(kind='bar', ylabel='Misclick Rate (%)', title='Average Misclick Rate per Website')
# plt.show()

# avg_speed_per_website_and_age_plot = avg_speed_per_website_and_age.plot(kind='bar', xlabel='Website and Age Group', ylabel='Speed (s)', title='Average Speed per Website and Age Group')
# plt.show()
# avg_mr_per_website_and_age_plot = avg_mr_per_website_and_age.plot(kind='bar', xlabel='Website and Age Group', ylabel='Misclick Rate (%)', title='Average Misclick Rate per Website and Age Group')
# plt.show()

# # for per icon type
# speed_per_icon_type_plot = speed_per_icon_type.plot(kind='bar', xlabel='Icon Type', ylabel='Speed (s)', title='Speed per Icon Type')
# plt.show()
# mr_per_icon_type_plot = mr_per_icon_type.plot(kind='bar', xlabel='Icon Type', ylabel='Misclick Rate (%)', title='Misclick Rate per Icon Type')
# plt.show()

# # CANT DO speed_per_icon_type_and_age_and_website BC UGLY LOLLLL

# # for drop off
# icon_type_distr_percentages_plot = icon_type_distr_percentages.plot(kind='bar', xlabel='Icon Type', ylabel='% Dropped Off', title='Drop-Off Rate per Icon Type')
# plt.show()
# icon_type_distr_per_age_percentages = icon_type_distr_per_age_percentages.plot(kind='bar', xlabel='Icon Type and Age Group', ylabel='% Dropped Off', title='Drop-Off Rate per Icon Type and Age Group')
# plt.show()


# ---------------- HISTOGRAMS HEHE ----------------
# histogram for speeds (per website)

# distr_of_speeds_w1 = df[df['Website'] == 1]['Speed']
# distr_of_speeds_w1_plot = distr_of_speeds_w1.plot(kind='hist', xlabel='Speed (s)', title='Speed Distribution for Website 1')
# plt.show()

# distr_of_speeds_age_w1 = df[df['Website'] == 1].groupby('Age')['Speed']
# distr_of_speeds_age_w1_plot = distr_of_speeds_age_w1.plot(kind='hist', xlabel='Speed (s)', title='Speed Distribution for Website 1 per Age Group', alpha=.5)
# plt.legend()
# plt.show()

# distr_of_speeds_w2 = df[df['Website'] == 2]['Speed']
# distr_of_speeds_w2_plot = distr_of_speeds_w2.plot(kind='hist', xlabel='Speed (s)', title='Speed Distribution for Website 2')
# plt.show()

# distr_of_speeds_age_w2 = df[df['Website'] == 2].groupby('Age')['Speed']
# distr_of_speeds_age_w2_plot = distr_of_speeds_age_w2.plot(kind='hist', xlabel='Speed (s)', title='Speed Distribution for Website 2 per Age Group', alpha=.5)
# plt.legend()
# plt.show()

# distr_of_speeds_w3 = df[df['Website'] == 3]['Speed']
# distr_of_speeds_w3_plot = distr_of_speeds_w3.plot(kind='hist', xlabel='Speed (s)', title='Speed Distribution for Website 3')
# plt.show()

# distr_of_speeds_age_w3 = df[df['Website'] == 3].groupby('Age')['Speed']
# distr_of_speeds_age_w3_plot = distr_of_speeds_age_w3.plot(kind='hist', xlabel='Speed (s)', title='Speed Distribution for Website 3 per Age Group', alpha=.5)
# plt.legend()
# plt.show()

# distr_of_speeds_w4 = df[df['Website'] == 4]['Speed']
# distr_of_speeds_w4_plot = distr_of_speeds_w4.plot(kind='hist', xlabel='Speed (s)', title='Speed Distribution for Website 4')
# plt.show()

# distr_of_speeds_age_w4 = df[df['Website'] == 4].groupby('Age')['Speed']
# distr_of_speeds_age_w4_plot = distr_of_speeds_age_w4.plot(kind='hist', xlabel='Speed (s)', title='Speed Distribution for Website 4 per Age Group', alpha=.5)
# plt.legend()
# plt.show()

# distr_of_speeds_w5 = df[df['Website'] == 5]['Speed']
# distr_of_speeds_w5_plot = distr_of_speeds_w5.plot(kind='hist', xlabel='Speed (s)', title='Speed Distribution for Website 5')
# plt.show()

# distr_of_speeds_age_w5 = df[df['Website'] == 5].groupby('Age')['Speed']
# distr_of_speeds_age_w5_plot = distr_of_speeds_age_w5.plot(kind='hist', xlabel='Speed (s)', title='Speed Distribution for Website 5 per Age Group', alpha=.5)
# plt.legend()
# plt.show()

# distr_of_speeds_w6 = df[df['Website'] == 6]['Speed']
# distr_of_speeds_w6_plot = distr_of_speeds_w6.plot(kind='hist', xlabel='Speed (s)', title='Speed Distribution for Website 6')
# plt.show()

# distr_of_speeds_age_w6 = df[df['Website'] == 6].groupby('Age')['Speed']
# distr_of_speeds_age_w6_plot = distr_of_speeds_age_w6.plot(kind='hist', xlabel='Speed (s)', title='Speed Distribution for Website 6 per Age Group', alpha=.5)
# plt.legend()
# plt.show()

# histogram for misclick rates

# distr_of_mr_w1 = df[df['Website'] == 1]['Misclick_Rate']
# distr_of_mr_w1_plot = distr_of_mr_w1.plot(kind='hist', xlabel='Misclick Rate (%)', title='Misclick Rate for Website 1', weights=np.ones(len(distr_of_mr_w1)) / len(distr_of_mr_w1))
# ax = plt.gca()
# ax.xaxis.set_major_locator(tck.MultipleLocator(5))
# ax.yaxis.set_major_formatter(tck.PercentFormatter(1))
# plt.xticks(rotation=45)
# plt.show()

# distr_of_mr_age_w1 = df[df['Website'] == 1].groupby('Age')['Misclick_Rate']
# distr_of_mr_age_w1_plot= distr_of_mr_age_w1.plot(kind='hist', xlabel='Misclick Rate (%)', title='Misclick Rate Distribution for Website 1 per Age Group', alpha=.5)
# ax = plt.gca()
# ax.xaxis.set_major_locator(tck.MultipleLocator(5))
# plt.xticks(rotation=45)
# plt.legend()
# plt.show()

# distr_of_mr_w2 = df[df['Website'] == 2]['Misclick_Rate']
# distr_of_mr_w2_plot = distr_of_mr_w2.plot(kind='hist', xlabel='Misclick Rate (%)', title='Misclick Rate Distribution for Website 2', weights=np.ones(len(distr_of_mr_w2)) / len(distr_of_mr_w2))
# ax = plt.gca()
# ax.xaxis.set_major_locator(tck.MultipleLocator(5))
# ax.yaxis.set_major_formatter(tck.PercentFormatter(1))
# plt.xticks(rotation=45)
# plt.show()

# distr_of_mr_age_w2 = df[df['Website'] == 2].groupby('Age')['Misclick_Rate']
# distr_of_mr_age_w2_plot = distr_of_mr_age_w2.plot(kind='hist', xlabel='Misclick Rate (%)', title='Misclick Rate Distribution for Website 2 per Age Group', alpha=.5)
# ax = plt.gca()
# ax.xaxis.set_major_locator(tck.MultipleLocator(5))
# plt.xticks(rotation=45)
# plt.legend()
# plt.show()

# distr_of_mr_w3 = df[df['Website'] == 3]['Misclick_Rate']
# distr_of_mr_w3_plot = distr_of_mr_w3.plot(kind='hist', xlabel='Misclick Rate (%)', title='Misclick Rate Distribution for Website 3', weights=np.ones(len(distr_of_mr_w3)) / len(distr_of_mr_w3))
# ax = plt.gca()
# ax.xaxis.set_major_locator(tck.MultipleLocator(5))
# ax.yaxis.set_major_formatter(tck.PercentFormatter(1))
# plt.xticks(rotation=45)
# plt.show()

# distr_of_mr_age_w3 = df[df['Website'] == 3].groupby('Age')['Misclick_Rate']
# distr_of_mr_age_w3_plot = distr_of_mr_age_w3.plot(kind='hist', xlabel='Misclick Rate (%)', title='Misclick Rate Distribution for Website 3 per Age Group', alpha=.5)
# ax = plt.gca()
# ax.xaxis.set_major_locator(tck.MultipleLocator(5))
# plt.xticks(rotation=45)
# plt.legend()
# plt.show()

# distr_of_mr_w4 = df[df['Website'] == 4]['Misclick_Rate']
# distr_of_mr_w4_plot = distr_of_mr_w4.plot(kind='hist', xlabel='Misclick Rate (%)', title='Misclick Rate Distribution for Website 4', weights=np.ones(len(distr_of_mr_w4)) / len(distr_of_mr_w4))
# ax = plt.gca()
# ax.xaxis.set_major_locator(tck.MultipleLocator(5))
# ax.yaxis.set_major_formatter(tck.PercentFormatter(1))
# plt.xticks(rotation=45)
# plt.show()

# distr_of_mr_age_w4 = df[df['Website'] == 4].groupby('Age')['Misclick_Rate']
# distr_of_mr_age_w4_plot = distr_of_mr_age_w4.plot(kind='hist', xlabel='Misclick Rate (%)', title='Misclick Rate Distribution for Website 4 per Age Group', alpha=.5)
# ax = plt.gca()
# ax.xaxis.set_major_locator(tck.MultipleLocator(5))
# plt.xticks(rotation=45)
# plt.legend()
# plt.show()

# distr_of_mr_w5 = df[df['Website'] == 5]['Misclick_Rate']
# distr_of_mr_w5_plot = distr_of_mr_w5.plot(kind='hist', xlabel='Misclick Rate (%)', title='Misclick Rate Distribution for Website 5', weights=np.ones(len(distr_of_mr_w5)) / len(distr_of_mr_w5))
# ax = plt.gca()
# ax.xaxis.set_major_locator(tck.MultipleLocator(5))
# ax.yaxis.set_major_formatter(tck.PercentFormatter(1))
# plt.xticks(rotation=45)
# plt.show()

# distr_of_mr_age_w5 = df[df['Website'] == 5].groupby('Age')['Misclick_Rate']
# distr_of_mr_age_w5_age = distr_of_mr_age_w5.plot(kind='hist', xlabel='Misclick Rate (%)', title='Misclick Rate Distribution for Website 5 per Age Group', alpha=.5)
# ax = plt.gca()
# ax.xaxis.set_major_locator(tck.MultipleLocator(5))
# plt.xticks(rotation=45)
# plt.legend()
# plt.show()

# distr_of_mr_w6 = df[df['Website'] == 6]['Misclick_Rate']
# distr_of_mr_w6_plot = distr_of_mr_w6.plot(kind='hist', xlabel='Misclick Rate (%)', title='Misclick Rate Distribution for Website 6', weights=np.ones(len(distr_of_mr_w6)) / len(distr_of_mr_w6))
# ax = plt.gca()
# ax.xaxis.set_major_locator(tck.MultipleLocator(5))
# ax.yaxis.set_major_formatter(tck.PercentFormatter(1))
# plt.xticks(rotation=45)
# plt.show()

# distr_of_mr_age_w6 = df[df['Website'] == 6].groupby('Age')['Misclick_Rate']
# distr_of_mr_age_w6_plot = distr_of_mr_age_w6.plot(kind='hist', xlabel='Misclick Rate (%)', title='Misclick Rate Distribution for Website 6 per Age Group', alpha=.5)
# ax = plt.gca()
# ax.xaxis.set_major_locator(tck.MultipleLocator(5))
# plt.xticks(rotation=45)
# plt.legend()
# plt.show()

# histogram for total speed

# distr_of_total_speed = df.groupby('Maze_ID')['Speed'].sum()
# distr_of_total_speed_plot = distr_of_total_speed.plot(kind='hist', xlabel='Speed (s)', title='Total Speed Across All Websites')
# plt.show()

# distr_of_total_speed_age = df.groupby(['Maze_ID', 'Age'])['Speed'].sum().groupby('Age')
# distr_of_total_speed_age_plot = distr_of_total_speed_age.plot(kind='hist', xlabel='Speed (s)', title='Total Speed Across All Websites', alpha=.5)
# plt.legend()
# # plt.show()

# distr_of_avg_speed = df['Speed'].dropna()
# distr_of_avg_speed_plot = distr_of_avg_speed.plot(kind='hist', xlabel='Speed (s)', title='Average Speed Across All Websites', weights=np.ones(len(distr_of_avg_speed)) / len(distr_of_avg_speed))
# ax = plt.gca()
# ax.xaxis.set_major_locator(tck.MultipleLocator(10))
# ax.yaxis.set_major_formatter(tck.PercentFormatter(1))
# ax.yaxis.set_major_locator(tck.MultipleLocator(.05))
# plt.xticks(rotation=45)
# plt.show()

# # histogram for total mr

# distr_of_avg_mr = df['Misclick_Rate'].dropna()
# distr_of_avg_mr_plot = distr_of_avg_mr.plot(kind='hist', xlabel='Misclick Rate (%)', title='Average Misclick Rate Across All Websites', weights=np.ones(len(distr_of_avg_mr)) / len(distr_of_avg_mr))
# ax = plt.gca()
# ax.xaxis.set_major_locator(tck.MultipleLocator(5))
# ax.yaxis.set_major_formatter(tck.PercentFormatter(1))
# ax.yaxis.set_major_locator(tck.MultipleLocator(.05))
# plt.xticks(rotation=45)
# plt.show()