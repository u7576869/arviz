"""
Separation Plot
===============
_gallery_category: Model Checking
"""
import matplotlib.pyplot as plt

import arviz as az

az.style.use("arviz-doc")

idata = az.load_arviz_data("classification10d")

az.plot_separation(idata=idata, y="outcome", y_hat="outcome", figsize=(8, 1))

plt.show()
