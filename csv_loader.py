import csv
from package import Package
from hashtable import HashMap

def read_csv_file(file_name):
    # Load data from a CSV file
    with open(file_name) as csvfile:
        data = csv.reader(csvfile)
        return list(data)

def create_address_mapping(file_name):
    # Load address data from a CSV file
    with open(file_name) as address_info:
        address_file = csv.reader(address_info)
        address_data = {}
        for row in address_file:
            address_id = int(row[0])
            # Store address ID mapping with address as the key
            address_data[row[2]] = address_id
        return address_data

def load_package_information(file_name):
    package_table = HashMap()
    with open(file_name) as package_info:
        package_file = csv.reader(package_info)
        for package in package_file:
            # Extract package information from each row of the CSV file
            package_ID, package_address, package_city, package_state, package_zipcode, package_deadline, package_weight = map(str.strip, package[:7])
            package_status = "At Hub"
            # Create a Package object with the extracted information
            pkg = Package(int(package_ID), package_address, package_city, package_state, package_zipcode, package_deadline, package_weight, package_status)
            # Store the package ID mapping with the Package object
            package_table.insert(int(package_ID), pkg)
    return package_table