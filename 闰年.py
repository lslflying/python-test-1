
# coding: utf-8

# In[8]:


a = int(input('请输入4位数年份：'))
if a < 1000:
    print('输入错误！')
else:
    if a % 400 == 0:
        print('%d是闰年。'% a)
    else:
        if a % 4 == 0 and a % 100 != 0:
            print('%d是闰年。'% a)
        else:
            print('%d不是闰年。'%a)

