#!/bin/bash

# Clean old stuff
rm -rf 0; cp -rf 0.org 0
rm -rf [1-9]*
rm -rf processor*
foamClearPolyMesh 

# Meshing
cartesianMesh
# Change boundary types
changeDictionary -constant
# Check mesh quality
checkMesh | tee log/checkMesh

# Solver
echo Running solver
buoyantBoussinesqSimpleFoam > log/solver 2>&1

# Post, read pressure from latest time on pathch inletSmall
# and writes the number in file pAverage after some string manipulation
patchAverage -latestTime p inletSmall | tee log/patchAverage 2>&1
cat log/patchAverage | grep 'patch inletSmall' | rev | cut -d' ' -f1 | rev > pAverage






