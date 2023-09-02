weather_c = {
    "Monday":12,
    "Tuesday":14,
    "Wednesday":15,
    "Thrusday":21,
    "Friday":14,
    "Saturday":22,
    "Sunday":24,
}
weather_f = {days: tem*9/5+ 32 for days,tem in weather_c.items()}
print(weather_f)