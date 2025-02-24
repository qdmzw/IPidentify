
# Romanian IP Identification Tool

## Overview
This Python script filters out Romanian IP addresses from a given list using the GeoLite2 database. It processes the IPs concurrently for efficiency and saves the identified Romanian IPs in a separate file.

## Requirements
- Python 3.x
- `geoip2` library
- `concurrent.futures` for multithreading
- `tqdm` for progress tracking
- GeoLite2 database (download from [MaxMind](https://dev.maxmind.com/geoip/geolite2-free-geolocation-data))

## Installation
1. Install required Python libraries:
   ```bash
   pip install geoip2 tqdm
   ```
2. Download and extract the GeoLite2 database.

## Usage
1. Place your list of IPs in a file (e.g., `affected_ips.txt`).
2. Update the script with the correct path to your GeoLite2 database.
3. Run the script:
   ```bash
   python script.py
   ```
4. The filtered Romanian IPs will be saved in `romanian_ips.txt`.

## Configuration
- `MAX_WORKERS`: Defines the number of threads for processing IPs (default: 50).
- `file_path`: Input file containing IP addresses.
- `output_path`: Output file where Romanian IPs are stored.

## How It Works
1. Reads IPs from the input file, removing duplicates and unnecessary spaces.
2. Uses `geoip2` to check if each IP belongs to Romania.
3. Processes IPs in parallel using multithreading for efficiency.
4. Saves identified Romanian IPs to an output file.

## Example Input (`affected_ips.txt`)
```
192.168.1.1
86.122.59.31
5.2.138.8
``` 

## Example Output (`romanian_ips.txt`)
```
86.102.50.1
5.2.120.0
```

## Notes
- Ensure that the GeoLite2 database is correctly referenced in the script.
- If you receive errors, verify that the database file is accessible and updated.

## License
This project is provided under the MIT License.

## Author
Cocerba Alexandru

