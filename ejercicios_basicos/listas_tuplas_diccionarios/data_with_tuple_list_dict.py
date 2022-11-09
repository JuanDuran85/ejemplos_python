
from dataclasses import dataclass


@dataclass
class KeysGeneral:
    """_summary_
        Type class interface.
    """
    key_1: str
    key_2: str
    key_3: int
    key_4: str
    key_5: str

list_of_tuplas: list[tuple] = [
    ('6', "2022-11-24", 111, 'abc_1', "12:00"),  # type: ignore
    ('6', "2022-11-28", 111, 'abc_1', "12:00"),  # type: ignore
    ('6', "2022-11-29", 111, 'abc_1', "12:00"),  # type: ignore
    ('1', "2022-11-30", 111, 'abc_1', "12:00"),  # type: ignore
    ('1', "2022-11-24", 111, 'abc_1', "12:00"),  # type: ignore
    ('1', "2022-11-28", 111, 'abc_1', "12:00"),  # type: ignore
    ('1', "2022-11-29", 111, 'abc_1', "12:00"),  # type: ignore
    ('9', "2022-11-30", 111, 'abc_1', "12:00"),  # type: ignore
    ('9', "2022-11-24", 111, 'abc_1', "12:00"),  # type: ignore
    ('9', "2022-11-28", 111, 'abc_1', "12:00"),  # type: ignore
    ('7', "2022-11-29", 111, 'abc_1', "12:00"),  # type: ignore
    ('7', "2022-11-30", 111, 'abc_1', "12:00")   # type: ignore
]

data_table_by_country: dict[str,list[str]] = {}

for data_obj in list_of_tuplas:
    data_from_country: list[str] = []
    second_value:str = str(data_obj[1])
    first_value: str = str(data_obj[0])

    if (not data_table_by_country.get(first_value)):
        data_table_by_country.setdefault(first_value, [second_value])
        continue
    
    data_from_country = data_table_by_country.get(first_value) or []
    data_from_country.append(second_value)
    data_table_by_country[first_value] = data_from_country
    
print(data_table_by_country)