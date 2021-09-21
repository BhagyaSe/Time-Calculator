# This entrypoint file to be used in developmeBBnt. Start by reading README.md
from time_calculator import add_time
#from cleanCode import add_time
from unittest import main


print(add_time("3:30 PM", "2:12")) #test_same_period #"5:42 PM"
print(add_time("11:55 AM", "3:12")) #test_different_period #"3:07 PM"
print(add_time("9:15 PM", "5:30")) #test_next_day #"2:45 AM (next day)"
print(add_time("11:40 AM", "0:25")) #test_period_change_at_twelve #"12:05 PM"
print(add_time("2:59 AM", "24:00")) #test_twenty_four #"2:59 AM (next day)"
print(add_time("5:01 AM", "0:00")) #test_no_change #"5:01 AM"
print(add_time("3:30 PM", "2:12", "Monday")) #test_same_period_with_day #"5:42 PM, Monday"
print(add_time("2:59 AM", "24:00", "saturDay")) #test_twenty_four_with_day #"2:59 AM, Sunday (next day)"
print(add_time("8:16 PM", "466:02")) #test_high_duration #"6:18 AM (20 days later)"
print(add_time("8:16 PM", "466:02", "tuesday")) #test_high_duration_with_day #"6:18 AM, Monday (20 days later)"
print(add_time("11:59 PM", "24:05")) #test_two_days_later #"12:04 AM (2 days later)"
print(add_time("11:59 PM", "24:05", "Wednesday")) #test_two_days_later_with_day #"12:04 AM, Friday (2 days later)"



# Run unit tests automatically
#main(module='test_module', exit=False)
