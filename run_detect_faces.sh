#!/usr/bin/env bash

#-pathToFiles /home/daniel/Documents/CV_HCI/A2/data/test -outputFile /home/daniel/Documents/CV_HCI/A2/testOutput/testOutput.txt -testFiles /home/daniel/Documents/CV_HCI/A2/data/testFiles.txt

#Parameters:
# $1: Path to test files
# $2: File with the list of test images
# $3: output file where the output of test images should be saved

if [ ! -d "$1" ]; then
  echo "Path not existing"
  exit 1
fi


if [ ! -f "$2" ]; then
  echo "File with test images not found"
  exit 1
fi

timestamp() {
  date +"%Y_%m_%d_%H_%M_%S"
}

# start training
timestampValue=$(timestamp)

outputFilename="logs/detect_faces_"$timestampValue".log"

source /home/dschumacher/dschumacher_working_dir/anaconda/bin/activate /home/dschumacher/dschumacher_working_dir/anaconda/envs/cv_env


srun -c 1 --mem=10000 -t 5-00 -p lowGPU -w i13hpc51 --gres=gpu:1 -o $outputFilename -e $outputFilename \
python3.6 detect_faces.py -pathToFiles $1 -testFiles $2 -outputFile $3
