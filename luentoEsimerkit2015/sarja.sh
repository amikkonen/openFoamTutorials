#!/bin/bash 

for k in 1 2 3 4 5
do
    caseDir="auto$k"; 
    echo $caseDir 
    # Clean
    rm -rf $caseDir
    # Copy
	cp -rf autoVersion auto$k
    # Calc rate 
    rate=$(awk "BEGIN{print 0.0001963495 * $k}")    
    echo '   'rate $rate
    # Run
    cd $caseDir
    bash solver.sh $rate #> logSarja 2&1
    pAverage=$(cat pAverage)    
    cd ..
    echo $caseDir $pAverage >> tulos
done


