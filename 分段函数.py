
# coding: utf-8

# In[3]:


a = float(input('please enter the number:'))
if a < 0:
    print('y = 0')
elif 0 <= a < 5:
    print('y = %.2f'%a)
elif 5 <= a <10:
    c = 3*a - 5
    print('y = %.2f'%c)
elif 10 <= a <20:
    c = 0.5*a - 2
    print('y = %.2f'%c)
elif a >= 20:
    print('y = 0')

