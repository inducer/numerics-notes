import marimo

__generated_with = "0.20.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Mappings of the Complex Plane

    Copyright (C) 2020 Andreas Kloeckner
    <details markdown="1">
    <summary>MIT License</summary>
    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
    </details>
    """)
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    import numpy as np
    import numpy.linalg as la

    return np, plt


@app.cell
def _(mo):
    alpha = mo.ui.slider(start=0, stop=1, label="Blend factor", 
                         value=0, step=0.01, full_width=True)
    return (alpha,)


@app.cell
def _(np):
    re, im = np.mgrid[-1:1:20j, -1:1:20j]
    z = re+1j*im
    return (z,)


@app.cell
def _(alpha, mo, plt, z):
    #f = z**2
    #f = z**3
    f = z**4
    #f = 1/z
    #f = 1/(z-0.2)

    blend = (1-alpha.value)*z + alpha.value*f

    cmap = plt.cm.viridis
    x = blend.real
    y = blend.imag
    n = x.shape[0]
    plt.figure(figsize=(6, 6))
    ax = plt.gca()
    for i in range(n):
        c = cmap(i / (n - 1))
        ax.plot(x[i, :], y[i, :], color=c, lw=0.9)
        ax.plot(x[:, i], y[:, i], color=cmap(1 - i / (n - 1)), lw=0.9, alpha=0.7)

    ax.set_aspect("equal")

    mo.vstack((alpha, plt.gca()))
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
