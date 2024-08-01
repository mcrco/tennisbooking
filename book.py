import requests
import argparse
from datetime import datetime, timedelta
from request import url, headers, bodies
import curlify

def book_court(court, timeslot, date):
    try:
        data = bodies[court][timeslot].format(date=date)
    except:
        print(f"Invalid court or timeslot: court {court} from {timeslot}.")
        return False

    response = requests.post(url=url, headers=headers, data=data)
    # print(curlify.to_curl(response.request))
    if response.status_code == 200 and response.json()['Success']:
        print(f"Successfully booked court {court} from {timeslot}.")
        return True
    else:
        print(f"Failed to book court {court} from {timeslot}: status code", response.status_code)
        return False

def main():
    # Get date for default date values (2 days in advance)
    current_date = datetime.now()
    future_date = current_date + timedelta(days=2)

    formatted_date = future_date.strftime("%m/%d/%Y")
    print('Booking court for', formatted_date)

    parser = argparse.ArgumentParser(
            prog='Court 6 Tennis Court Booker',
            description='Books court 4 or 6 given date and time slot'
            )

    parser.add_argument('-y', '--year', type=str, default=future_date.year)
    parser.add_argument('-m', '--month', type=str, default=future_date.month)
    parser.add_argument('-d', '--day', type=str, default=future_date.day)

    args = parser.parse_args()

    with open('./cookie') as f:
        cookie = f.readline().strip()
    headers.update({'cookie': cookie})

    success = book_court(6, '5-6', args)
    if not success:
        book_court(4, '5-6', args)
    success = book_court(6, '6-7', args)
    if not success:
        book_court(4, '6-7', args)

if __name__ == '__main__':
    main()
