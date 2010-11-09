#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
import matplotlib.mlab as mlab
import matplotlib.ticker as ticker
import random
import math

def sample_chess(size):
    x = random.random()
    y = random.random()

    xsquare = int(x * size)
    ysquare = int(y * size)

    label = (xsquare + ysquare) % 2

    return (label, (x, y));

def sample_chess2(size):
    x = random.random()
    y = random.random()

    xsquare = int(x * size)
    ysquare = int(y * size)

    label = (xsquare + ysquare) % 2

    return (label, ((x * size) % 2, (y * size) % 2))

def sample_ring(size):
    x = random.random()
    y = random.random()

    dist1 = math.sqrt(x*x + y*y)
    dist2 = math.sqrt((1-x)*(1-x) + (1-y)*(1-y))

    idist1 = int(dist1 * size)
    idist2 = int(dist2 * size)

    label = (idist1 + idist2) % 2

    return (label, (x, y))

def sample_ring2(size):
    x = random.random()
    y = random.random()

    dist1 = math.sqrt(x*x + y*y)
    dist2 = math.sqrt((1-x)*(1-x) + (1-y)*(1-y))

    idist1 = int(dist1 * size)
    idist2 = int(dist2 * size)

    label = (idist1 + idist2) % 2

    return (label, (dist1, dist2))

def sample_ring3(size):
    x = random.random()
    y = random.random()

    dist1 = math.sqrt(x*x + y*y)
    dist2 = math.sqrt((1-x)*(1-x) + (1-y)*(1-y))

    idist1 = int(dist1 * size)
    idist2 = int(dist2 * size)

    label = (idist1 + idist2) % 2

    return (label, ((dist1 * size) % 2, (dist2 * size) % 2))

def doplot(size, npoints, gen, name, title, labelx="x", labely="y"):
    points = [gen(size) for x in xrange(0, npoints)];

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
    plt.title('%s; %d points' % (title, npoints))
    plt.ylabel(labelx)
    plt.xlabel(labely)

    plt.plot(x0, y0, 'rx');
    plt.plot(x1, y1, 'b+');


    #plt.axes().autoscale_view(tight=True, scaley=False)
    #plt.axes().yaxis.grid(which="major", linestyle="-");
    #plt.axes().yaxis.grid(which="minor");
    #plt.axes().yaxis.set_minor_locator(ticker.LogLocator(subs=[0.2,0.3,0.4,1.0]))
    #plt.legend(loc='lower left')

    #plt.show()

    plt.savefig('%s-%d.pdf' % (name, npoints), transparent=True)


doplot(8, 10, sample_chess, "chess-8x8", "Mystery distribution A")
doplot(8, 100, sample_chess, "chess-8x8", "Mystery distribution A")
doplot(8, 1000, sample_chess, "chess-8x8", "Mystery distribution A")
doplot(8, 10000, sample_chess, "chess-8x8", "Mystery distribution A")
doplot(8, 1000, sample_chess2, "chess-8x8-tr",
       "Mystery distribution A transformed", "$8x\  \mathrm{mod}\ 2$", "$8y\ \mathrm{mod}\ 2$")

doplot(8, 10, sample_ring, "ring-8", "Mystery distribution B")
doplot(8, 100, sample_ring, "ring-8", "Mystery distribution B")
doplot(8, 1000, sample_ring, "ring-8", "Mystery distribution B")
doplot(8, 10000, sample_ring, "ring-8", "Mystery distribution B")

doplot(8, 1000, sample_ring2, "ring-8-tr",
       "Mystery distribution B transformed", "$\sqrt{x^2 + y^2}$", "$\sqrt{(1-x)^2 + (1-y)^2}$")

doplot(8, 1000, sample_ring3, "ring-8-tr2",
       "Mystery distribution B transformed", "$8\sqrt{x^2 + y^2}\ \mathrm{mod}\ 2$", "$\sqrt{(1-x)^2 + (1-y)^2}\ \mathrm{mod}\ 2$")


