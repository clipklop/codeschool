# **
# An app to email users about Weather Forecasts.
# **


import requests, json


def get_emails():
    try:
        emails = {}
        emails_file = open('emails.txt', 'r')

        for line in emails_file:
            (email, name) = line.strip().split(";")
            emails[email] = name

    except FileNotFoundError as e:
        print(e)
    else:
        return emails


def get_schedule():
    try:
        schedule_file = open('schedule.txt', 'r')
        schedule = schedule_file.read()
        schedule_file.close()

    except FileNotFoundError as e:
        print(e)
    else:
        return schedule


def get_weather():
    url = "http://api.openweathermap.org/data/2.5/forecast?id=524901&units=metric&APPID=5617a2122cca993a3ddcbe401adb149d"
    r = requests.get(url)
    rj = r.json()
    city = rj['city']['name']
    description = rj['list'][9]['weather'][0]['description']
    temp_min = rj['list'][1]['main']['temp_min']
    temp_max = rj['list'][1]['main']['temp_max']

    return city, description, temp_min, temp_max


def main():
    emails = get_emails()
    print(emails)

    schedule = get_schedule()
    print(schedule)

    print(get_weather())


main()