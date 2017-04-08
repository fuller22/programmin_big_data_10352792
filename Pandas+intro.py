
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd


# In[2]:

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])


# In[3]:

s


# In[4]:

s.index


# In[6]:

pd.Series(np.random.randn(5))


# In[7]:

d = {'a' : 0., 'b' : 1., 'c' : 2.}

pd.Series(d)
# In[8]:

d


# In[9]:

pd.Series(d)


# In[10]:

pd.Series(d, index=['b', 'c', 'd', 'a'])


# In[11]:

s


# In[12]:

s(0)


# In[13]:

s[0]


# ### 

# In[14]:

s[:3]


# In[15]:

s[s>s.median()]


# In[16]:

s[[4,3,1]]


# In[17]:

nd.exp[s]


# In[18]:

nd.exp(s)


# In[19]:

np.exp(s)


# In[20]:

s['a']


# In[21]:

s['e']= 12


# In[22]:

s


# In[23]:

'f'  in s


# In[24]:

if 'f' in s
    s['f']


# In[25]:

if 'f' in s:
    s['f']


# In[26]:

if 'e' in s :
        print 'e'


# In[27]:

if 'e' in s :
        print s['e']


# In[28]:

s.get('f', nan)


# In[29]:

s.get('f', np.nan)


# In[30]:

s+s


# In[31]:

s['f'] = 0


# In[32]:

s


# In[33]:

s[1:]+s[:-1]


# In[34]:

d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
      'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}


# In[35]:

d


# In[36]:

df = pd.DataFrame(d)


# In[37]:

df


# In[38]:

pd.DataFrame(d, index=['d', 'b', 'a'])


# In[39]:

pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three'])


# In[40]:

df.index


# In[41]:

df.columns


# In[42]:

d = {'one' : [1., 2., 3., 4.],
     'two' : [4., 3., 2., 1.]}


# In[43]:

d


# In[44]:

pd.Dataframe(d)


# In[45]:

pd.Dataframe(d)


# In[46]:

pd.DataFrame(d)


# In[47]:

pd.DataFrame(d, index=['a', 'b', 'c', 'd'])


# In[48]:

data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])


# In[49]:

data[:] = [(1,2.,'Hello'), (2,3.,"World")]


# In[50]:

pd.DataFrame(data)


# In[51]:

data


# In[52]:

data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])


# In[53]:

data


# In[54]:

data[:] = [(1,2.,'Hello'), (2,3.,"World")]


# In[55]:

pd.DataFrame(data)


# In[56]:

pd.DataFrame(data, index=['first', 'second'])


# In[57]:

pd.DataFrame(data, columns=['C', 'A', 'B'])


# In[58]:

data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]


# In[59]:

pd.DataFrame(data2)


# In[60]:

pd.DataFrame(data2, index=['first', 'second'])


# In[61]:

pd.DataFrame(data2, columns=['a', 'b'])


# In[62]:

df


# In[63]:

df['one']


# In[64]:

df['three'] = df['one'] * df['two']


# In[65]:

df


# In[66]:

df['flag'] = df['one'] > 2


# In[67]:

df


# In[68]:

del df['two']


# In[69]:

three = df.pop('three')


# In[70]:

three


# In[71]:

df


# In[72]:

df['foo']= 'bar'


# In[73]:

df


# In[74]:

df['one_trunc'] = df['one'][:2]


# In[75]:

df


# In[76]:

df.insert(1, 'bar', df['one'])


# In[77]:

df


# In[ ]:



