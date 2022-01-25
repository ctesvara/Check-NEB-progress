#!/bin/bash -l

filename= $(pwd)

for a in 01 02 03 04 05 06 07 08 
   do
      cd $a
      perl ~/bin/vasp.5.4.4/vtstscripts-939/vef.pl
      mv fe.dat fe-image-$a.dat
      cd ..
      echo $a forces are written
   done

