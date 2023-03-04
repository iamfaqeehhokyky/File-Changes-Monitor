# File-Changes-Monitor

This code is meant to monitor any changes made to a folder and notify the user of the changes. For instance, if you have a folder where you save all your school assignments, you can use this code to monitor the folder and know when a new assignment is added or an old one is removed.

## How it works

The code uses the `os` and `time` modules to monitor the folder. The `os` module provides a way to interact with the file system and the `time` module is used to add a delay of 5 seconds before checking for changes.

The code works by getting the initial state of the folder and then continuously checking for changes every 5 seconds. If there are any changes, it will notify the user by printing the changes and updating the initial state.

## Your Tasks

# Task 1:

Create a `for` loop to loop over the initial state of the folder. If a file is found that was not there before, return the file and append it to the `added_files` list.

For example, if you have a folder where you save all your school assignments, and you add a new assignment named `math_assignment.pdf`, the code should detect the addition and notify you.

# Task 2:

Create a `for` loop to loop over the current state of the folder. If a file is found that was there before but is not there now, return the file and append it to the `removed_files` list.

For example, if you have a folder where you save all your school assignments, and you delete an assignment named `english_assignment.docx`, the code should detect the deletion and notify you.

## Hints

Here are some hints to help you complete the tasks:

# Hint for Task 1:

Use a `for` loop to loop over the initial_state list.
Use the `os.path.join()` method to join the folder path and file name.
Use the `os.path.isfile()` method to check if the path is a file.
If the path is a file and it's not in the `current_state` list, append it to the `added_files` list.

# Hint for Task 2:

Use a `for` loop to loop over the current_state list.
Use the `os.path.join()` method to join the folder path and file name.
Use the `os.path.isfile()` method to check if the path is a file.
If the path is a file and it's not in the `initial_state` list, append it to the `removed_files` list.
Good luck with the project!

## After working the tasks (1 & 2)

If any changes are detected, the function prints the changes (added and removed files) and updates the initial state to the current state.

To test the function, run the program with the folder path. The function will continuously monitor the folder for changes and notify you when changes are detected. A sample of what your console should look like have been attached below.

![image](https://user-images.githubusercontent.com/73473767/222281407-f85ccd36-8c2b-41f8-a3e6-f4c2fd72f4c1.png)
