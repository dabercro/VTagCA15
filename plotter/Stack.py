#!/usr/bin/env python

from CrombieTools.PlotTools.PlotStack import *
from CrombieTools.LoadConfig import cuts
import os

SetupFromEnv()

plotter.AddDataFile('MET.root')
plotter.SetLegendLocation(plotter.kUpper, plotter.kRight, 0.3, 0.4)
plotter.SetMinLegendFrac(0.03)

plotter.SetRatioMinMax(0.0, 2.0)

def SetupArgs():
    return [
        ['dRfj1Isob', 20, 0.0, 4.0, '#Delta R(CA15, AK4 b)', 'Events/Bin'],
        ['fj1MSD_corr', 25, 0.0, 250.0, 'm_{SD} [GeV]', 'Events/Bin'],
        ]

if __name__ == '__main__':
    MakePlots(cuts.categories, cuts.regions, SetupArgs(), parallel=False)
