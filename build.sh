#!/bin/bash
cd $WORKSPACE
./setup_env.sh

source $WORKSPACE/env/bin/activate
cd $WORKSPACE

python tests.py
