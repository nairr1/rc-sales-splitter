# Sales Splitter Script

## Overview
This Python script is designed to split large Redcat legacy sales files into smaller, more manageable files for efficient processing by the Polygon POS Management Revenue Processing Service. Large sales files can overwhelm the service, causing delays or failures in processing. By splitting the sales data into smaller files, this script ensures smoother handling.

The script:
- Removes the file header and appends it as the first line of each split file.
- Splits sales based on user-defined numbers, grouping lines starting with "1" (indicating the start of a sale) and ending with lines starting with "3".
- Appends "EOF" at the end of each split file to ensure proper handling by the revenue processing service.

## Key Features
- **Splits sales files**: Divides a large Redcat legacy sales file into smaller, user-defined files.
- **Retains the header**: The file header is removed and prepended to each split file.
- **Custom file size**: Users can define the number of output files.
- **EOF Handling**: Appends "EOF" to the last line of each split file to ensure correct processing by the Polygon POS management service.

## Requirements
- Python 3.x
- Standard Python libraries (`os`, `argparse`)

## Installation
1. Clone or download the repository.
2. Ensure Python 3.x is installed on your machine.
3. No additional dependencies are required.

## Usage
### Command Line Arguments
The script can be run via the command line, with the following arguments:
```bash
python sales_splitter.py -i <input_file> -o <output_template> -s <starting_number> -n <number_of_files>