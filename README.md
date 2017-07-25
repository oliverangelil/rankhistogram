# rankhistogram
Python function that takes model data, obs data, and a boolean mask to generate a rank histogram. Ranks overwhich values are tied (often occurs for rainfall of 0mm for example) are asigned a random rank. A 2001 paper by Thomas Hamil that describes rank histograms is [here](http://journals.ametsoc.org/doi/pdf/10.1175/1520-0493%282001%29129%3C0550%3AIORHFV%3E2.0.CO%3B2).

### Example
```
import numpy as np
from ranky import rankz
import matplotlib.pyplot as plt

# generate dummy data with 10 timesteps, 40 lat and lon grid cells, and 20 ensemble members. 
obs = np.random.randn(10, 40, 40)
ensemble = np.random.randn(20, 10, 40, 40)
mask = np.random.randint(0, 2, (10, 40, 40)) #masked where 0/false.

# feed into rankz function
result = rankz(obs, ensemble, mask)

# plot histogram
plt.bar(range(1,ensemble.shape[0]+2), result[0])

# view histogram
plt.show()
``` 
Dimensions for "obs" can be anything. Dimensions for "mask" must be identical to "obs".
