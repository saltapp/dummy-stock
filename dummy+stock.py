
# coding: utf-8

# In[79]:


import random
def random_index(rate):
    """随机变量的概率函数"""
    #
    # 参数rate为list<int>
    #
    start = 0
    randnum = random.randint(1, sum(rate))
    for index, item in enumerate(rate):       
        start += item
        if randnum <= start:
            break
    return index


def getPB(market, net):
    return market/net

#to do function
def generateOffset():



def generateGrowthPoints():
    growthPoints = []
    for i in range(-100,101,1):
        growthPoints.append(i)
    return growthPoints

def generateProbabilityPoints(growthPoints,offset):
    probabilityPoints = []
    for point in growthPoints:
        probabilityPoints.append(-pow((point-offset),2) + 10000)
    return probabilityPoints

def updown():
    growthPoints = generateGrowthPoints()
    probabilityPoints = generateProbabilityPoints(growthPoints)
    index = random_index(probabilityPoints)
    return round(growthPoints[index]/1000,3)


# In[80]:

score = 100
score_history = []
for i in range(100):
    score *= (1+updown())
    score_history.append(round(score,2))

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



