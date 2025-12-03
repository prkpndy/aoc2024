#!/bin/bash

# Check if exactly two arguments were provided
if [ "$#" -ne 2 ]; then
    echo "Error: Two compulsory arguments (year and problem) are required."
    echo "Usage: $0 <YEAR> <PROBLEM_NAME>"
    echo "Example: $0 2023 day1"
    exit 1
fi

# Assign arguments to descriptive variables
YEAR=$1
PROBLEM=$2

# Define the target directory path
TARGET_DIR="${YEAR}/${PROBLEM}"

# 1. Create the directory structure (e.g., 2023/day1)
# The -p flag ensures parent directories (like 2023) are created if they don't exist.
echo "Creating directory: ${TARGET_DIR}..."
if mkdir -p "${TARGET_DIR}"; then
    echo "Directory created successfully."
else
    echo "Error: Failed to create directory ${TARGET_DIR}."
    exit 1
fi

# Define the files to be created inside the target directory
FILES=(
    "p1.py"
    "p2.py"
    "input.txt"
    "example.txt"
)

# 2. Create the required files inside the new directory
echo "Creating files inside ${TARGET_DIR}..."
for FILE_NAME in "${FILES[@]}"; do
    # Use 'touch' to create an empty file
    touch "${TARGET_DIR}/${FILE_NAME}"
done

echo "---"
echo "Setup complete!"
echo "Files created at: $(pwd)/${TARGET_DIR}"
echo "Ready to start coding!"
