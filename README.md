# Check-NEB-progress

A simple script to check the convergence of NEB calculations
Can be used to plot the barrier, the forces as a function of image number or reaction distance. 

Note that you will need the vef.pl script provided by Dr. Graeme Lab at UT Austin (vtstscript)

There are two scripts needed to obtain the graphs: get-fe-forces.sh and neb-check.py
get-fe-forces.sh prints the forces of each ionic step to a readable file by neb-check.py
neb-check.py plots the NEB progress. make sure get-fe-forces.sh is in the working path.

To run, simply run python neb-check.py
The code will ask for initial energy (image 00) to calculate the barriers. 
