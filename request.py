url = 'https://rec.caltech.edu/booking/reserve'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.5',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'sec-fetch-site': 'same-origin',
    'x-requested-with': 'XMLHttpRequest',
    'origin': 'https://rec.caltech.edu',
    'connection': 'keep-alive',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'priority': 'u=1',
    'te': 'trailers'
}

bodies = {
    4: {
        '5-6': "bId=f20965ff-b976-4e7d-9ad5-f7759b823407&fId=9502d610-f2ae-4881-a307-8403712d2d8f&aId=57b4c6de-1dc1-41fc-a562-ed3072d8d4aa&tsId=aaeea0a2-54cd-4f3e-b02b-1024fd65d755&tsiId=73329e31-d759-4f12-accb-db48c2002aec&y={date.year}&m={date.month}&d={date.day}&t=&v=0",
        '6-7': "bId=f20965ff-b976-4e7d-9ad5-f7759b823407&fId=9502d610-f2ae-4881-a307-8403712d2d8f&aId=15777de2-d804-4f71-9fd0-a9e0f66a4701&tsId=3a8fa6c9-a086-4dd1-9c2c-7e596dca8a8c&tsiId=07a2ea45-fc75-462b-9032-63c56dc9add5&y={date.year}&m={date.month}&d={date.day}&t=&v=0"
    },
    6: {
        '4-5': "bId=f20965ff-b976-4e7d-9ad5-f7759b823407&fId=ce97fc31-bd28-4d79-a884-79962fbf179b&aId=dd77f214-dbf1-4f48-a653-fc130dca1bdc&tsId=2d2f5b9b-1187-4100-bd2b-8604917dce43&tsiId=00000000-0000-0000-0000-000000000000&y={date.year}&m={date.month}&d={date.day}&t=&v=0",
        '5-6': "bId=f20965ff-b976-4e7d-9ad5-f7759b823407&fId=ce97fc31-bd28-4d79-a884-79962fbf179b&aId=a511e63d-742c-4862-8573-851641b7f4ed&tsId=aaeea0a2-54cd-4f3e-b02b-1024fd65d755&tsiId=d0b35142-48e1-470c-bc26-e1df9161e6e9&y={date.year}&m={date.month}&d={date.day}&t=&v=0"
    }
}

