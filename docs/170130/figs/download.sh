#!/bin/bash

crombie downloadtar "http://t3serv001.mit.edu/~dabercro/plotviewer/returntar.php?only=pdf&files=170127%2Fcat_base_dRfj1Isob%2C170127%2Fcat_base_fj1MSD_corr"
crombie downloadtar "http://t3serv001.mit.edu/~dabercro/plotviewer/returntar.php?only=pdf&files=170127%2Fcat_base%2BcloseB_fj1MSD_corr%2C170127%2Fcat_base%2BfarB_fj1MSD_corr"
crombie downloadtar "http://t3serv001.mit.edu/~dabercro/plotviewer/returntar.php?only=pdf&files=170127%2Fcat_base%2BrightMass_dRfj1Isob"
crombie downloadtar "http://t3serv001.mit.edu/~dabercro/plotviewer/returntar.php?only=pdf&files=170127%2Fcat_base%2BrightMass_fj1Tau21%2C170127%2Fcat_base%2BrightMass_fj1Tau21SD"
crombie downloadtar "http://t3serv001.mit.edu/~dabercro/plotviewer/returntar.php?only=pdf&files=170127%2Fcat_base_N2DDT%2C170127_background%2Fcat_base_N2DDT%2C170127_down%2Fcat_base_N2DDT%2C170127_up%2Fcat_base_N2DDT%2C170127%2Fcat_base_fj1MSD_corr%2C170127_background%2Fcat_base_fj1MSD_corr%2C170127_down%2Fcat_base_fj1MSD_corr%2C170127_up%2Fcat_base_fj1MSD_corr"
crombie downloadtar "http://t3serv001.mit.edu/~dabercro/plotviewer/returntar.php?only=pdf&files=170127%2Fcat_base_fj1M"
crombie downloadtar "http://t3serv001.mit.edu/~dabercro/plotviewer/returntar.php?only=pdf&files=170127%2Fcat_fullcutz_fj1M%2C170127%2Fcat_fullcutz_fj1MSD_corr"

for f in */*.pdf
do
    pdfcrop $f $f
done
