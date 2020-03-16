age = int(input())
convert = input()

if convert == "to minutes":
    from_years_to_minutes = 365 * 24 * 60
    print(age * from_years_to_minutes)
else:
    from_years_to_seconds = 365 * 24 * 60 * 60
    print(age * from_years_to_seconds)
