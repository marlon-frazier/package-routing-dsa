import datetime
from csv_loader import read_csv_file, create_address_mapping, load_package_information
from loaded_truck_data import truck_one, truck_two, truck_three

# The DeliverySystem class represents the overall delivery system
class DeliverySystem:
    def __init__(self):
        # Load necessary data from CSV files
        self.distance_data = read_csv_file("csv_files/distance.csv")
        self.address_data = create_address_mapping("csv_files/address.csv")
        self.pkg_table = load_package_information("csv_files/package.csv")

    def fetch_address_data(self, location):
        # Retrieve address information from the address data
        return self.address_data.get(location)

    def calculate_distance(self, x_value, y_value):
        try:
            # Get the distance between two addresses from the distance data
            gap = float(self.distance_data[x_value][y_value])
        except (ValueError, IndexError):
            # If distance is not found, try reversing the order of addresses
            try:
                gap = float(self.distance_data[y_value][x_value])
            except (ValueError, IndexError):
                # If distance is still not found, set a default large value for distance
                gap = float('inf')  # Set a default large value for distance
        return gap

    def optimize_route_for_truck(self, delivery_truck):
        packages_remaining = [self.pkg_table.lookup(packageID) for packageID in delivery_truck.packages]
        delivery_truck.packages.clear()

        # Create a list of package addresses in the order they appear in the package table
        package_addresses = [self.fetch_address_data(pkg.address) for pkg in packages_remaining]

        # Calculate the initial route distance and assign it to the current distance
        current_distance = sum(self.calculate_distance(package_addresses[i], package_addresses[i + 1])
                               for i in range(len(package_addresses) - 1))

        # Iterate until no further improvements can be made
        while True:
            improved = False

            for i in range(1, len(package_addresses) - 2):
                for j in range(i + 1, len(package_addresses) - 1):
                    # Calculate the new distance after swapping two edges
                    new_distance = current_distance - self.calculate_distance(package_addresses[i - 1],
                                                                              package_addresses[i]) \
                                   - self.calculate_distance(package_addresses[j],
                                                             package_addresses[j + 1]) \
                                   + self.calculate_distance(package_addresses[i - 1],
                                                             package_addresses[j]) \
                                   + self.calculate_distance(package_addresses[i],
                                                             package_addresses[j + 1])

                    # If the new distance is shorter, update the route and set the flag to indicate improvement
                    if new_distance < current_distance:
                        package_addresses[i:j + 1] = reversed(package_addresses[i:j + 1])
                        current_distance = new_distance
                        improved = True

            # Exit the loop if no further improvements were made
            if not improved:
                break

        # Update truck and package information based on the optimized route
        truck_address = self.fetch_address_data(delivery_truck.address)
        current_time = delivery_truck.depart_time

        for address in package_addresses:
            proximity = self.calculate_distance(truck_address, address)
            next_parcel = min(packages_remaining, key=lambda pkg: self.fetch_address_data(pkg.address) == address)

            delivery_truck.packages.append(next_parcel.ID)
            packages_remaining.remove(next_parcel)
            delivery_truck.mileage += proximity
            truck_address = address
            current_time += datetime.timedelta(hours=proximity / 18)
            next_parcel.delivery_time = current_time
            next_parcel.departure_time = delivery_truck.depart_time

        delivery_truck.time = current_time

    def display_all_packages_info(self, time):
        # Get information for all packages at a given time
        try:
            for pkg in sorted(self.pkg_table.values(), key=lambda x: x.ID):
                pkg.update_status(time)
                print(str(pkg))
        except ValueError:
            print("Invalid input. Please try again.")

    def display_single_package_info(self, time, package_id):
        # Get information for a single package at a given time
        try:
            pkg = self.pkg_table.lookup(package_id)
            if pkg:
                pkg.update_status(time)
                print(str(pkg))
            else:
                print(f"No package found with ID: {package_id}")
        except ValueError:
            print("Invalid input. Please try again.")

    def print_menu(self):
        # Print the menu options for the delivery system
        print("=== Western Governors University Parcel Service (WGUPS) ===")
        print("Please select an option:")
        print("1. Get info for all packages at a particular time")
        print("2. Get info for a single package at a particular time")
        print("3. Exit Program")

    def run_delivery_system(self):
        # Run the delivery system
        # Perform the delivery process for each truck
        self.optimize_route_for_truck(truck_one)
        self.optimize_route_for_truck(truck_two)
        truck_three.depart_time = min(truck_one.time, truck_two.time)
        self.optimize_route_for_truck(truck_three)

        # Print the overall summary of the delivery
        print('------------------------------')
        print('WGUPS Routing Program')
        print('C950 Performance Assessment')
        total_mileage = truck_one.mileage + truck_two.mileage + truck_three.mileage
        print(f'Route was completed in {total_mileage} miles.')
        print('------------------------------\n')

        # Display the menu and handle user input
        self.print_menu()
        choice = input("Enter the option number: ")

        while choice != "3":
            if choice == "1":
                try:
                    # Get time from user and retrieve information for all packages at that time
                    user_time = input(
                        "Please enter a time to check the status of all packages. Use the following format, HH:MM: ")
                    (h, m) = user_time.split(":")
                    converted_time = datetime.timedelta(hours=int(h), minutes=int(m))
                    self.display_all_packages_info(converted_time)
                except ValueError:
                    print("Invalid input. Please try again.")

            elif choice == "2":
                try:
                    # Get time and package ID from user and retrieve information for that package at that time
                    user_time = input(
                        "Please enter a time to check the status of a single package. Use the following format, HH:MM: ")
                    (h, m) = user_time.split(":")
                    converted_time = datetime.timedelta(hours=int(h), minutes=int(m))
                    package_id = int(input("Enter the numeric package ID: "))
                    self.display_single_package_info(converted_time, package_id)
                except ValueError:
                    print("Invalid input. Please try again.")

            else:
                print("Invalid choice. Please try again.")

            print()
            self.print_menu()
            choice = input("Enter the option number: ")

        print("Exiting the program. Thank you!")
