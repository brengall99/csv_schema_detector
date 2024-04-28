import csv
from tabulate import tabulate
from datetime import datetime


def generate_schema(csv_file_path):
    # List to store column information as lists [name, data_type, nullable]
    schema = []

    # Read the CSV file
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)

        # Iterate over the rows to infer schema
        for row in reader:
            for key, value in row.items():
                # Check if it's a date
                try:
                    datetime.strptime(value, '%d/%m/%Y')
                    data_type = "date"
                except ValueError:
                    # Infer data type based on the value
                    if value.isdigit():
                        data_type = "int"
                    elif value.replace(".", "", 1).isdigit():
                        data_type = "float"
                    else:
                        data_type = "str"

                # Check if nullable
                nullable = False if value.strip() else True

                # Update or add column information
                found = False
                for column_info in schema:
                    if column_info[0] == key:
                        found = True
                        if data_type != column_info[1]:
                            if column_info[1] == "str":
                                column_info[1] = data_type
                            elif data_type == "str":
                                pass
                            else:
                                column_info[1] = "str"
                        if nullable:
                            column_info[2] = True
                        break
                if not found:
                    schema.append([key, data_type, nullable])

    return schema


# Print the schema as a table
def print_schema_table(schema):
    headers = ["Column Name", "Data Type", "Nullable"]
    print(tabulate(schema, headers=headers, tablefmt="grid"))


# Example usage
csv_file_path = "example_data.csv"
schema = generate_schema(csv_file_path)

# Print the schema as a table
print_schema_table(schema)


