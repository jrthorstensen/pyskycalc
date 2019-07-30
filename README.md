# pyskycalc

# Deprecated -- see thorsky package 

Please go to  https://github.com/jrthorstensen/thorsky instead, in which an updated and better-documented version of this software is packaged properly for easy installation. 

*************
This is the old description, mostly valid: 

Time-and-the-sky routines for astronomers, built mostly on astropy and including a GUI interface.

Copyright 2018 by John Thorstensen.  Distributed under a BSD-style 3-clause license.

This runs under Python 3 and obviously requires a recent astropy, numpy, and so on. The jupyter notebook should give a good idea of the functionality available.  The basic idea is to integrate ```astropy.coordinates``` and ```astropy.Time``` to facilitate common time-and-the-sky calculations. 

The modules here underly a program '''pyskycalc3''', which is a GUI interface using these routines very similar to the author's JSkyCalc; the GUI is written in tkinter (formerly capitalized as Tkinter in python 2.7).  It has an incomplete interface to ds9 that requires the XPA interface, which is available from the same site as ds9.  

This is very much a work in progress, but it should be useful already.  
