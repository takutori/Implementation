import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(1000)
y = np.random.randn(1000)
data = np.array([x,y])
np.save('../../dataset/py_study/newdata',data)
