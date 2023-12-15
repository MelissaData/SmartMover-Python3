import json
from threading import local
import requests
import argparse
import urllib.parse

def main():
  base_service_url = "https://smartmover.melissadata.net/"
  service_endpoint = "V3/WEB/SmartMover/doSmartMover"

  # Create an ArgumentParser object
  parser = argparse.ArgumentParser(description='Smart Mover command line arguments parser')

  # Define the command line arguments
  parser.add_argument('--license', '-l', type=str, help='License key')
  parser.add_argument('--pafid', type=str, help='PAF ID')
  parser.add_argument('--company', type=str, help='Company')
  parser.add_argument('--fullname', type=str, help='Full Name')
  parser.add_argument('--addressline1', type=str, help='Address Line 1')
  parser.add_argument('--city', type=str, help='City')
  parser.add_argument('--state', type=str, help='State')
  parser.add_argument('--postalcode', type=str, help='Postal Code')
  parser.add_argument('--country', type=str, help='Country')

  # Parse the command line arguments
  args = parser.parse_args()

  # Access the values of the command line arguments
  license = args.license
  pafid = args.pafid
  company = args.company
  fullname = args.fullname
  addressline1 = args.addressline1
  city = args.city
  state = args.state
  postalcode = args.postalcode
  country = args.country

  call_api(base_service_url, service_endpoint, license, pafid, company, fullname, addressline1, city, state, postalcode, country)

def get_contents(base_service_url, request_query):
    url = urllib.parse.urljoin(base_service_url, request_query)
    response = requests.get(url)
    obj = json.loads(response.text)
    pretty_response = json.dumps(obj, indent=4)

    print("\n================================== OUTPUT ==================================\n")

    print("API Call: ")
    for i in range(0, len(url), 70):
        if i + 70 < len(url):
            print(url[i:i+70])
        else:
            print(url[i:len(url)])
    print("\nAPI Response:")
    print(pretty_response)

def call_api(base_service_url, service_endpoint, license, pafid, company, fullname, addressline1, city, state, postalcode, country):
    print("\n================= WELCOME TO MELISSA SMART MOVER CLOUD API =================\n")

    should_continue_running = True
    while should_continue_running:
        input_pafid = ""
        input_company = ""
        input_fullname = ""
        input_addressline1 = ""
        input_city = ""
        input_state = ""
        input_postalcode = ""
        input_country = ""
        if not pafid and not company and not fullname and not addressline1 and not city and not state and not postalcode and not country:
            print("\nFill in each value to see results")
            input_pafid = input("Pafid: ")
            input_company = input("Company: ")
            input_fullname = input("Full Name: ")
            input_addressline1 = input("Addressline1: ")
            input_city = input("City: ")
            input_state = input("State: ")
            input_postalcode = input("Postal: ")
            input_country = input("Country: ")
        else:
            input_pafid = pafid
            input_company = company
            input_fullname = fullname
            input_addressline1 = addressline1
            input_city = city
            input_state = state
            input_postalcode = postalcode
            input_country = country

        while not input_pafid or not input_company or not input_addressline1 or not input_city or not input_state or not input_postalcode or not input_country:
            print("\nFill in each value to see results")
            if not input_pafid:
                input_pafid = input("\nPafid: ")
            if not input_company:
                input_company = input("\nCompany: ")
            if not input_fullname:
                input_fullname = input("\nFull Name: ")
            if not input_addressline1:
                input_addressline1 = input("\nAddressline1: ")
            if not input_city:
                input_city = input("\nCity: ")
            if not input_state:
                input_state = input("\nState: ")
            if not input_postalcode:
                input_postalcode = input("\nPostal: ")
            if not input_country:
                input_country = input("\nCountry: ")

        inputs = {
            "format": "json",
            "pafid": input_pafid,
            "comp": input_company,
            "full": input_fullname,
            "a1": input_addressline1,
            "city": input_city,
            "state": input_state,
            "postal": input_postalcode,
            "ctry": input_country
        }

        print("\n================================== INPUTS ==================================\n")
        print(f"\t   Base Service Url: {base_service_url}")
        print(f"\t  Service End Point: {service_endpoint}")
        print(f"\t              Pafid: {input_pafid}")
        print(f"\t            Company: {input_company}")
        print(f"\t          Full Name: {input_fullname}")
        print(f"\t       Addressline1: {input_addressline1}")
        print(f"\t               City: {input_city}")
        print(f"\t              State: {input_state}")
        print(f"\t        Postal Code: {input_postalcode}")
        print(f"\t            Country: {input_country}")

       # Create Service Call
        # Set the License String in the Request
        rest_request = f"&id={urllib.parse.quote_plus(license)}"

        # Set the Input Parameters
        for k, v in inputs.items():
            rest_request += f"&{k}={urllib.parse.quote_plus(v)}"

        # Build the final REST String Query
        rest_request = service_endpoint + f"?{rest_request}"

        # Submit to the Web Service.
        success = False
        retry_counter = 0

        while not success and retry_counter < 5:
            try: #retry just in case of network failure
                get_contents(base_service_url, rest_request)
                print()
                success = True
            except Exception as ex:
                retry_counter += 1
                print(ex)
                return

        is_valid = False;

        if (pafid is not None) and (company is not None) and (fullname is not None) and (addressline1 is not None) and (city is not None) and (state is not None) and (postalcode is not None) and (country is not None):
            inputline = pafid + company + fullname + addressline1 + city + state + postalcode + country
        else:
            inputline = None

        if inputline is not None and inputline != "":
            is_valid = True
            should_continue_running = False

        while not is_valid:
            test_another_response = input("\nTest another record? (Y/N)")
            if test_another_response != '':
                test_another_response = test_another_response.lower()
                if test_another_response == 'y':
                    is_valid = True
                elif test_another_response == 'n':
                    is_valid = True
                    should_continue_running = False
                else:
                    print("Invalid Response, please respond 'Y' or 'N'")

    print("\n================== THANK YOU FOR USING MELISSA CLOUD API ===================\n")

main()
