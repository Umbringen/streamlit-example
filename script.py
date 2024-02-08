import pandas as pd

def process_csv(input_file, output_file):
    # Read CSV file
    df = pd.read_csv(input_file)

    # Add something (e.g., a new column)
    df['New_Column'] = 'New_Value'

    # Save to new file
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_file = "test.csv"  # Replace with your input CSV file path
    output_file = "output_file.csv"  # Replace with the desired output CSV file path

    process_csv(input_file, output_file)
