"""_summary_

    Identify Holidays: Identify holidays in a given year.

"""

import pandas as pd
from datetime import date
import holidays
from workalendar.america import Chile

cl_holidays: holidays.Chile = holidays.Chile(years=[2022])
print(cl_holidays)

range_of_dates: pd.DatetimeIndex = pd.date_range("2021-01-01", "2022-12-31")
data_frame_result = pd.DataFrame(index=range_of_dates, data={"is_holidays": [date in cl_holidays for date in range_of_dates]})
print(data_frame_result)

holidays_list: list = []
for holidays in holidays.Chile(years=[2022]).items():
    print(holidays)
    holidays_list.append(holidays)
    
holidays_data_frame: pd.DataFrame = pd.DataFrame(holidays_list, columns=['date', 'name'])
print(holidays_data_frame)

# ----------------------------------------------------------------------------
# workalendar
cl_calendar: Chile = Chile()
data_frame_chile: pd.DataFrame = pd.DataFrame(cl_calendar.holidays(2022), columns=["date","holidays"])
print(data_frame_chile)

result_working_day: bool = cl_calendar.is_working_day(date(2022, 9, 18))
print(result_working_day)