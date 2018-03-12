
# coding: utf-8

# In[5]:


a = int(input('请输入小于1000的整数：'))
c = a
b = [] #存储因数
i = 2
if a == 1:
    print('1 = 1')
else:
    while i <= a:
        if a%i == 0:
            b.append(i)
            a = a/i
        else:
            i+=1
    print(c,'=','x'.join([str(i) for i in b]))

