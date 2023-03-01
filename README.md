# File-Changes-Monitor

A Python program that monitors changes to files and directories and notifies the user.

## Explaining the code

In this program, the `monitor_changes` function takes a `folder_path` parameter, which is the path to the folder that should be monitored. This folder has been created for you and named `test_folder`. The function uses the `os` and `time` modules to get the initial state of the folder, wait for 5 seconds, get the current state of the folder, and find the differences between the initial and current states.

## After working the tasks (1 & 2)

If any changes are detected, the function prints the changes (added and removed files) and updates the initial state to the current state.

To test the function, run the program with the folder path. The function will continuously monitor the folder for changes and notify you when changes are detected. A sample of what your console should look like have been attached below.

![image](https://user-images.githubusercontent.com/73473767/222281407-f85ccd36-8c2b-41f8-a3e6-f4c2fd72f4c1.png)
