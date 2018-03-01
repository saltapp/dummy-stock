
# coding: utf-8

# In[79]:


import random
import math
def random_index(rate):
    """随机变量的概率函数"""
    #
    # 参数rate为list<int>
    #
    start = 0
    randnum = random.uniform(1, sum(rate))
    for index, item in enumerate(rate):       
        start += item
        if randnum <= start:
            break
    return index


def getPB(market, net):
    return market/net

#2018-02-26 completed
#to be modified 
def generateOffset(pb):
    offset = -(1.5625 * pow((pb-5),3))
    if(offset > 100.0):
        offset = 100.0
    if(offset < -100.0):
        offset = -100.0
    return offset

#to do function 2018-02-26
# www.symbolab.com get process of integral
def getReverseProbability(offset):
    sumProbability = (2/3) * pow(100,3/2)   # (2/3) * pow(x,3/2)
    offsetProbability = (2/3) * pow(offset,3/2)
    randomP = random.uniform(0, sumProbability)
    if(randomP <= offset):
        return True
    else:
        return False

def generateGrowthPoints(start, end):
    growthPoints = []
    for i in range(start, end+1, 1):
        growthPoints.append(i)
    return growthPoints            #growthPoints = [-100,-99,...,0,1,...100]

def generateProbabilityPoints(growthPoints,offset):
    probabilityPoints = []
    for point in growthPoints:
        probabilityPoints.append(-pow((point-offset),2) + 10000)
    return probabilityPoints

def updown(offset):
    if(offset > 0):
        start = math.ceil(-100 + offset)
        end = 100
    if(offset < 0):
        start = -100
        end = math.floor(100 + offset)
    if(offset == 0):
        start = -100
        end = 100
    growthPoints = generateGrowthPoints(start, end)
    probabilityPoints = generateProbabilityPoints(growthPoints, offset)
    index = random_index(probabilityPoints)
    return round(growthPoints[index]/1000,3)


# In[80]:

market = 500
net = 100
score_history = []
offset = 0
for i in range(120):
    if(i % 12 == 0):
        net *= 1.15
    market *= (1+updown(offset))
    score_history.append(round(market,2))
    pb = getPB(market, net)
    offset = generateOffset(pb)
    print(offset)
    reverseFlag = getReverseProbability(offset)
    if(reverseFlag == True):
        offset = 0 - offset


print(score_history)


# In[81]:






#------以下为策略部分-----------------------------------
money = 0       #每个月固定投10000
money_noaction = 0
i = 0
money_result = []
money_noaction_result = []
for i in range(0,len(score_history)):
    if i - 1 >= 0:
        rate = (score_history[i] - score_history[i-1]) / score_history[i-1]
        money = money * (1 + rate)
        money += 10000
        money_noaction += 10000
    else:
        money += 10000
        money_noaction += 10000
    money_result.append(round(money,2))
    money_noaction_result.append(money_noaction)
# print(round(money,1))
# print(round(money_noaction,1))

# print(money_result)
# print(money_noaction_result)


# In[82]:

money = 0   #每个月在最近三个月为跌的时候投一万
money_noaction = 0
money_out = 0
money_result = []
money_noaction_result = []
for i in range(0,len(score_history)):
    if i -3 >= 0     and (score_history[i] - score_history[i-1]) / score_history[i-1] < 0     and (score_history[i-1] - score_history[i-2]) / score_history[i-2] < 0     and (score_history[i-2] - score_history[i-3]) / score_history[i-3] < 0:
        rate = (score_history[i] - score_history[i-1]) / score_history[i-1]
        money = money * (1 + rate)
        money += 10000
        money_noaction += 10000
    else:
        money_out += 10000
        money_noaction += 10000
    money_result.append(round(money+money_out,2))

# print(round(money+money_out,2))
# print(round(money_noaction,2))

# print(money_result)


# In[83]:

money = 0    #每个月在最近三个月为跌的时候投一万和剩余的钱
money_noaction = 0
money_out = 0
money_result = []
money_noaction_result = []
rate = 0
for i in range(0,len(score_history)):
    money = money * (1 + rate)
    if i -3 >= 0     and (score_history[i] - score_history[i-1]) / score_history[i-1] < 0     and (score_history[i-1] - score_history[i-2]) / score_history[i-2] < 0     and (score_history[i-2] - score_history[i-3]) / score_history[i-3] < 0:
        rate = (score_history[i] - score_history[i-1]) / score_history[i-1]
        money += 10000
        money += money_out
        money_out = 0
    else:
        money_out += 10000
    money_result.append(round(money+money_out,2)) 
    money_noaction += 10000
    
    
# print(round(money+money_out,2))
# print(round(money_noaction,2))

# print(money_result)


# In[ ]:




# In[ ]:



