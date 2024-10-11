import os
import argparse

# Function to split sales files
def split_sales_file(input_file_path, output_file_template, starting_number, number_of_output_files):
    # Check if the input file exists
    if not os.path.exists(input_file_path):
        print(f"Error: The input file '{input_file_path}' does not exist.")
        return

    # Ensure the output directory exists, if not, create it
    output_dir = os.path.dirname(output_file_template)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Read the input file
    with open(input_file_path, "r") as file:
        lines = file.readlines()

    # Store the header
    header = lines[0]

    # Remove the header from the list of lines for splitting
    lines = lines[1:]

    # Split the sales into groups based on the sale headers (lines starting with "1")
    sales = []
    current_sale = []

    for line in lines:
        if line.startswith("1") and current_sale:
            sales.append(current_sale)
            current_sale = []
        current_sale.append(line)

    # Add the last sale if it exists
    if current_sale:
        sales.append(current_sale)

    # Calculate the total number of sales
    total_sales = len(sales)

    # Determine how many sales should go into each file
    sales_per_file = total_sales // number_of_output_files

    # Prepare files data
    files_data = []
    current_file = [header]

    for i, sale in enumerate(sales):
        current_file.extend(sale)

        # Check if we should start a new file based on the required number of sales
        if (i + 1) % sales_per_file == 0 and len(files_data) < number_of_output_files - 1:
            files_data.append(current_file)
            current_file = [header]

    # Add any remaining sales to the last file
    if current_file:
        files_data.append(current_file)

    # Write the data into the respective output files and ensure "EOF" is added directly after the last sale
    for i, file_data in enumerate(files_data):
        file_number = starting_number + i
        output_file_name = f"{output_file_template}{file_number:02}.RCZ"
        
        with open(output_file_name, "w") as output_file:
            output_file.writelines(file_data)
            output_file.write("EOF\n")

    print(f"Successfully split the file into {number_of_output_files} files.")

# Main function to handle command-line arguments
def main():
    parser = argparse.ArgumentParser(description="Split a Redcat legacy sales file into smaller files.")
    
    # Define the command-line arguments
    parser.add_argument('-i', '--input', required=True, help="Path to the input sales file.")
    parser.add_argument('-o', '--output', required=True, help="Template for output files (e.g., C:/path/to/outputfilename).")
    parser.add_argument('-s', '--start', type=int, required=True, help="Starting number for the output file numbering.")
    parser.add_argument('-n', '--num_files', type=int, required=True, help="Number of output files to create.")

    args = parser.parse_args()

    # Call the sales splitting function with the parsed arguments
    split_sales_file(args.input, args.output, args.start, args.num_files)

if __name__ == "__main__":
    main()