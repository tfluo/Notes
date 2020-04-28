# RSA encrypt & decrypt in Django
## start django project
```sh
django-admin startproject cryptodemo
cd cryptodemo
django-admin startapp api
```
## create folder for static files
```sh
mkdir static
```

## create private and public key
```sh
openssl genrsa -out rsa_1024_pri.pem 1024
openssl rsa -pubout -in rsa_1024_pri.pem -out rsa_1024_pub.pem
```

## edit crytpo/setting.py
```python
#...
    'DIRS': [os.path.join(BASE_DIR, 'static')], 'DIRS': [os.path.join(BASE_DIR, 'static')],
#...
STATICFILES_DIRS = [os.path.join(BASE_DIR,"static"),]
with open('rsa_1024_pri.pem') as f:
    RSA_PRIVATE_KEY = ''.join(f.readlines())
with open('rsa_1024_pub.pem') as f:
    RSA_PUBLIC_KEY = ''.join(f.readlines())
```

## download jsencrypt.min.js & jquery.min.js into static
* download [jsencrypt.min.js](https://github.com/travist/jsencrypt/blob/master/bin/jsencrypt.min.js)
* download [jquery.min.js](https://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js)

## edit static/crypto.html
```html
<!DOCTYPE html>
{% load staticfiles %}
<html lang="en" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>Crypto</title>
        <!-- #引入加密的js包 -->
        <script src="/static/jsencrypt.min.js"></script>
        <!-- #引入必要的jquery包 -->
        <script src="/static/jquery.min.js"></script>
    </head>
    <body>
        <!-- #隐藏的input，用来将公钥引入前端 -->
        <input type="hidden" name="public_key" id="public_key" value="{{ public_key }}">
        <!-- #表单 -->
        <form method="post" id="CryptoForm" action="/crypto/">
            {% csrf_token %} <!-- #保证POST传输的   -->
            <table>密码：</table>
            <input type="text" id="id_password" name="id_password">
            <!-- #按钮，有一个点击的事件，调用下面的 doPost()函数 -->
            <input  onclick="doPost()" id="sub" type="button" value="提交">
        </form>
        <script type="text/javascript">
            <!-- #点击事件的函数 -->
            function doPost()
            {
                //#取出用户输入的密码
                var password_old = document.getElementById("id_password").value;
                //#实例化一个加密对象
                var encrypt = new JSEncrypt();
                //#取出公钥
                encrypt.setPublicKey($('#public_key').val());
                //#对旧密码进行加密
                var password_new = encrypt.encrypt(password_old);
                //#将新密码覆盖到旧密码
                document.getElementById("id_password").value = password_new;
                //#进行提交
                CryptoForm.submit();
            }
        </script>
    </body>
</html>
```

## edit crypto/urls.py
```python
from django.conf.urls import include
from api import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^crypto/', views.crypto),
    url(r'^getpass/', views.get_pass),
]
```

## edit api/views.py
```python
from django.http import HttpResponseNotFound, HttpResponse
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from django.conf import settings
import base64

def crypto(request):
    values = {}
    values['public_key'] = settings.RSA_PUBLIC_KEY
    if request.method == 'GET':
        return render(request, 'crypto.html', values)

    elif request.method == 'POST':
        password_new = request.POST.get('id_password')
        with open('password.txt', 'w') as f:
            f.write(password_new)
        return HttpResponse('OK.')
    else:
        return HttpResponseNotFound('')

def get_pass(request):
    random_gen = Random.new().read
    RSA.generate(1024, random_gen)
    rsakey = RSA.importKey(settings.RSA_PRIVATE_KEY)
    cipher = PKCS1_v1_5.new(rsakey)
    with open('password.txt') as f:
      password_encrypt = f.readline()
    password = cipher.decrypt(base64.b64decode(password_encrypt), random_gen)
    return HttpResponse('password is %s.' % password)
```
