from matplotlib import pyplot as plt
from matplotlib import rc, rcParams
from cycler import cycler
params = {
  "lines.linewidth": 2.0,
  "axes.edgecolor": "#bcbcbc",
  "patch.linewidth": 0.5,
  "legend.fancybox": True,
 'axes.prop_cycle':cycler('color', [
    "#348ABD",
    "#A60628",
    "#7A68A6",
    "#467821",
    "#CF4457",
    "#188487",
    "#E24A33"
  ]),
  "axes.facecolor": "#eeeeee",
  "axes.labelsize": "large",
  "axes.grid": False,
  "patch.edgecolor": "#eeeeee",
  "axes.titlesize": "x-large",
  "text.usetex":True,
  'font.family': 'serif',
  "font.serif": [],
  "figure.dpi": 300,
    'font.size': 12
}

rcParams.update(params)