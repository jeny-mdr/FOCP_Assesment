import sys

#Function to analyze the file and print the required statistics
def cat_shelter(log_file):
    """
     Analyzes a cat shelter log file and prints relevant statistics.

     Returns:
        None
    """
    
    
    #Function to calculate_visits from log lines
    def calculate_visits(log_lines):
        """
        Calculates visits based on the log lines.

        Returns:
        Tuple containing:
        - cat_visits (int): Number of visits by owned cats.
        - other_cats (int): Number of visits by other cats.
        - total_time_in_house (int): Total time owned cats spent in the house (in minutes).
        - visit_duration (list): List of durations of each visit (in minutes).
        """

        cat_visits = 0
        other_cats = 0
        total_time_in_house = 0
        visit_duration = []

        for line in log_lines:
            line_parts = line.split(",")
            if line_parts[0] == "END":
                break

            cats, entry_time, exit_time = line_parts
            entry_time = int(entry_time)
            exit_time = int(exit_time)

            if cats == "OURS":
                cat_visits += 1
                total_time_in_house += exit_time - entry_time
                visit_duration.append(exit_time - entry_time)
            else:
                other_cats += 1

        return cat_visits, other_cats, total_time_in_house, visit_duration

    try:
        #Read the log file
        with open(log_file, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f'Cannot open "{log_file}"!')
        return
    except Exception as e:
        print(f'Error reading file: {e}')
        return
    

    # Calculate statistics from log lines
    cat_visits, other_cats, total_time_in_house, visit_duration = calculate_visits(lines)
    average_visit_length = sum(visit_duration) // len(visit_duration)
    longest_visit = max(visit_duration)
    shortest_visit = min(visit_duration)

    #Header
    header="\nLog File Analysis"
    header_design=("=")

    # Print the analysis results
    print(header)
    print(len(header)*header_design)
    print(f"\nCat Visits: {cat_visits}")
    print(f"Other Cats: {other_cats}")
    print(f"\nTotal Time in House: {total_time_in_house // 60} {'Hour' if total_time_in_house // 60 <= 1 else 'Hours'}, {total_time_in_house % 60} {'Minute' if total_time_in_house % 60 <= 1 else 'Minutes'}")
    print("\nAverage Visit Length: {:<2} Minutes".format(average_visit_length))
    print("Longest Visit:        {:<2} Minutes".format(longest_visit))
    print("Shortest Visit:       {:<2} Minutes".format(shortest_visit))


# Check if the correct number of command line arguments is provided
if len(sys.argv) != 2:
    print("Missing command line argument!")
else:
    log_file = sys.argv[1]

     # Call the cat_shelter function with the specified log file
    cat_shelter(log_file)



    
    

    
    
