"""
Ridgeplot
=========
"""
import arviz as az

rugby_data = az.load_arviz_data("rugby")
ax = az.plot_forest_kwargs(
    rugby_data,
    kind="ridgeplot",
    var_names=["defs"],
    linewidth=4,
    combined=True,
    ridgeplot_overlap=1.5,
    colors="blue",
    figsize=(9, 4),
    backend="bokeh",
    alternate_row_shading=False
)
