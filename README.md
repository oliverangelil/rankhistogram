# rankhistogram
Python function that takes model data, obs data, and a boolean mask to generate a rank histogram 

###Example
```
import numpy as np
from ranky import rankz

# generate dummy data
obs = np.random.randn(10, 40, 40)
ensemble = np.random.randn(20, 10, 40, 40)
mask = np.random.randint(0, 2, (10, 40, 40))

# feed into rankz function
result = rankz(obs, ensemble, mask)

# plot histogram
plt.bar(range(1,ensemble.shape[0]+2), result[0])

# view histogram
plt.show()
``` 
