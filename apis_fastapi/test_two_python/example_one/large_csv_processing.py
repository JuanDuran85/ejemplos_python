"""_summary_

    Working with large CSV files

"""

def _csv_reader(path_file: str) -> list[dict]:
    """Reads a CSV file and returns a list of dictionaries with data information.

    Args:
        path_file (str): The file path of the CSV file.

    Raises:
        Exception: If there is an error while reading the file.

    Returns:
        list[dict]: A list of dictionaries, where each dictionary represents a row in the CSV file.
    """
    try:
        with open(path_file, "r", encoding="utf8") as file_read:
            lines: list[str] = file_read.readlines()
            headers: list[str] = lines[0].rstrip().split(',')
            return [dict(zip(headers, line.rstrip().split(','))) for line in lines[1:]]
    except Exception as e:
        print("Error on reading: ", e)
        raise e

def _csv_writer(data: list[dict[str, str]], path: str) -> str:
    """Write data to a CSV file.

    Args:
        data (list[dict[str, str]]): A list of dictionaries containing data information to write to the CSV file.
        path (str): The file path and name to save the CSV file.

    Returns:
        str: A message indicating the successful completion of the write operation.

    Raises:
        Exception: If an error occurs during the writing process.
    """
    print(path)
    try:
        with open(path, 'w', encoding="utf8") as total_file:
            headers = data[0].keys()
            total_file.write(','.join(headers) + "\n")
            for text_line in data:
                total_file.write(','.join(text_line[one_header] for one_header in headers) + "\n")
        return "ok"
    except Exception as e:
        print(f"Error on writing: {e}")
        raise e

def _first_order_data(data_in: list[dict[str, str]]) -> dict[str, dict[str, list[dict[str, str]]]]:
    """Process the data and return a dictionary by song name and dates.

    Args:
        data_in (list[dict[str, str]]): List of dictionaries with data information.

    Returns:
        dict[str, dict[str, list[dict[str, str]]]]: A dictionary containing the processed data, 
        grouped by song name and dates.
    """

    data_table_by_song: dict[str, dict[str, list[dict[str, str]]]] = {}
    for data_obj in data_in:
        data_from_song: list = []
        song_obj: str = str(data_obj['Song'])
        date_obj: str = str(data_obj['Date'])
        number_of_plays_obj: str = str(data_obj['Number of Plays'])

        if (not data_table_by_song.get(song_obj)):
            data_table_by_song.setdefault(song_obj, {})
        if (not data_table_by_song[song_obj].get(date_obj)):
            data_table_by_song[song_obj].setdefault(date_obj, [data_obj])
        else:
            data_from_song: list = data_table_by_song[song_obj].get(
                date_obj) or []
            value_of_plays: str = str(
                int(data_from_song[0]['Number of Plays']) + int(number_of_plays_obj))
            data_from_song[0].update(
                {'Song': song_obj, 'Date': date_obj, 'Number of Plays': value_of_plays})
            data_table_by_song[song_obj][date_obj] = data_from_song
    return data_table_by_song

def _sort_and_extend_list(first_prev_data: dict[str, dict[str, list[dict[str, str]]]]) -> list[dict[str, str]]:
    """Sorts and extends a list of dictionaries.

    This function takes a dictionary `first_prev_data` as input, which contains nested dictionaries and lists of dictionaries.
    It sorts the keys of the nested dictionaries and creates a new dictionary with the sorted keys.
    Then, it extends the final list with the values from the first dictionary in each nested dictionary.

    Args:
        first_prev_data (dict[str, dict[str, list[dict[str, str]]]]): A dictionary with nested dictionaries and lists of dictionaries.

    Returns:
        list[dict[str, str]]: A list of dictionaries containing the values from the first dictionary in each nested dictionary.
    """
    final_list = []
    for value in first_prev_data.values():
        keys_from_value = sorted(value.keys())
        sorted_final_dict = {i: value[i] for i in keys_from_value}
        final_list.extend(value[0] for value in sorted_final_dict.values())

    return final_list

def _change_name_key(final_list_sorted_to_save: list[dict[str, str]]) -> None:
    """Change the name of the key in the dictionary.

    This function iterates over a list of dictionaries and changes the name of the key 'Number of Plays' to 'Total Number of Plays for Date'.

    Args:
        final_list_sorted_to_save (list[dict[str, str]]): A list of dictionaries containing key-value pairs.

    Returns:
        None
    """
    for value in final_list_sorted_to_save:
        value['Total Number of Plays for Date'] = value['Number of Plays']
        del value['Number of Plays']

def start_processing(path_file_read: str, path_file_write: str) -> str:
    """Process a large CSV file.

    This function reads a large CSV file, performs some data processing operations,
    and writes the processed data to a new CSV file.

    Args:
        path_file_read (str): The path to the CSV file to be read.
        path_file_write (str): The path to the CSV file to be written.

    Returns:
        str: A message indicating the success or failure of the processing operation.
    """
    list_from_reader = _csv_reader(path_file_read)
    first_prev_data = _first_order_data(list_from_reader)
    final_list_sorted_to_save = _sort_and_extend_list(first_prev_data)
    _change_name_key(final_list_sorted_to_save)
    return _csv_writer(final_list_sorted_to_save, path_file_write)

if __name__ == '__main__':
    file_path_to_read: str = "test_two_python/uploads_temp/csv_file.csv"
    file_path_to_save: str = "test_two_python/uploads_temp/csv_file_saved.csv"
    final_result: str = start_processing(file_path_to_read, file_path_to_save)
    print(final_result)