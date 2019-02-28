# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data=np.genfromtxt(path,delimiter=",", skip_header=1)
census=np.concatenate((data,new_record))


# --------------
#Code starts here
age=np.array(census[:,0],dtype='int16')
max_age=max(age)
min_age=min(age)
age_mean=np.mean(age)
age_std=np.std(age)
print(max_age,min_age,age_mean,age_std)



# --------------
#Code starts here
race=census[:,2]
race_0=census[np.where(race==0)]
race_1=census[np.where(race==1)]
race_2=census[np.where(race==2)]
race_3=census[np.where(race==3)]
race_4=census[np.where(race==4)]

len_0=race_0[:,2].size
len_1=race_1[:,2].size
len_2=race_2[:,2].size
len_3=race_3[:,2].size
len_4=race_4[:,2].size

print(len_0)
len_1
len_2
len_3
len_4

min_race=min(len_0,len_1,len_2,len_3,len_4)
if len_0==min_race:
    minority_race=0
if len_1==min_race:
    minority_race=1
if len_2==min_race:
    minority_race=2
if len_3==min_race:
    minority_race=3
if len_4==min_race:
    minority_race=4



# --------------
#Code starts here
senior_citizens=census[census[:,0]>60]
working_hours_sum=senior_citizens[:,6].sum()
senior_citizens_len=senior_citizens[:,6].size
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)




# --------------
#Code starts here
high=census[census[:,1]>10]
low=census[census[:,1]<=10]
avg_pay_high=np.mean(high[:,7])
avg_pay_low=np.mean(low[:,7])
avg_pay_high>avg_pay_low


