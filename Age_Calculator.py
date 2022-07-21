#Import libraries.
from datetime import date
import calendar
from dateutil import relativedelta
from datetime import date
from datetime import datetime
import datetime
from dateutil.relativedelta import relativedelta

BirthDate=input("Enter date of birth in MM/DD/YYY format.")

one_year_from_now = datetime.datetime.now()
date_formated = one_year_from_now.strftime("%m/%d/%Y")
start_date = datetime.datetime.strptime(BirthDate, "%m/%d/%Y")
end_date = datetime.datetime.strptime(date_formated, "%m/%d/%Y")
delta = relativedelta(end_date, start_date)
print('Years, Months, Days between two dates is')
print(delta.years, 'Years,', delta.months, 'months,', delta.days, 'days')