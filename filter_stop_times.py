import csv

# === CONFIGURE THIS ===
stop_ids_to_keep = {"29", "7639"}  # Add more stop IDs as needed
input_file = r"C:\Users\rache\Desktop\prt-bus-display\gtfs\stop_times.txt"
output_file = r"C:\Users\rache\Desktop\prt-bus-display\gtfs\my_times.txt"

# Read input and write filtered output
with open(input_file, newline='', encoding='utf-8') as infile, \
     open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    
    writer.writeheader()  # Write CSV header
    
    for row in reader:
        if row['stop_id'] in stop_ids_to_keep:
            writer.writerow(row)

print(f"Filtered stop times written to {output_file}")
