import numpy as np
mean = 12
stdeviation = 19
x = np.random.normal(12,19,8500)

#standardizing the values 

z = (x-mean)/stdeviation

print("The value of z score is: ",z)

count1 = 0
count2 = 0
count3 = 0
for i in z:
    if(5.825<=i<=18.175):
        count1+=1
    if(2.5<=i<=21.5):
        count2+=1
    if (6.775<=i<=17.225):
        count3+=1


percentage1 = (count1/8500)*100
print("The percentage of z present in first range is : ",percentage1)
percentage2 = (count2/8500)*100
print("The percentage of z present in second range is : ",percentage2)
percentage3 = (count3/8500)*100
print("The percentage of z present in third range is : ",percentage3)
