from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business import api

my_app_id = '{app-id}'
my_app_secret = '683212320577996|VzSdjaY88jFNcC4U_PGozfj7FAs'
my_access_token = 'EAAJtYMOsmcwBO1udvb1d89iEuSrVnC4e8YZBXRcZCNwms4P3Gul6aLlzzikGqRjeMZCsfbG7ZCmSoP5H0DthB8fOVXoZB1j8StjlSg5SMZBmU9jWkSRguKi7ZCgPUI2SZB0qQnMaaZBxGPSZBBuXL3cWVYbqR4tXRNSecsMb92JZAUmOe6P8tZCjkqK6UIxHDTItdUSHT7IpD2llVIegGszb1IbTmokPRAZDZD'
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
my_account = AdAccount('act_{{adaccount-id}}')
campaigns = my_account.get_campaigns()
print(campaigns)

