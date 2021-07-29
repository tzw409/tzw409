#created by Nisha Agrawal
#Enter integer no:
def my_multi(time):
 nums=[1]
 s=1
 for i in range(time-1):
  s=s*10+1
  nums.append(s)
 return nums
line=int(input())
mul=my_multi(line)
res=[mul[i]**2 for i in range(line)]
for i in range(line):        print(mul[i],"*",mul[i],"=",res[i])
print("☆"*(35))
print("Created by Nisha Agrawal")