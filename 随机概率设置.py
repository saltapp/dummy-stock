
# coding: utf-8

# In[51]:


import random
def random_index(rate):
    """随机变量的概率函数"""
    #
    # 参数rate为list<int>
    #
    start = 0
    randnum = random.randint(1, sum(rate))
    print('randnum=' + str(randnum))
    for index, item in enumerate(rate):
        print(str(index) + '-----' + str(item))        
        start += item
        print('start=' + str(start))
        print('randnum=' + str(randnum) + '??' + 'start=' + str(start))
        if randnum <= start:
            print('index=' + str(index))
            print('---------------------------------------------------------------------------')
            break
    return index

def main():
    arr = ['red', 'green', 'blue']
    rate = [45, 30, 25]

    red_times = 0
    green_times = 0
    blue_times = 0
    i = 0
    for i in range(10000):
        index = random_index(rate)
        if arr[index] == 'red':
            red_times += 1
            print (red_times, green_times, blue_times)
            print('==================================================================================')
            continue
        if arr[index] == 'green':
            green_times += 1
            print (red_times, green_times, blue_times)
            print('==================================================================================')
            continue
        if arr[index] == 'blue':
            blue_times += 1
            print (red_times, green_times, blue_times)
            print('==================================================================================')
            continue
    print(i)
    print (red_times, green_times, blue_times)
    print (red_times+ green_times+ blue_times)


# In[52]:

main()


# In[53]:

main()


# In[ ]:



