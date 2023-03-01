import os
import time


def monitor_changes(folder_path):
    """
    Monitor changes to files and directories and notify the user
    """
    # Get the initial state of the folder
    initial_state = os.listdir(folder_path)

    while True:
        # Wait for 5 seconds
        time.sleep(5)

        # Get the current state of the folder
        current_state = os.listdir(folder_path)

        # Find the differences between the initial and current states
        added_files = []
        removed_files = []

        """Task 1:"""
        # Create a for loop to loop over the initial state of the file
        # Return the file if nothing was found
        # Append the returned value inside the added_files list.
        # Write your code for the first task beneath this line

        # Write your code for the first task above this line

        """Task 2:"""
        # Create a for loop to loop over the current state of the file
        # Return the file if nothing was found
        # Append the returned value inside the removed_files list.
        # Write your code for the second task beneath this line

        # Write your code for the second task above this line

        # Print the changes and update the initial state
        if added_files or removed_files:
            print(f"Changes detected at {time.ctime()}:")
            if added_files:
                print(f"Added files: {added_files}")
            if removed_files:
                print(f"Removed files: {removed_files}")
            print("="*40)
            initial_state = current_state


# Test the function with a folder path
folder_path = "./test_folder"
monitor_changes(folder_path)
