#!/bin/bash

rm */*.pdf

crombie downloadtar "http://t3serv001.mit.edu/~dabercro/plotviewer/returntar.php?only=pdf&files=170207_VTagCA15%2Fcat_fullcutz_fj1Tau32%2C170207_VTagCA15%2Fcat_fullcutz_medB%2C170207_VTagCA15%2Fcat_fullcutz_looseB%2C170207_VTagCA15%2Fcat_fullcutz_fj1Tau32SD%2C170207_VTagCA15%2Fcat_fullcutz_N2DDT%2C170207_VTagCA15%2Fcat_fullcutz_fj1MaxCSV%2C170207_VTagCA15%2Fcat_fullcutz_dphiUW%2C170207_VTagCA15%2Fcat_base_fj1MSD_corr%2C170207_VTagCA15%2Fcat_fullcutz_fj1MSD_corr%2C170207_VTagCA15%2Fcat_fullcutz_fj1Pt%2C170207_VTagCA15%2Fcat_fullcutz_nJet%2C170207_VTagCA15%2Fcat_fullcutz_pfmetnomu"
crombie downloadtar "http://t3serv001.mit.edu/~dabercro/plotviewer/returntar.php?only=pdf&files=170207_VTagCA15_background%2Fcat_fullcutz_N2DDT%2C170207_VTagCA15_more%2Fcat_fullcutz_N2DDT%2C170207_VTagCA15_down%2Fcat_fullcutz_N2DDT%2C170207_VTagCA15_up%2Fcat_fullcutz_N2DDT%2C170207_VTagCA15_background%2Fcat_fullcutz_fj1MSD_corr%2C170207_VTagCA15_more%2Fcat_fullcutz_fj1MSD_corr%2C170207_VTagCA15_down%2Fcat_fullcutz_fj1MSD_corr%2C170207_VTagCA15_up%2Fcat_fullcutz_fj1MSD_corr"
crombie downloadtar "http://t3serv001.mit.edu/~dabercro/plotviewer/returntar.php?only=pdf&files=170207_VTagCA15%2Fcat_base_dRfj1Isob%2C170207_VTagCA15%2Fcat_fullcutz_dRfj1Isob"
crombie downloadtar "http://t3serv001.mit.edu/~dabercro/plotviewer/returntar.php?only=pdf&files=170207_VTagCA15%2Fcat_fullcutz%2BfarB_fj1MaxCSV%2C170207_VTagCA15%2Fcat_fullcutz_fj1MaxCSV%2C170207_VTagCA15%2Fcat_base_dRfj1Isob%2C170207_VTagCA15%2Fcat_base%2BrightMass_dRfj1Isob%2C170207_VTagCA15%2Fcat_fullcutz%2BrightMass_dRfj1Isob%2C170207_VTagCA15%2Fcat_fullcutz_dRfj1Isob%2C170207_VTagCA15%2Fcat_base%2BfarB_fj1MSD_corr%2C170207_VTagCA15%2Fcat_fullcutz%2BfarB_fj1MSD_corr%2C170207_VTagCA15%2Fcat_base_fj1MSD_corr%2C170207_VTagCA15%2Fcat_fullcutz_fj1MSD_corr"
crombie downloadtar "http://t3serv001.mit.edu/~dabercro/plotviewer/returntar.php?only=pdf&files=170207_VTagCA15%2Fcat_base%2BfarB_dRfj1Isob%2C170207_VTagCA15%2Fcat_fullcutz%2BfarB_dRfj1Isob"
crombie downloadtar "http://t3serv001.mit.edu/~dabercro/plotviewer/returntar.php?only=pdf&files=170207_VTagCA15%2Fcat_base%2BfarB_N2DDT%2C170207_VTagCA15%2Fcat_base%2BfarB%2BrightMass%2Bn2ddt_N2DDT%2C170207_VTagCA15%2Fcat_base%2BfarB_fj1MSD_corr%2C170207_VTagCA15%2Fcat_base%2BfarB%2BrightMass%2Bn2ddt_fj1MSD_corr"
crombie downloadtar "http://t3serv001.mit.edu/~dabercro/plotviewer/returntar.php?only=pdf&files=170207_VTagCA15%2Fcat_fullcutz%2BrightMass%2Bn2ddt_N2DDT%2C170207_VTagCA15%2Fcat_fullcutz_N2DDT%2C170207_VTagCA15%2Fcat_fullcutz%2BrightMass%2Bn2ddt_fj1MSD_corr%2C170207_VTagCA15%2Fcat_fullcutz_fj1MSD_corr"

for f in */*.pdf
do
    pdfcrop $f $f
done
