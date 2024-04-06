hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
dur_hours = dura // 60
dur_mins = dura % 60

end_min = (mins + dur_mins) % 60
end_hour = ((hour + dur_hours) % 24) + 1

print(end_hour,end_min,sep=':')
