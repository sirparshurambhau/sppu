#!/bin/bash

# Define the TSV file path
FILE="uptime_data.tsv"

# Create the TSV file with headers if it doesn't exist
if [ ! -f "$FILE" ]; then
    echo -e "Timestamp\tUptime" > "$FILE"
fi

# Function to get current timestamp
get_timestamp() {
    date +"%Y-%m-%d %H:%M:%S"
}

# Function to get system uptime
get_uptime() {
    uptime -p | cut -d' ' -f2-
}

# Function to append uptime data to the TSV file
append_to_file() {
    timestamp="$1"
    uptime="$2"
    echo -e "$timestamp\t$uptime" >> "$FILE"
}

# Continuously monitor uptime and update the TSV file
while true; do
    timestamp=$(get_timestamp)
    uptime=$(get_uptime)
    append_to_file "$timestamp" "$uptime"
    sleep 300  # Wait for 5 minutes before updating again
done

