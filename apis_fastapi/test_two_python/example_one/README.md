# How the code works

The code begins in the function "start_processing". This function takes two arguments: path_file_read and path_file_write, which are the paths to the CSV file to be read and the CSV file to be written, respectively.

Inside the function, the "_csv_reader" function is called with path_file_read as an argument. This function reads the CSV file and returns a list containing the data from the file. Next, the returned list from the "_csv_reader" function is assigned to the variable list_from_reader. Now, with this values, the "_first_order_data" function is called to create the first_prev_data list. 

So, the first_prev_data list is then passed to the "_sort_and_extend_list" function. This function sorts the list and performs some additional operations to extend it, and returns a new list called final_list_sorted_to_save that contains the processed data, next, the "_change_name_key" function is called with final_list_sorted_to_save as an argument to modifies the list by changing the name of a third key.

Finally, the "_csv_writer" function is called with final_list_sorted_to_save and path_file_write as arguments to writes the final data to the CSV file specified by path_file_write.

The return value of "_csv_writer" is then returned by the start_processing function, which is a message indicating the success or failure of the processing operation. Overall, this code reads a large CSV file, performs some data processing operations on it, and writes the processed data to a new CSV file.

In brief, the computational complexity of this code start with O(n) and ends with O(n * k) in the worst case.