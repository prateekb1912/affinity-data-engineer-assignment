#!/bin/bash

# Download the file and onto local machine
wget amfiindia.com/spages/NAVAll.txt

# Extract Scheme Name (column 4) and Asset Value (column 5)
# and storing result in a temporary file
awk -F ';' '{print $4 "," $5}' NAVAll.txt > assets_temp.txt

# Clean the text file by removing rows where data is empty (only the seperator is present)
# and save the final results to a CSV file
awk -F ',' 'length($0) > 1' assets_temp.txt > assets.csv

# Remove the original and temporary files
rm NAVAll.txt assets_temp.txt
