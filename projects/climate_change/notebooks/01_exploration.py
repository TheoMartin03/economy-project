import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import numpy as np
    import polars as pl
    import matplotlib.pyplot as plt
    import seaborn as sns
    import plotly.express as px
    import sklearn

    print("Environment working!")
    return


if __name__ == "__main__":
    app.run()
