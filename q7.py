def convert_time(seconds):
  if not isinstance(seconds, int) or seconds < 0 or seconds >= 86400:
    return "Invalid number of seconds."

  hours = seconds // 3600
  minutes = (seconds % 3600) // 60
  secs = seconds % 60

  period = "AM"
  if hours >= 12:
    period = "PM"
  hours = hours % 12
  if hours == 0:
    hours = 12

  return f"{hours} {minutes} {secs} {period}"

print(convert_time(19067))
