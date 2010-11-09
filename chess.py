#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
import matplotlib.mlab as mlab
import matplotlib.ticker as ticker
import random

def sample_chess():
    size = 8

    x = random.random()
    y = random.random()

    xsquare = int(x * size)
    ysquare = int(y * size)

    label = (xsquare + ysquare) % 2

    return (label, (x, y));

def sample_ring():
    size = 4

    x = random.random()
    y = random.random()

    dist = math.sqrt(x*x + y*y)

    idist = int(dist * size)

    label = idist % 2

    return (label, (x, y))

def doplot(size, npoints, gen, name):
    points = [gen() for x in xrange(0, npoints)];

    ones = [point for point in points if point[0] == 1]
    zeros = [point for point in points if point[0] == 0]

    x1 = [point[1][0] for point in ones]
    y1 = [point[1][1] for point in ones]
    l1 = [point[0]    for point in ones]

    x0 = [point[1][0] for point in zeros]
    y0 = [point[1][1] for point in zeros]
    l0 = [point[0]    for point in zeros]

    plt.clf()

    plt.figure(1, figsize=(8,8))
    plt.hold(True)
    plt.title('Mystery distribution; %d points' % npoints)
    plt.ylabel('x')
    plt.xlabel('y')

    plt.plot(x0, y0, 'rx');
    plt.plot(x1, y1, 'bx');


    #plt.axes().autoscale_view(tight=True, scaley=False)
    #plt.axes().yaxis.grid(which="major", linestyle="-");
    #plt.axes().yaxis.grid(which="minor");
    #plt.axes().yaxis.set_minor_locator(ticker.LogLocator(subs=[0.2,0.3,0.4,1.0]))
    #plt.legend(loc='lower left')

    #plt.show()

    plt.savefig('%s-%d.pdf' % (name, npoints), transparent=True)



doplot(8, 10, sample_chess, "chess-8x8")
doplot(8, 100, sample_chess, "chess-8x8")
doplot(8, 1000, sample_chess, "chess-8x8")
doplot(8, 10000), sample_chess, "chess-8x8")

doplot(8, 10, sample_ring, "ring-4")
doplot(8, 100, sample_ring, "ring-4")
doplot(8, 1000, sample_ring, "ring-4")
doplot(8, 10000), sample_ring, "ring-4")


