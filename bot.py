import requests
from settings import URL
from time import sleep
from bored.main import Bored


welcome_msg = '''
<b>Assalomu alaykum aziz qadirdonim !</b>

🌟 Tasodifiy maslahat Kom_IT_Auto Bot-ga xush kelibsiz! 🌟

Siz uchun faqat donolik va ko'rsatmalar dozasini olishga tayyor bo'ling. Mana bu botdan maksimal darajada foydalanish bo'yicha tezkor qo'llanma:
1. <b>/start:</b> Issiq kutib olish xabarini olish va bot bilan qanday aloqa qilish bo'yicha ko'rsatmalar olish uchun ushbu buyruqdan foydalaning.

2. <b>/random:</b> O'z-o'zidan his qilyapsizmi? Ushbu buyruqni hozirda sizga kerak bo'lgan narsa bo'lishi mumkin bo'lgan tasodifiy maslahat uchun foydalaning.

3. <b>/sport:</b> Sport bilan bog'liq maslahatlar kerakmi? Ushbu buyruqni kiriting va Bot sizga sport bilan bog'liq donolikka xizmat qiladi.

4. <b>/education:</b> Agar siz ta'lim masalalariga rahbarlik qilmoqchi bo'lsangiz, ushbu buyruqdan qimmatbaho maslahat olish uchun foydalaning.

5. <b>/recreational:</b> Bo'sh vaqt va dam olish faoliyatida maslahatlar uchun bu buyruqni kiriting va ba'zi bir fikrli takliflardan zavqlaning.

6. <b>/social:</b>Ijtimoiy munosabatlar bo'yicha maslahatlarni qidiryapsizmi? Ijtimoiy tajribangizni oshiradigan maslahatlarni olish uchun ushbu buyruqdan foydalaning.

7. <b>/diy:</b>DIY loyihasini rejalashtirish? O'zingizning harakatlaringiz uchun foydali maslahatlarni olish uchun ushbu buyruqni kiriting.

8. <b>/cooking:</b> Mazali taomni qamchilashga tayyormisiz? Ovqat pishirish uchun ushbu buyruqdan ham yaxshi tajribangizni yanada yaxshiroq qiladi.

9. <b>/relaxation:</b>Stressni his qilyapsizmi? Sizga yoqishga yordam beradigan dam olish usullari bo'yicha maslahat uchun ushbu buyruqni kiriting.

10. <b>/busywork:</b>O'zingizni ishg'ol qilish uchun biror narsa kerakmi? Ushbu buyruqni samarali va vazifalarni bajarish bo'yicha maslahatlar uchun foydalaning.

Yodingizda bo'lsin, agar siz boshqa biron bir matnni kiritsangiz, bot sizni mavjud buyruqlarga qaytarish uchun xato xabarini beradi.
'''


def get_last_update(url: str) -> dict:
    endpoint = '/getUpdates'
    url += endpoint
    
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()['result']

        if len(result) != 0:
            return result[-1]

        else:
            return 404
    
    return response.status_code

def send_message(url: str, chat_id: int, text: str):
    endpoint = '/sendMessage'
    url += endpoint

    payload = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'HTML'
    }
    requests.get(url, params=payload)


def main(url: str):
    bored = Bored()
    last_update_id = -1
    while True:
        curr_update = get_last_update(url)

        if curr_update['update_id'] != last_update_id:
            user = curr_update['message']['from']
            text = curr_update['message'].get('text')

            if text is None:
                send_message(url, user['id'], 'send text message')
            elif text == '/start':
                send_message(url, user['id'], welcome_msg)
            elif text == '/random':
                advice = bored.get_activity()['activity']
                send_message(url, user['id'], advice)
            elif text == '/education':
                advice = bored.get_activity_by_type('education')['activity']
                send_message(url, user['id'], advice)
            elif text == '/recreational':
                advice = bored.get_activity_by_type('recreational')['activity']
                send_message(url, user['id'], advice)
            elif text == '/social':
                advice = bored.get_activity_by_type('social')['activity']
                send_message(url, user['id'], advice)
            elif text == '/diy':
                advice = bored.get_activity_by_type('diy')['activity']
                send_message(url, user['id'], advice)
            elif text == '/cooking':
                advice = bored.get_activity_by_type('cooking')['activity']
                send_message(url, user['id'], advice)
            elif text == '/relaxation':
                advice = bored.get_activity_by_type('relaxation')['activity']
                send_message(url, user['id'], advice)
            elif text == '/busywork':
                advice = bored.get_activity_by_type('busywork')['activity']
                send_message(url, user['id'], advice)
            else:
                send_message(url, user['id'], 'error message')

            last_update_id = curr_update['update_id']

        sleep(0.5)


main(URL)