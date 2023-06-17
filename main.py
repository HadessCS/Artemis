import json
import os
import zipfile
import os
import shutil
from apkutils import APK
import sys
import re
from ipwhois import IPWhois


def show_banner():
    banner = """
	SSSS%%SSSSS%%%%S%SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS%%%%%%%%SSSS%%%%%%%%%%%%
	SS%%%%SSSSSS%%%%%%%SSSSSSSSSSSSSSSSSSS%SSSSSSSS%%SSSSSSSSSSSSSSS%%%%%SSSSSSSSS%%%SSSS%%%SS
	S%%%%%%%%S%%%%%SSSSSS%SSSS%SSS??%%SSSSSSSSSSSSSSSSSSS%%%SSSSS%%%SSS%%SSSSSSS%%%%%%%%%%%SSS
	%%%%%%%%%SS%%%SSSSSSS%S%%SSS*:,,,:;+?%SSS%%??????+;;::::;*SSSSSSSSSSSS%%SSS%%%%%%%%%%%SSSS
	S%%%SSS%SSSSS%SSSSSSS%%%%SS?,,,:::::::;*?+++;:::,,,,,::::::+%#SSSSSSSS%%%%%%%%%%%%%%%%SS%S
	%%S%%S%SSSSSSSSSSSSSSSSSSS#?.,::::::::::::;;;+++++;;:::::::::*SSSSSSSS%%%%%%%%%%S%%%%%SSSS
	SSS%%%SSSSSSSSSSSSSSSS%SSSSS:,::::::::::::::::::::;;++;;::::::;?#SSSSSSS%%SSSSSS%%%%%%%SSS
	%%%%%%SSSS%%SSSSSSSSSSS%SSS#S;,::::::::::::::::::::::::;;;::::::+SSSSSSSSSSSSSSS%%%%SS%%%%
	SS%%%%%%%%%%SSSSSSSSSSSSSSS%*?+::::::::::*%??*;::::::::::::::::::;%#SSSSSSS%SSSSSSSSS%%SSS
	SS%%%%%%%%%%SS%SSSSSSSSSS%+:::+*+;:::::;+S?++****+;::::::::::::::::*SSSSS%%%%SSSSSSSS%%SSS
	%S%%%%%%%%%%SS%SSSSSSSSS+:,:,,,:;+*****??+;;;;;;;+**+;::::::::::::::+SSS%SS%SSS%%SSSSSS%%%
	%%S%%%%S%%S%SSSSSSSSSS%;,::::::::::;;;:::::::::::;++**+;::::::::::;::;%SSSSSSS%SSSSSSSSS%%
	SS%%S%%S%SSSSSSSSSSSS%:,,,::::::::::::::::::::::::;++*?*+;::::::::::::;?#SSS%%SSSSSSSS%%%S
	SS%%%SSSSSSSSSSSSSSSS;,::;++++++++++;;::::::::::;;;++++*?++;::::::::::::?#SSSSS%S%%SS%%SSS
	S%%%%%%SSSSSSSSSSSS#?,;++;::::::::::;;+++;::::::;;+;+++++?+++;:::::::::::*SSSSSS%%%SSS%SSS
	%%%%%%%%%SSSSS%SSSS#*+?:::::::::::::::::;+**+;;;;;+++++++*?++++;::::::::::*SSS%%%SSSSS%%%%
	%%SSSS%%%%%%%SSSSSS#??:::::::::::::::::::::;*?*+;+++++++++*?*++++;:::::::::*SS%%SSSSSS%%%%
	%%SSSSSSSSSSSSSSSSSS#;;+:;+:::::::::;;;;;;;;;;+**+++++++++++?++++++;::::::::?S%S%SSSSSS%%%
	%%%%%%%SSSSSSS%SSSSS%++,;?S*:::::::::::+++++*+;;+?*+++++++++??++**+++;;:::::?SSSSSSSSSSSS%
	%%S%SSSSSSSSSSSSSSSS?*,:#+#S:::::::::;*+:+%%?+;;;;*?++++++++*%+++?*+++++;::?SSSSSSSSSSS%SS
	%%%SSSSSSSSSSSSSSSSS?+,;@#@%:::::::::*+.+S:*@@?;;;;+?*+++++++?+++*?++*++;+%SSSS%SSSSSSS%SS
	SSSSSSSS%%S%%SSSSSSS?;*:?##;:::::::;;*,.?@?S@#%;::;;;?*++++++?*+++??++++%SS%%SSS%SSSSSS%%%
	SSSS%SSS%%SS%SSSSSSS%:;+;;;:::::::;;;*:.;@@##%?;::;;;;??+++++??++++%**%SSSSSSSSSS%%SSSSS%%
	%SSSSSSSSSS%SSSSSSSSS+,,::::::::::;;;;*;,:*?**;:::;;;;;*?++++S%++++?SSSSSSSS%%SSSSSSS%%%SS
	%%SSSSSSSSSSSSSSSSSSSS;,:::;::::::::;:;++++++;::;;;;;;;;%?+?S#%+++++SSSSSSSSSSSSSS%%%%%SSS
	%%SSSSS%SSSSSSSSSSSSSSS;,::::::::::::::::;;::::;;;;;;;;;?#%SSSS++++;?SSSSSSSSSSS%SSSSS%SS%
	%%SSSSSSSSSSSSSSSSSSSSSS+::::::::::;;;::::::;;;;;;;;;;;;SSSSSS#++;;;+SSS%%%SSSSS%%SS%%%%%%
	%%%%S%SSSSSSSSSSSSSSSSSSS?;::;;::::;;;::;;;;;;;;;;;;;;+%#SSSSS#*;;++;%SSSSSSSSSS%%%%%%%%%%
	SSSSSSSS%SSSSSSSSSSSSSSSSSS?+;:;;;;;;;;;;;;;;;;;;;;;;??*?SSSSS#?;;++;*SSSS%SSSSS%%%SS%%%SS
	SSSSSSSSSSSSSSSSSSSSSSSSSSSSS%?*+;;;;;;;;;;;;;;;;;;;*?+***?S#S#%;+;;+;%SSSSSSSSS%%%%%%%SSS
	SSSSSSS%%SSSSSS%%%SSSSSSSSSSSSSSSSS%%%?????*;;;;;+**+++;;;::;;;%+;;;;;*#SSS%SSSS%%%%%%%SSS
	SSSSSSSSS%SSSSSS%%SSSSSSSSSSSSSSSSSSSSSSSSSS%++*+;:,,,,,:;;;;+;%*;;:;;;SS%%%%%%%%%%%SS%%%%
	SSS%S%%%SS%%%SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS?+:,.,,:;++++;;;++*%%::::::*SS%SSSSSSSS%%SSSSS
	SSSSS%SSSSS%%%%%%SSSSSSSSSSSSSSSSSSSSSSSSSS*...,;++;:::::::::;++%+::::::%SSSSSSSSSS%%%SSSS
	SSS%SSSSSS%%%SS%%SSSSSSSSS%SSSSSSSSSSSSSSS?.,:++;::::::::::;;+++*?::::::+SSSSSSSS%%%%SSSSS
	%%%%%%%SSSSSSSSS%SSSSSSSSSSSSSSSSSSSSSSSS#;:*+:::::::::;;;;++++++?+::::::?SSSSSSSS%%%%%SS%
	%%%%SSS%SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS?**+::::::;+**???????*+++*%::::::;SSSS%%%%%%%%%%%%
	%%%%%SS%%%%SSSSSSS%%SSSSSSSSSSSSSSSSSS%+::;::::;+????******?????*+?+::::::*#SSSSS%%%%%%%%%
	%%%%%%%SS%%%%%SSSSSSSSSSSSSSSSSSSSSSS?;::::::;*???*+++*********?%%*%;::;*?SSSS%SS%%%%%%%%S
	S%%%S%%SSS%%SSSSSSSSSSSSSSSSSSSSSSS#?:::::;;?%?***+;++***********?%S%?%SSSSSS%%%%%%%%%%%SS
	%%%%S%SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS;:::;+*%?**???*++**************%#SSSSSSS%%%%%%%S%%%%%%
	SSSSSS%SSSSSSSSSSSSSSSSSSSSSSSSSSS#?:::++*%?**?%?*++****************%#SS%%%%%SS%SSSSS%%%%S
	SSS%SS%%SSSSSSSSSSSSSSSSSSSSSSSSSSS;:;++*%?***S?**+*?****************%#SSSS%%%%SSSSSSS%%%S
	%S%%SSS%S%SSSSSSSSSSSSSSSSSSSSSSSS%:;++*%?***%%******???**************SSS%SSSSSSSSSSSSSSSS
	SS%%SSS%%%SSSSSSSSSSSSSSSSSSSSSSS#*;++*%?****S??**********************?#SSSSS%%SSS%SSSS%SS
	1) Read Manifest
	2) Find IP Address
	3) Whoise IP
    """
    print(banner)




def manifest(path):


	apk = APK.from_file(path).parse_resouce()

	m_xml = apk.get_manifest()
	print(m_xml)

	x = apk.get_dex_strings()
	print(x)


    	

def extract_zip(zip_path, extract_path):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
        print(f"ZIP file extracted successfully to {extract_path}")
    except Exception as e:
        print(f"Error extracting ZIP file: {e}")



def search_ip_address(directory_path):
    try:
        extract_zip(directory_path, 'uncompress')
        directory_path = './uncompress'
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='latin-1') as file:
                        content = file.read()
                        ip_addresses = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", content)
                        if ip_addresses:
                            print(f"IP Addresses found in {file_path}:")
                            for ip in ip_addresses:
                                print(ip)
                        else:
                            #print(f"No IP Addresses found in {file_path}.")
                            pass
                except Exception as e:
                    print(f"Error searching IP address in {file_path}: {e}")
    except Exception as e:
        print(f"Error searching IP addresses: {e}")


def whoise_infra(directory_path):
    try:
        extract_zip(directory_path, 'uncompress')
        directory_path = './uncompress'
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='latin-1') as file:
                        content = file.read()
                        #fix this for find better ip address and infrastrucutre like domain and subdomain
                        ip_addresses = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", content)
                        domains = re.findall(r"(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,63}", content)
                        subdomains = re.findall(r"(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+", content)
                        if ip_addresses:
                            print(f"IP Addresses found in {file_path}:")
                            for ip in ip_addresses:
                                print(ip)
                                ip_info = IPWhois(ip)
                                result = ip_info.lookup_rdap()
                                print(f"WHOIS information for IP: {ip}")
                                print("Organization:", result['asn_description'])
                                print("Country:", result['asn_country_code'])
                                print("City:", result['city'])
                                print("Latitude:", result['latitude'])
                                print("Longitude:", result['longitude'])
                                print("ASN:", result['asn'])
                                print("--------------------")
                        else:
                        	pass
                        #if domains:
                        #    print(f"Domain found in {file_path}:")
                        #    for domitem in domains:
                        #        print(domitem)
                        #else:
                        #	pass
                        #if subdomains:
                        #    print(f"Subdomain found in {file_path}:")
                        #    for subitem in subdomains:
                        #        print(subitem)
                        #else:
                            # print(f"No IP Addresses found in {file_path}.")
                        #    pass
                except Exception as e:
                    #print(f"Error searching IP address in {file_path}: {e}")
                    pass
    except Exception as e:
        #print(f"Error searching IP addresses: {e}")
        pass








# Specify the path to your .zip file
#zip_path = "sample.zip"

# Specify the destination path for extraction
#dest_path = "directory"

# Extract the .zip file
#extract_zip(zip_path, dest_path)




def option_1():
    print("You selected Option 1")
    apk_path = input("Input APK Path: ")
    manifest(apk_path)

def option_2():
    print("You selected Option 2")

def option_3():
    print("You selected Option 3")

# Display the banner
show_banner()




def find_parameters(script_args):
    parameters = {}

    i = 0
    while i < len(script_args):
        arg = script_args[i]

        if arg.startswith('--'):
            parameter = arg[2:]

            # Check if the parameter has a corresponding value
            if i + 1 < len(script_args) and not script_args[i + 1].startswith('--'):
                value = script_args[i + 1]
                parameters[parameter] = value
                i += 1
            else:
                parameters[parameter] = None

        i += 1

    return parameters

# Get all parameters and their values from script arguments
script_parameters = find_parameters(sys.argv[1:])

if sys.argv[1:]:
	path = ""

	if 'path' in script_parameters:
	    path = script_parameters['path']
	else:
	    print("Path parameter not provided.")
	    exit()


	# Example usage
	if 'manifest' in script_parameters:
	    manifest(path)
	if 'infra' in script_parameters:
		print('infra')
	if 'whoise' in script_parameters:
		print('infra')
		# please complete this
		whoise_infra(path)
	if 'help' in script_parameters:
		show_banner()
	else:
		pass
	
else:
	selected_option = input("Select an option (1, 2, or 3): ")
	# Trigger the function based on the selected option
	if selected_option == "1":
		apk_path = input("Input APK File Path: ")
		manifest(apk_path)
		exit()
	elif selected_option == "2":
	    option_2()
	elif selected_option == "3":
	    option_3()
	else:
	    print("Invalid option selected!")
	





