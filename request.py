url = 'https://rec.caltech.edu/booking/reserve'

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
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

bodies = {
    4: {
        '5-6': "bId=f20965ff-b976-4e7d-9ad5-f7759b823407&fId=9502d610-f2ae-4881-a307-8403712d2d8f&aId=57b4c6de-1dc1-41fc-a562-ed3072d8d4aa&tsId=aaeea0a2-54cd-4f3e-b02b-1024fd65d755&tsiId=73329e31-d759-4f12-accb-db48c2002aec&y={date.year}&m={date.month}&d={date.day}&t=&v=0",
        '6-7': "bId=f20965ff-b976-4e7d-9ad5-f7759b823407&fId=9502d610-f2ae-4881-a307-8403712d2d8f&aId=6c4d4642-10fa-481e-a5e6-2cd29ffeddee&tsId=3a8fa6c9-a086-4dd1-9c2c-7e596dca8a8c&tsiId=a0ddfe67-d9b0-4489-b337-1b2ef6054b31&y={date.year}&m={date.month}&d={date.day}&t=&v=0"
    },
    6: {
        '4-5': "bId=f20965ff-b976-4e7d-9ad5-f7759b823407&fId=ce97fc31-bd28-4d79-a884-79962fbf179b&aId=dd77f214-dbf1-4f48-a653-fc130dca1bdc&tsId=2d2f5b9b-1187-4100-bd2b-8604917dce43&tsiId=00000000-0000-0000-0000-000000000000&y={date.year}&m={date.month}&d={date.day}&t=&v=0",
        '5-6': "bId=f20965ff-b976-4e7d-9ad5-f7759b823407&fId=ce97fc31-bd28-4d79-a884-79962fbf179b&aId=a511e63d-742c-4862-8573-851641b7f4ed&tsId=aaeea0a2-54cd-4f3e-b02b-1024fd65d755&tsiId=d0b35142-48e1-470c-bc26-e1df9161e6e9&y={date.year}&m={date.month}&d={date.day}&t=&v=0"
    }
}

