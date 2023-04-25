#!/bin/bash

# Array containing the exact names of the chapters
chapter_names=(
  "Exploratory Data Analysis (EDA)"
  "Linear Models for Interpretability"
  "Decision Trees and Random Forests"
  "Explainable Boosting Machines"
  "Model Agnostic Interpretability Methods"
  "Model Interpretation in Deep Learning"
  "Fairness and Ethics in Machine Learning"
)

# Function to format chapter names: convert to lowercase, replace spaces with underscores,
# and remove characters that are not safe for directory names
format_chapter_name() {
  echo "$1" | tr '[:upper:]' '[:lower:]' | tr ' ' '_' | tr -d '()'
}

# Number of sections
num_sections=1

# Function to pad numbers with leading zeros
pad_number() {
  printf "%02d" "$1"
}

# Create sections and chapters
for ((section=1; section<=num_sections; section++)); do
  section_padded=$(pad_number $section)
  section_dir="section${section_padded}"
  mkdir -p "$section_dir"
  for ((chapter=1; chapter<=${#chapter_names[@]}; chapter++)); do
    chapter_padded=$(pad_number $chapter)
    formatted_chapter_name=$(format_chapter_name "${chapter_names[chapter-1]}")
    chapter_dir="chapter${chapter_padded}-${formatted_chapter_name}"
    # Create chapter directory inside the section directory
    mkdir -p "$section_dir/$chapter_dir"
    # Create files for lecture notes, slides, resources, and Python scripts for running code
    touch "$section_dir/$chapter_dir/lecture_notes.md"
    touch "$section_dir/$chapter_dir/slides.pdf"
    touch "$section_dir/$chapter_dir/resources.md"
    touch "$section_dir/$chapter_dir/run_exercises.py"
    touch "$section_dir/$chapter_dir/run_examples.py"
  done
done

echo "Directories and files for coding exercises have been created successfully."
