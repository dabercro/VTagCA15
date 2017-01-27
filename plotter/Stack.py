#!/usr/bin/env python

from CrombieTools.PlotTools.PlotStack import *
from CrombieTools.LoadConfig import cuts
import os

overwrite = int(os.environ.get('OW', 1))

SetupFromEnv()

plotter.AddDataFile('MET.root')
plotter.SetMinLegendFrac(0.03)

plotter.SetRatioMinMax(0.0, 2.0)

def SetupArgs_RightLegend():
    return [
        ['dRfj1Isob', 45, 0.0, 4.5, '#Delta R(CA15, AK4 b)'],
        ['fj1Pt', 30, 200.0, 800.0, 'p_{T} [GeV]'],
        ['npv', 50, 0, 50, 'NPV'],
        ['pfmet', 30, 0, 600.0, 'MET [GeV]'],
        ['pfmetnomu', 30, 0, 600.0, 'Recoil [GeV]'],
        ['fj1MaxCSV', 20, 0, 1.0, 'Maximum CSV'],
        ['fj1MinCSV', 20, 0, 1.0, 'Minimum CSV'],
        ['fj1IsMatched', 4, -1, 3, 'Is Top Matched'],
        ['fj1IsWMatched', 4, -1, 3, 'Is W Matched'],
        ['fj1Tau21SD', 20, 0, 1.0, '#tau_{2}/#tau_{1}'],
        ['fj1Tau21', 20, 0, 1.0, '#tau_{2}/#tau_{1}'],
        ['puppimet', 30, 0, 600.0, 'PUPPI MET [GeV]'],
        ['jet1CSV', 20, 0, 1.0, 'Jet 1 CSV'],
        ['jet2CSV', 20, 0, 1.0, 'Jet 2 CSV'],
        ['isojet1CSV', 20, 0, 1.0, 'Jet 1 CSV'],
        ['isojet2CSV', 20, 0, 1.0, 'Jet 2 CSV'],
        [{'var_name': 'looseB'}, 'Sum$(jetPt>30 && jetIso && jetCSV>0.605)', 5, 0, 5, 'Number of Loose B'],
        [{'var_name': 'medB'}, 'Sum$(jetPt>30 && jetIso && jetCSV>0.89)', 5, 0, 5, 'Number of Medium B'],
        ['fj1MSD_corr', 25, 0.0, 250.0, 'm_{SD} [GeV]'],
        ]

def SetupArgs_LeftLegend():
    return [
        ['fj1Tau32SD', 20, 0, 1.0, '#tau_{3}/#tau_{2}'],
        ['fj1Tau32', 20, 0, 1.0, '#tau_{3}/#tau_{2}'],
        ['fj1sjQGL', 40, -1.0, 1.0, 'QGL'],
        ['nJet', 10, 0, 10, 'Number of Jets'],
        ['fj1M', 25, 0.0, 250.0, 'm_{Raw} [GeV]'],
        ['N2DDT', 20, -0.25, 0.25, 'DDT'],
        ]

def make_new(tail):
    new_out = os.environ['CrombieOutPlotDir'].rstrip('/') + tail
    plotter.SetOutDirectory(new_out)
    if not os.path.exists(new_out):
        os.makedirs(new_out)

def main():
    regions = ['base', 'fullcutz']
    for add in ['closeB', 'farB', 'rightMass', 'closeB+rightMass', 'farB+rightMass']:
        regions.append('base+' + add)

    plotter.SetLegendLocation(plotter.kUpper, plotter.kRight, 0.3, 0.4)
    MakePlots(cuts.categories, regions, SetupArgs_RightLegend(), overwrite)
    plotter.SetLegendLocation(plotter.kUpper, plotter.kLeft, 0.3, 0.4)
    MakePlots(cuts.categories, regions, SetupArgs_LeftLegend(), overwrite)

if __name__ == '__main__':
    main()

    plotter.NameTreesAfterLimits()
    plotter.SetLegendColor('Signal', 867)
    plotter.SetLegendColor('Background', 393)

    make_new('_background')
    main()
    plotter.ScaleBackgrounds('Background', 1.0)
    make_new('_up')
    main()
    plotter.ScaleBackgrounds('Background', -0.75)
    make_new('_down')
    main()
