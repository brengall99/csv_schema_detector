import pandas as pd
from tabulate import tabulate

def detect_csv_schema(file_path):

    # Load the CSV file, attempt to parse dates
    data = pd.read_csv(file_path, parse_dates=True, dayfirst=True)
    data = data.loc[:, ~data.columns.str.contains('^Unnamed')] # Drop empty columns

    # Iterate and check for date and bool type
    for column in data.columns:
        col_data = data[column]
        if col_data.dtype == 'object':
            # Attempt to manually parse datetime if not automatically detected
            try:
                data[column] = pd.to_datetime(data[column], dayfirst=True)
            except (ValueError, TypeError):
                pass

        # Check for bool columns that use 0s or 1s
        unique_values = pd.unique(col_data.dropna())
        if set(unique_values) <= {0, 1}:
            if len(unique_values) == 2:
                data[column] = col_data.astype('bool')

    # Prepare schema data for each column
    schema = []
    for column in data.columns:
        col_data = data[column]
        data_type = col_data.dtype

        # Refine type descriptions
        if pd.api.types.is_datetime64_any_dtype(data_type):
            data_type = "DateTime"
        elif pd.api.types.is_bool_dtype(data_type):
            data_type = "Boolean"
        elif pd.api.types.is_object_dtype(data_type):
            if any(isinstance(x, (int, float, complex)) and not isinstance(x, bool) for x in col_data.dropna()):
                data_type = "Mixed (Numeric & String)"
            else:
                data_type = "String (Homogeneous)"

        # Determine the mode (nullable or not)
        mode = "Nullable" if col_data.isnull().any() else "Not Nullable"

        schema.append({
            "Column Name": column,
            "Type": str(data_type),
            "Mode": mode
        })

    # Print the schema using tabulate
    print(tabulate(schema, headers="keys", tablefmt="grid"))


# Replace 'example_data.csv' with a different file to detect schema
detect_csv_schema("example_data.csv")

if __name__ == "__main__":
    detect_csv_schema("example_data.csv")
    



