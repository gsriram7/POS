#!/bin/sh

set -e

mv 1.txt old_1.txt || true
mv 2.txt old_2.txt || true

cp ../en_dev_tagged.txt ./1.txt
cp ../opt.txt ./2.txt

chmod 660 1.txt || true
chmod 660 2.txt || true

tr '\n' '\t' < 1.txt > 11.txt
tr ' ' '\n' < 11.txt > 111.txt
tr '\t' '\n' < 111.txt > 1111.txt

tr '\n' '\t' < 2.txt > 22.txt
tr ' ' '\n' < 22.txt > 222.txt
tr '\t' '\n' < 222.txt > 2222.txt

rm -f 1.txt 11.txt 111.txt 2.txt 22.txt 222.txt
mv 1111.txt 1.txt
mv 2222.txt 2.txt