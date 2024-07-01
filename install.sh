#!/bin/bash
## Internal variables
# Directory for project
DIR=~/COLVIRM
# Repository COLVIRM
REPO=https://github.com/hadesmechanics/COLVIRM_im7conversion.git
# Conda activate
CONDA=~/anaconda3/bin/activate
# Environment requirements
DIC=DICenv.yml
# Create COLVIRM directory
mkdir -p $DIR
# Change current directory
cd $DIR
## Run in terminal if git needs installation
# Update package manager to install
# sudo apt update
# Download git package, if needed
# sudo apt install git
## End of lines of git installation
## Git operations
# Clone COLVIRM repository
git clone $REPO $DIR
# Activate conda environment
. $CONDA
# Create DIC environment
conda env create -f $DIC
# Activate DIC environment
conda activate dic
# Install ReadIM-python
pip install ReadIM
## Remove comment for example
# Read and convert COLVIRM_01.im7 to png
#python3 RDIMCV.py --single-im7 COLVIRM_01.im7
# Another way to run same example
#python3 RDIMCV.py --single-im7 COLVIRM_01
## End of remove comment
#---------------------------------------
# Training
#---------------------------------------
# Training task 1: adjust the program so that
# the following command line produces the same
# image operations as the example above
#python3 RDIMCV.py --default COLVIRM_01
#---------------------------------------
# Training task 2: adjust the program so that
# the example run give 8-bit png images by
# running same command line as before
#python3 RDIMCV.py --single-im7 COLVIRM_01.im7

