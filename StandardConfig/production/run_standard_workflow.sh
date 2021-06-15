#!/bin/bash
set -euo pipefail

RUN_THE_THINGS=ON

function run_cmd() {
  local logfile=${1}
  shift
  echo $@
  if [ "X${RUN_THE_THINGS}" = "XON" ]; then
    $@ > ${logfile} 2>&1
  fi
}

function clear_outputs() {

  local output_files=( bbudsc_3evt_AIDA.root \
    bbudsc_3evt_DST.slcio \
    bbudsc_3evt_LCTuple.root \
    bbudsc_3evt_PfoAnalysis.root \
    bbudsc_3evt_REC.slcio \
    bbudsc_3evt_SIM.slcio \
    MarlinStdRecoParsed.xml \
    ddsim.out \
    marlin.out \
    lctuple.out )

  for file in $output_files; do
    [ -f ${file} ] && rm ${file} || true
  done
}

function prepare_lcfiweights() {
  local lcfiweights=$(pwd)/../../LCFIPlusConfig/lcfiweights
  local weights=4q250_ZZ_v4_p00_ildl5
  if [ ! -d ${lcfiweights}/${weights} ]; then
    echo "Unpacking LCFIPlus weights for test"
    tar -xzf ${lcfiweights}/${weights}.tar.gz
  fi
}

UNUSED_ARGS=

while [ $# != 0 ]; do
  case "$1" in
    -h|--help)
      echo "Usage: $0 [-h|--help] [-d|--dry-run] [--clear] [tag]"
      echo "Run the standard workflow steps as described in the README.md"
      echo "If run in dry-run mode only print the commands that would be run"
      echo "If run with --clear, remove the outputs that are generated by this script, but do not run the workflow steps"
      exit 0
      ;;
    -d|--dry-run)
      RUN_THE_THINGS=OFF
      shift
      ;;
    --clear)
      clear_outputs
      exit 0
      ;;
    *)
      git checkout $1
      shift
      ;;
  esac
done

DDSIM_CMD="ddsim \
  --inputFiles Examples/bbudsc_3evt/bbudsc_3evt.stdhep \
  --outputFile bbudsc_3evt_SIM.slcio \
  --compactFile $lcgeo_DIR/ILD/compact/ILD_l5_v02/ILD_l5_v02.xml \
  --steeringFile ddsim_steer.py"

MARLIN_CMD="Marlin MarlinStdReco.xml \
  --constant.lcgeo_DIR=$lcgeo_DIR \
  --constant.DetectorModel=ILD_l5_o1_v02 \
  --constant.OutputBaseName=bbudsc_3evt \
  --global.LCIOInputFiles=bbudsc_3evt_SIM.slcio"

LCTUPLE_CMD="Marlin MarlinStdRecoLCTuple.xml \
  --global.LCIOInputFiles=bbudsc_3evt_DST.slcio \
  --MyAIDAProcessor.FileName=bbudsc_3evt_LCTuple"

MINIDST_CMD="Marlin mini-DST-maker.xml \
  --global.LCIOInputFiles=bbudsc_3evt_DST.slcio \
  --constant.OutputFile=bbudsc_3evt_miniDST.slcio \
  --constant.LCFIPlusWeightsDir=$(pwd)/../../LCFIPlusConfig/lcfiweights/4q250_ZZ_v4_p00_ildl5"


clear_outputs
run_cmd ddsim.out ${DDSIM_CMD}
run_cmd marlin.out ${MARLIN_CMD}
run_cmd lctuple.out ${LCTUPLE_CMD}

prepare_lcfiweights
run_cmd minidst.out ${MINIDST_CMD}