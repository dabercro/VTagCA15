source ../slimmer/CrombieSlimmingConfig.sh

export CrombieMCConfig=MCConfig.txt
#export CrombieSignalConfig=SignalConfig.txt
export CrombieExcept_example=MCAdjust.txt
export CrombieLuminosity=36600.0
export CrombieInFilesDir=/data/t3home000/bmaier/flat/sf
export CrombieOutPlotDir=/home/dabercro/public_html/plots/`date +%y%m%d`_VTagCA15
export CrombieOutLimitTreeDir=limits/`date +%y%m%d`

export CrombieCutsFile=cuts.py

if [ "$DEBUG" != "" ]
then

    export CrombieNLocalProcs=1

fi