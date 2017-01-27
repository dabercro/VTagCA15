# Two dictionaries to define the cuts for separate categories and control regions

base = ' && '.join([
        'nFatjet==1',
        '(nLooseElectron+nLoosePhoton+nTau)==0 && nLooseMuon==1 && looseLep1IsTight==1',
        'fj1Pt>200',
        'fj1MSD_corr>50',
        'fj1MSD_corr<250',
        'dphiUW>0.4',
        'metFilter==1',
        'Sum$(jetPt>30 && jetIso && jetCSV>0.89)>0',
        'Sum$(jetPt>30 && jetIso && jetCSV>0.605)==2',
        'Sum$(jetPt>30 && jetIso)<4',
        ])

categoryCuts = {
    'cat' : '1'
    }

regionCuts = {
    'base' : base,
    'closeB' : 'dRfj1Isob < 1.5',
    'farB' : 'dRfj1Isob > 1.5',
    'rightMass' : 'fj1MSD_corr < 105 && fj1MSD_corr > 65',
    'n2ddt' : 'N2DDT < 0',
    'fullcutz' : ' && '.join([
            base,
            'fj1MaxCSV < 0.5',
            ])
    }

# These are just for the users to loop over

categories = categoryCuts.keys()
regions    = regionCuts.keys()

# Making selection of multiple entries

def joinCuts(toJoin=regionCuts.keys(), cuts=regionCuts):
    return ' && '.join([cuts[cut] for cut in toJoin])

# A weight applied to all MC

defaultMCWeight = '*'.join([
        'normalizedWeight',
        'sf_pu',
        'sf_ewkV',
        'sf_qcdV',
        'sf_csvWeightB*sf_csvWeightM',
        'sf_tt8TeV',
        'sf_metTrig',
        'sf_lep',
        ])

defaultDataWeight = '(trigger&1)!=0'

# Additional weights applied to certain control regions

region_weights = { # key : [Data,MC]
    'signal'  : ['0', defaultMCWeight],
    'default' : [defaultDataWeight, defaultMCWeight]
    }

# Do not change the names of these functions or required parameters
# Otherwise you cannot use some convenience functions
# Multiple regions are concatenated with '+'
# Generally you can probably leave these alone

def cut(category, region):
    return '((' + categoryCuts[category] + ') && (' + joinCuts(toJoin=region.split('+')) + '))'

def dataMCCuts(region, isData):
    key = 'default'
    if region in region_weights.keys():
        key = region

    index = 0 if isData else 1

    return '(' + region_weights[key][index] + ')'
