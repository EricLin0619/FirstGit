TownNumber,SiteNumber,scope=map(int,input().split())
arr=[[0]*3 for i in range(TownNumber)]  #3行的二維陣列
people=[0]*TownNumber # 存放每個城鎮周圍人數的總和
number_arr=[0]*SiteNumber #存放被包含的城鎮編號
total=0 #總覆蓋人數

for q in range(TownNumber):
    x,y,z=map(int,input().split())
    arr[q][0]=x
    arr[q][1]=y
    arr[q][2]=z

times=0 #計數器
while times<SiteNumber:
    for a in range(TownNumber):
        for b in range(TownNumber):
            distance=((arr[a][0]-arr[b][0])**2+(arr[a][1]-arr[b][1])**2)**0.5 #算出兩城鎮的距離
            if distance<=scope:
                people[a]=people[a]+arr[b][2]  #把距離小於scope的城鎮的人數加起來

    max=0 #覆蓋的人數
    number=0 #最多人城鎮編號
    for c in range(TownNumber):
        if people[c]>max:
            max=people[c]
            number=c
            

    number_arr[times]=number+1

    for b in range(TownNumber):
        distance=((arr[number][0]-arr[b][0])**2+(arr[number][1]-arr[b][1])**2)**0.5 #算出兩城鎮的距離
        if distance<=scope:
            total=total+arr[b][2]
            arr[b][2]=0
    times+=1
    people=[0]*TownNumber

for g in range(SiteNumber):
   print(number_arr[g])
print(total)