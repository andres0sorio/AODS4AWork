#!/bin/bash

SCRIPT="ganga_script-Ver_1.0.py"
SCRIPT_PATH="ganga/"

. $HOME/gangaenv/bin/activate

cd $SCRIPT_PATH

zip -r input_data.zip datosproyecto/ spde-book-functions.R

ganga $SCRIPT

exit 1
