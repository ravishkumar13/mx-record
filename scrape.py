import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
import json

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Domains').sheet1

#domains = sheet.get_all_records()

def mxrecord(domain):
    url = 'https://api.exana.io/dns/'+domain+'/mx'
    print(url)
    #url = 'https://intodns.com/'+domain
    response = requests.get(url)
    text_data = response.text
    #print(text_data)
    data = json.loads(text_data)
    print(data)

    for mx in data['answer']:
    	mx_records = mx['rdata']
        #records_string = str(mx_records)
    	return mx_records

for i in range(2, 6):
    domain = sheet.cell(i,1).value
    print(domain)
    final_data = mxrecord(domain)
    print(final_data)
    sheet.update_cell(i,2,final_data)
    
