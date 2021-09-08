#!/bin/bash

echo "Arg1 $1"
echo "Arg2 $2"

DATA=input_data.zip
unzip $DATA
mkdir output
SCRIPT="modeloaccidentesv0609.R"
R --version

#Rscript $SCRIPT $1 $2

echo R CMD BATCH --no-save --no-restore '--args a="'$1'" b="'$2'"' $SCRIPT $SCRIPT.out

sudo nice --15 R CMD BATCH --no-save --no-restore '--args a="'$1'" b="'$2'"' $SCRIPT $SCRIPT.out

# For debuging
echo $PWD
ls

