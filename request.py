import requests
import argparse
from datetime import datetime, timedelta

# Get date for default date values (2 days in advance)
current_date = datetime.now()
future_date = current_date + timedelta(days=2)

parser = argparse.ArgumentParser(
        prog='Court 6 Tennis Court Booker',
        description='Books court 6 from 4-6 given month year and date'
        )

parser.add_argument('-y', '--year', type=str, default=future_date.year)
parser.add_argument('-m', '--month', type=str, default=future_date.month)
parser.add_argument('-d', '--day', type=str, default=future_date.day)
# parser.add_argument('-fo', '--four', action='store_true', default=False)
# parser.add_argument('-fi', '--five', action='store_true', default=False)

args = parser.parse_args()

url = 'https://rec.caltech.edu/booking/reserve'

with open('./cookie') as f:
    cookie = f.readline().strip()

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': cookie,
    'dnt': '1',
    'origin': 'https://rec.caltech.edu',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}

timeslot_45_data = {
    'bId': 'f20965ff-b976-4e7d-9ad5-f7759b823407',
    'fId': 'ce97fc31-bd28-4d79-a884-79962fbf179b',
    'aId': 'dd77f214-dbf1-4f48-a653-fc130dca1bdc',
    'tsId': '2d2f5b9b-1187-4100-bd2b-8604917dce43',
    'tsiId': '00000000-0000-0000-0000-000000000000',
    'y': args.year,
    'm': args.month,
    'd': args.day,
    't': '',
    'v': '0'
}

timeslot_56_data = {
    'bId': 'f20965ff-b976-4e7d-9ad5-f7759b823407',
    'fId': 'ce97fc31-bd28-4d79-a884-79962fbf179b',
    'aId': 'a511e63d-742c-4862-8573-851641b7f4ed',
    'tsId': 'aaeea0a2-54cd-4f3e-b02b-1024fd65d755',
    'tsiId': 'd0b35142-48e1-470c-bc26-e1df9161e6e9',
    'y': args.year,
    'm': args.month,
    'd': args.day,
    't': '',
    'v': '0'
}

timeslot_67_data = {
    'bId': 'f20965ff-b976-4e7d-9ad5-f7759b823407',
    'fId': 'ce97fc31-bd28-4d79-a884-79962fbf179b',
    'aId': 'cb4436ee-7a73-4c83-af29-f3511bfeb155',
    'tsId': '3a8fa6c9-a086-4dd1-9c2c-7e596dca8a8c',
    'tsiId': 'f5765830-c9f2-4014-8281-cfee7d672440',
    'y': args.year,
    'm': args.month,
    'd': args.day,
    't': '',
    'v': '0'
}

# if args.four:
# response = requests.post(url, headers=headers, data=timeslot_45_data)
# print('Request for 4-5: ', response.json()['Success'])

# if args.five:
response = requests.post(url, headers=headers, data=timeslot_56_data)
print('Request for 5-6: ', response.json()['Success'])

response = requests.post(url, headers=headers, data=timeslot_67_data)
print('Request for 5-6: ', response.json()['Success'])
