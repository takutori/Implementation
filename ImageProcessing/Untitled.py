
# coding: utf-8

# In[6]:


import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
import numpy as np


# In[33]:


Hirate1 = np.array(Image.open('Hirate1.jpg'))
Hirate2 = np.array(Image.open('Hirate2.jpg'))
Hirate3 = np.array(Image.open('Hirate3.jpg'))


# In[19]:


Hirate3.shape


# In[11]:


plt.imshow(Hirate1/np.mean(Hirate1))


# In[18]:


plt.imshow(Hirate2[200:600,200:600,:]+Hirate1)


# In[34]:


plt.imshow(Hirate3)


# In[25]:


get_ipython().run_line_magic('matplotlib', 'inline')
from ipywidgets import RangeWidget, RadioWidget

import matplotlib.pyplot as plt
from ipywidgets import interact
import numpy as np

def f(k):
    x = np.linspace(0, 10, num=1000)
    y = np.sin(k*x)
    plt.plot(x, y)
    plt.show()

slider_k = (0.0,5.0,0.1)
interact(f, k= slider_k)


# In[12]:


from bokeh.io import output_notebook
from bokeh.io import show
output_notebook()


# In[7]:


from ipywidgets import HTML


# In[10]:


from ipywidgets import IntSlider
slider = IntSlider(value=50)#valueの値は可変
slider


# In[11]:


text = HTML("スライダーの値は{}".format(slider.value))
text


# In[16]:


from ipywidgets import IntSlider
from ipywidgets.embed import embed_minimal_html

slider = IntSlider(value=40)
embed_minimal_html('export.html', views=[slider], title='Widgets export')


# In[19]:


type(slider)


# In[34]:


import numpy as np
import nbinteract as nbi
nbi.publish('SamLau95/nbinteract-image/master','Untitled.ipynb')
def normal(mean, sd):
    return np.random.normal(mean, sd, 1000)
# Pass in the ‘normal‘ function and let user change mean and sd.
# Whenever the user interacts with the sliders, the
# ‘normal‘ function is called and the returned data are plotted.
nbi.hist(normal, mean=(0, 10), sd=(0, 2.0))


# In[33]:


get_ipython().run_line_magic('matplotlib', 'inline')
from ipywidgets import interactive
import matplotlib.pyplot as plt
import numpy as np

def f(m, b):
    plt.figure(2)
    x = np.linspace(-10, 10, num=1000)
    plt.plot(x, m * x + b)
    plt.ylim(-5, 5)
    plt.show()

interactive_plot = interactive(f, m=(-2.0, 2.0), b=(-3, 3, 0.5))
output = interactive_plot.children[-1]
output.layout.height = '350px'
interactive_plot

