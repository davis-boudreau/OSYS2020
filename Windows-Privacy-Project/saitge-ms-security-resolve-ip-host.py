import socket
import csv
import os

filename = "windows-startup-network-capture.csv"

def resolve_hostname(ip_address):
     try:
         hostname = socket.gethostbyaddr(ip_address)[0]
         return hostname
     except (socket.herror, socket.gaierror):
         return None

def resolve_ips_from_csv(input_filename=filename, output_filename="suspected-spyware.csv"):
     resolved_data = []
     input_filepath = os.path.join(os.path.dirname(__file__), input_filename)
     try:
         with open(input_filepath, 'r', newline='') as csvfile:
             reader = csv.DictReader(csvfile)
             print(f"CSV Columns: {reader.fieldnames}")  # Debugging line
             if 'destination' not in reader.fieldnames:
                 print(f"Error: The input CSV file '{input_filename}' must have a column named 'destination'.")
                 return
             for row in reader:
                 ip_address = row['destination']
                 hostname = resolve_hostname(ip_address)
                 resolved_data.append({'destination': ip_address, 'hostname': hostname})

         with open(output_filename, 'w', newline='') as csvfile:
             fieldnames = ['destination', 'hostname']
             writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
             writer.writeheader()
             writer.writerows(resolved_data)

         print(f"Successfully resolved hostnames from '{input_filename}' and saved to '{output_filename}'.")

     except FileNotFoundError:
         print(f"Error: Input CSV file '{input_filename}' not found.")
     except Exception as e:
         print(f"An error occurred: {e}")

if __name__ == "__main__":
     resolve_ips_from_csv()