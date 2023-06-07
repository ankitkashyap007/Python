from truecallerpy import search_phonenumber

# Paste id here after login
id = "You id here"

# To know your installation id run `truecallerpy -i` on terminal or command prompt

# Get user input
searchN = input('Enter number : ')

# search_phonenumber( "PHONE_NUMBER","COUNTRY_CODE","INSTALLATION_ID")
data = search_phonenumber(searchN,"IN", id)

# Print received
# print(data)

# Response variable
response = ''

# Checking Name receive or not
if data["data"][0]["name"] != '':
    name = data["data"][0]["name"]
    response = f'Name: {name}\nMobile Number: {searchN}'

# Checking Carrier receive or not
if data["data"][0]["phones"][0]["carrier"] !='':
    Carrier = data["data"][0]["phones"][0]["carrier"]
    response += f'\nCarrier: {Carrier}'

# Checking Email receive or not
if len(data["data"][0]["internetAddresses"]) > 0 :
    email = data["data"][0]["internetAddresses"][0]["id"]
    response += f"\nEmail: {email}"

# Print Response
print(response)