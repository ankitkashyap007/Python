from truecallerpy import search_phonenumber
id = "You id here"
# To know your installation id run `truecallerpy -i` on terminal or command prompt
searchN = input('Enter number ')
# search_phonenumber( "PHONE_NUMBER","COUNTRY_CODE","INSTALLATION_ID")
data = search_phonenumber(searchN,"IN", id)
print(data)

number = searchN
response = number

if data["data"][0]["name"] != '':
    name = data["data"][0]["name"]
    response = f'Name: {name}\nMobile Number: {response}'

if data["data"][0]["phones"][0]["carrier"] !='':
    Carrier = data["data"][0]["phones"][0]["carrier"]
    response += f'\nCarrier: {Carrier}'
    
if len(data["data"][0]["internetAddresses"]) > 0 :
    email = data["data"][0]["internetAddresses"][0]["id"]
    response += f"\nEmail: {email}"

print(response)

# ==> search_phonenumber("+12093031250","IN", id)