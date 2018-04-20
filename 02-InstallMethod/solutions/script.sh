#!/bin/sh
inputImage=${1}
outputFolder=${2}

java -jar /input/otsubinarization.jar ${inputImage} ${outputFolder}