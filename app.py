import random
import string
import requests
import names

# get the redirected link from url
def get_redirected_link(url):    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # get the redirected link
    response = requests.get(url, headers=headers)
    return response.url



def extract_unique_id(url):
    return url.split('/')[6].replace('=', '')

def generate_random_name():
    return names.get_full_name()

def generate_random_email():
    emaildomains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'aol.com']
    return generate_random_name().replace(' ','').lower() + '@' + random.choice(emaildomains)
    
   

def generate_random_southafricanid():
    return ''.join(random.choice(string.digits) for i in range(13))

def generate_random_phone():
    return '+27' + ''.join(random.choice(string.digits) for i in range(9))

def generate_password(unique_id):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))

def generate_5digits_otp():
    return ''.join(random.choice(string.digits) for i in range(5))
    
def GenerateDataPayload(unique_id):
    return {
        'mail': generate_random_email(),
        'password': generate_password(unique_id),
        'phone': generate_random_phone(),
        'otp': generate_5digits_otp(),
        'id': unique_id,
        'identification':generate_random_southafricanid()
    }


def main():    
    # make control c exit the program
    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)    
    bCompleted = False    
    amountOfPOSTs = 0
    formsCompleted = 0

    while not bCompleted:
        url = get_redirected_link('https://bit.ly/3pTAzlY')
        unique_id = extract_unique_id(url)
        data = GenerateDataPayload(unique_id)

        # print data 
        print('Posting the following payload to the server:',data)

        # make the POST request to the server
        response = requests.post('https://oximetalona.com.mx/archivos/ups/h2/'+unique_id+'=/password.php', data={'email':data['mail']})
        amountOfPOSTs += 1

        # check if the POST request was successful
        if response.status_code == 200:
            print('[+] Successfully sent POST request to server. Total POST requests: ' + str(amountOfPOSTs))
        else:
            print('[-] Failed to send POST request to server. Total POST requests: ' + str(amountOfPOSTs))
            bCompleted = True

        # send post to https://oximetalona.com.mx/archivos/ups/h2/send/send_phone.php
        response = requests.post('https://oximetalona.com.mx/archivos/ups/h2/send/send_phone.php', data={'identification':data['identification'],'phone':data['phone']})
        amountOfPOSTs += 1

        # check if the POST request was successful
        if response.status_code == 200:
            print('[+] Successfully sent POST request to server. Total POST requests: ' + str(amountOfPOSTs))
        else:
            print('[-] Failed to send POST request to server. Total POST requests: ' + str(amountOfPOSTs))
            bCompleted = True
        
        # send post to https://oximetalona.com.mx/archivos/ups/h2/send/send_login.php
        response = requests.post('https://oximetalona.com.mx/archivos/ups/h2/send/send_login.php', data={'mail':data['mail'],'password':data['password']})
        amountOfPOSTs += 1

        # check if the POST request was successful
        if response.status_code == 200:
            print('[+] Successfully sent POST request to server. Total POST requests: ' + str(amountOfPOSTs))
        else:
            print('[-] Failed to send POST request to server. Total POST requests: ' + str(amountOfPOSTs))
            bCompleted = True
        
        # send post to https://oximetalona.com.mx/archivos/ups/h2/app/otp.php
        response = requests.post('https://oximetalona.com.mx/archivos/ups/h2/app/otp.php', data={'otp':data['otp']})

        amountOfPOSTs += 1

        # check if the POST request was successful
        if response.status_code == 200:
            print('[+] Successfully sent POST request to server. Total POST requests: ' + str(amountOfPOSTs))
        else:
            print('[-] Failed to send POST request to server. Total POST requests: ' + str(amountOfPOSTs))
            bCompleted = True

        formsCompleted += 1

        print('[+] Successfully completed ' + str(formsCompleted) + ' forms.')

if __name__ == '__main__':
    main()



