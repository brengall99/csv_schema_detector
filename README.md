# CSV Schema Detector

## Project Overview
This is a tool designed to analyse and automaticaly report the shcema of a .csv file. The tool reads the CSV file, infers data types for each column, and identifies whether the columns contain homogeneous types, mixed numeric and string types, or date formats. Additionally, it detects columns that effectively represent boolean values using 0s and 1s.

## Features
- **Date Detection:** Automatically detects and parses columns that contain date information.
- **Boolean Detection:** Identifies columns with binary data represented as 0 or 1 and converts them to boolean.
- **Type Identification:** Classifies columns into various types including DateTime, Boolean, Mixed (Numeric & String), and String (Homogeneous).
- **Nullability Check:** Checks each column for null values and provides the mode (Nullable or Not Nullable).

## Required Libraries
```python
pip install pandas tabulate
```

## Data
Included in this repository is an example csv 'example_data.csv'. To use this example, ensure it is in the same folder as the 'schema_inference_tool.py' file.

## Usage
We can use the tool as an independent function, and call it to a different project via:
```python
from detect_csv_schema import detect_csv_schema

# Replace 'yourfile.csv' with apropriate file or path
detect_csv_schema('yourfile.csv')
```

or, we can run the tool as an independend function, by running 'schema_inference_tool.py' directly.

## Example Output
<img width="395" alt="Screenshot 2024-04-29 at 18 27 41" src="https://github.com/brengall99/csv_schema_detector/assets/159880330/905bf2b8-8268-46ed-bfe9-4a4b52092c93">
