import sys
import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('background', help='file with background data')
parser.add_argument('signal', help='file with signal data')

args = parser.parse_args()

print(args)

# load data files
x_b,y_b = np.loadtxt(args.background, unpack=True)
x_s,y_s = np.loadtxt(args.signal, unpack=True)

mcd_signal = str(args.signal).replace('txt', 'mcd')
mcd_background = str(args.background).replace('txt', 'mcd')

time_background, time_signal = 0,0
for line in open(mcd_background):
    if line.startswith('LIVETIME'):
        print(line)
        time_background = float(line.split()[1])
        break
for line in open(mcd_signal):
    if line.startswith('LIVETIME'):
        print(line)
        time_signal = float(line.split()[1])
        break

#normalize the background to signal time
y_b = np.asarray([round(x) for x in (y_b*time_signal/time_background)])

fig, (ax_s, ax_b, ax_diff) = plt.subplots(nrows=3)


ax_s.plot(x_s,y_s)
ax_s.set(xlabel = "channel", ylabel = "Counts per channel", title = "signal spectrum")
ax_s.grid()

ax_b.plot(x_b,y_b)
ax_b.set(xlabel = "channel", ylabel = "Counts per channel", title = "background spectrum")
ax_b.grid()

ax_diff.plot(x_b,y_s - y_b)
ax_diff.set(xlabel = "channel", ylabel = "Counts per channel", title = "difference spectrum")
ax_diff.grid()

plt.show()




