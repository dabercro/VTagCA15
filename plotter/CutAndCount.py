#!/usr/bin/env python

from CrombieTools.AnalysisTools.HistAnalysis import *
from CrombieTools.LoadConfig import cuts
import os, sys

SetupFromEnv()

histAnalysis.SetPrintingMethod(histAnalysis.kPresentation)

histAnalysis.AddDataFile('MET.root')
histAnalysis.SetSignalName('Signal')
histAnalysis.SetSearchBy(histAnalysis.kLimitName)
histAnalysis.SetMCWeight(cuts.defaultMCWeight)
histAnalysis.SetDataWeight(cuts.defaultDataWeight)

def GetTables():
    histAnalysis.ResetScaleFactorCuts()
    for name, cut in [('SD Mass Cut',cuts.regionCuts['rightMass']),
                      ('N2DDT',cuts.regionCuts['n2ddt']),
                      ('Full Cut',cuts.joinCuts(['rightMass','n2ddt']))]:
        histAnalysis.AddScaleFactorCut(name, cut)

    histAnalysis.SetBaseCut(cuts.cut('cat', 'base'))
    histAnalysis.DoScaleFactors('fj1IsMatched', 1, 0, 2)

    print '\nWith anti-btag\n'

    histAnalysis.SetBaseCut(cuts.cut('cat', 'fullcutz'))
    histAnalysis.DoScaleFactors('fj1IsMatched', 1, 0, 2)

    print '\nWith far-btag\n'

    histAnalysis.SetBaseCut(cuts.cut('cat', 'base+farB'))
    histAnalysis.DoScaleFactors('fj1IsMatched', 1, 0, 2)


if __name__ == "__main__":
    GetTables()

    print '\nBackground Up\n'
    histAnalysis.ChangeBackground(1.0)
    GetTables()
    print '\nBackground Down\n'
    histAnalysis.ChangeBackground(-0.5)
    GetTables()

    histAnalysis.ChangeBackground(0.0)
