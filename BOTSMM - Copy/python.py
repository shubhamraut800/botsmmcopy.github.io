# Open the input file for reading
with open("data.txt", "r") as f:
    # Read the lines from the file
    lines = f.readlines()

# Initialize the output string
output = ""

# Process each line of the input file
for line in lines:
      # Split the line into its columns
    cols = line.strip().split("\t")
    if len(cols) == 6:
        # Extract the relevant information
        service_name = cols[1].split("-")[0].strip()
        service_type = cols[1].split("-")[1].strip()
        service_price = cols[2]
        # Format the output line
        output_line = f"{service_name}\t{service_type}\t{service_price}\n"
        # Append the output line to the output string
        with open("output.txt", "a") as f:
    # Write the output string to the file
          f.write('"' +service_name+ '"'+",")
        output += output_line
    else:
        # Handle the case where the line has the wrong number of columns
        print(f"Skipping line {line.strip()}: wrong number of columns")


# Open the output file for writing
