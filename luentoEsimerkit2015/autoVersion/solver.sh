#!/bin/bash

# Clean old stuff
rm -rf 0; cp -rf 0.org 0
rm -rf [1-9]*
rm -rf processor*
foamClearPolyMesh 

# Set parameters
sed -i "s/rateSmall X/rateSmall $1/g" 0/U

# Make geometry
rm constant/triSurface/*
salome -t dump.py
cp ../cad/*.stl constant/triSurface/

# Make background mesh
blockMesh -dict system/blockMeshDict
# Run snappyHexMesh 
snappyHexMesh -overwrite
# Check mesh quality
checkMesh | tee log/checkMesh
# Change boundary types
changeDictionary -constant
decomposePar
echo Running solver
mpirun -np 2 buoyantBoussinesqSimpleFoam -parallel > log/solver 2>&1
reconstructPar -latestTime

# Post, read pressure from latest time on pathch inletSmall
# and writes the number in file pAverage after some string manipulation
patchAverage -latestTime p inletSmall > log/patchAverage 2>&1
cat log/patchAverage | grep 'patch inletSmall' | rev | cut -d' ' -f1 | rev > pAverage











