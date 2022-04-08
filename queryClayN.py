
# %%


#%%
# %%
def getSubmissionKey(cookie):
    import requests
    import json
    from requests.structures import CaseInsensitiveDict

    url = "https://www.claynation.io/api/form/FormSubmissionKey"

    headers = CaseInsensitiveDict()
    headers["accept"] = "application/json, text/plain, */*"
    headers["accept-encoding"] = "gzip, deflate, br"
    headers["accept-language"] = "en-GB,en-US;q=0.9,en;q=0.8"
    headers["Content-Length"] = "0"
    headers["Content-Type"] = "application/json"
    headers["cookie"] = cookie
    headers["origin"] = "https://www.claynation.io"
    headers["referer"] = "https://www.claynation.io/baked-reg"
    #headers["sec-ch-ua"] = "" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100""
    headers["sec-ch-ua-mobile"] = "?0"
    #headers["sec-ch-ua-platform"] = """ "macOS" """
    headers["sec-fetch-dest"] = "empty"
    headers["sec-fetch-mode"] = "cors"
    headers["sec-fetch-site"] = "same-origin"
    headers["user-agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
    headers["x-csrf-token"] = "BQQYSHH631loNTNjMmYxODYzNWQ0ZDAwOWQ2OTM1ZGYzYTdjY2Q3"


    resp = requests.post(url, headers=headers)

    print(resp.status_code)

    key = json.loads(resp.content)
    #print("Key->", key)
    return key
# %%
def ip_address():
    from faker import Faker  
    import time
    faker = Faker()  
    ip_addr = faker.ipv4() 
    print(ip_addr)
    return ip_addr

def get_word_list():
    import time
    import csv
    import re
    file = open("results.csv")
    csvreader = csv.reader(file)
    header = next(csvreader)
    rows = []
    i = 0
    try:
        for row in csvreader:
            word = row[0].split('|')[2]
            s = re.sub(r'[^\w\s]','', word)
            rows.append(s)
    except:
        #print("done")
        file.close()
        return rows
    file.close()
    return rows
# %%
def saveFormdata(cookie, key, address, random_text):
    import requests
    import json
    from requests.structures import CaseInsensitiveDict

    word_t = random_text
    ip_address_t =  ip_address()
    print(ip_address_t)
    address_t = address
    url = "https://www.claynation.io/api/form/SaveFormSubmission"

    headers = CaseInsensitiveDict()
    headers["accept"] = "application/json, text/plain, */*"
    headers["accept-encoding"] = "gzip, deflate, br"
    headers["accept-language"] = "en-GB,en-US;q=0.9,en;q=0.8"
    headers["content-length"] = "2"
    headers["Content-Type"] = "application/json"
    headers["cookie"] = cookie
    headers["origin"] = "https://www.claynation.io"
    headers["referer"] = "https://www.claynation.io/baked-reg"
    #headers["sec-ch-ua"] = "" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100""
    headers["sec-ch-ua-mobile"] = "?0"
    #headers["sec-ch-ua-platform"] = ""macOS""
    headers["sec-fetch-dest"] = "empty"
    headers["sec-fetch-mode"] = "cors"
    headers["sec-fetch-site"] = "same-origin"
    headers["user-agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
    headers["x-csrf-token"] = "BQQYSHH631loNTNjMmYxODYzNWQ0ZDAwOWQ2OTM1ZGYzYTdjY2Q3"

    data_payload = {"key": key,"formId":"624dab6d6a29a07e100e06cb",
    "collectionId":"624daa75a529b116a242186d",
    "objectName":"page-section-624daa75a529b116a242186f",
    #"form":"{\"text-yui_3_17_2_1_1649257123675_7763\":\"addr1q9eflych950x8cwuxt0w2lq83f69gg87gl7ahr349375pwdl74gnlxv3xqm5vxrl3vel7xhth6x0hk79mwvs50xw8uxqwfvx5q\",\"textarea-yui_3_17_2_1_1649257123675_7764\":\"Submit Address\",\"select-42f18e55-2594-4860-98b8-00d79d0767a4\":\"10\",\"select-a5c42c51-b35a-4bb2-b1b0-02dd18150961\":\"No, I am registering for the pubic mint \",\"hidden-f9c908f5-006a-4702-b456-e37da5e4f870\":\"122.182.219.124\"}",
    "form":"{\"text-yui_3_17_2_1_1649257123675_7763\":\""+address_t+"\",\"textarea-yui_3_17_2_1_1649257123675_7764\":\""+word_t+"\",\"select-42f18e55-2594-4860-98b8-00d79d0767a4\":\"10\",\"select-a5c42c51-b35a-4bb2-b1b0-02dd18150961\":\"No, I am registering for the pubic mint \",\"hidden-f9c908f5-006a-4702-b456-e37da5e4f870\":\""+ip_address_t+"\"}",
    "pagePermissionTypeValue":1,"pageTitle":"Baked Registration","pageId":"624daa75a529b116a242186d","contentSource":"c","pagePath":"/baked-reg"}

    #print(data)
    final_payload = json.dumps(data_payload)
    print(final_payload)
    resp = requests.post(url, headers=headers, data=final_payload)
    print("Done with the response from SaveFormdata")
    print(resp.status_code)

#%%
import json
import time
import random 
with open('addresses.json', 'r') as f:
  data = json.load(f)

random_words =   get_word_list()
random_words = random_words[1:18000]
not_executed_list = []
for i in range(714,7500) :
    try:
        wallet_key = "Amar"+str(i)
        address = data[wallet_key]
        print(address)
        word = random_words[i+2]
        cookie = "crumb=BQQYSHH631loNTNjMmYxODYzNWQ0ZDAwOWQ2OTM1ZGYzYTdjY2Q3; ss_cvr=024fb47c-4aca-44d5-af9f-9630c75efaf4|1649327756052|1649410983220|1649421709115|8; ss_cvt=1649421709115"
        subkey = getSubmissionKey(cookie)
        print(subkey['key'])
        saveFormdata(cookie, subkey['key'], address, word)
        #print(formdata)
        print(i)
        time.sleep(random.randint(5, 10))
    except KeyError:
        print("Key error")
        not_executed_list.append(i)
        print(not_executed_list)
        time.sleep(15)
print(not_executed_list)
# %%
