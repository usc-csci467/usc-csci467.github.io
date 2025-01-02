#!/bin/bash
set -eu -o pipefail
if [ $# -eq 0 ]
then
    echo "Usage: $0 [fall|spring]year" 1>&2
    exit 1
fi

# Markdown
mkdir -p $1
cp index.md project.md $1
cd $1
sed -i -e "s@(/assets@(/assets/$1@g" index.md
sed -i -e "s/include hw.html/include hw.html sem=\"$1\"/g" index.md
sed -i -e "s@(/assets@(/assets/$1@g" project.md
cd ..

# Assets 
cd assets
mkdir -p $1
mv hw*.pdf hw*.zip notes.pdf report*.pdf backprop exams images lectures sections $1
mkdir -p backprop exams images lectures sections
mv $1/images/person_placeholder.jpg images
cd ..
