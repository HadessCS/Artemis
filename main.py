import json
import os
import zipfile
import os
import shutil
from apkutils import APK
import sys
import re
from ipwhois import IPWhois
import tldextract
from validators import domain as validate_domain
import shutil
import requests
from colorama import init, Fore, Style
from termcolor import colored
import emoji
from tqdm import tqdm
import time
from shodan import Shodan

import virustotal_python
from pprint import pprint




# Initialize colorama
init()


# TI Config file
config = {}
config_path='./config'

# Get all local environment variables
env_vars = os.environ




progress_bar_length = 20  # Number of characters in the progress bar
initialize_msg = Fore.YELLOW + Style.DIM + "Initializing ... " + emoji.emojize(":rocket:")
print(initialize_msg)






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
    """
    print(banner)



def cli_show_banner():
    banner = """
                                  _      
   /\         _              (_)     
  /  \   ____| |_  ____ ____  _  ___ 
 / /\ \ / ___)  _)/ _  )    \| |/___)
| |__| | |   | |_( (/ /| | | | |___ |
|______|_|    \___)____)_|_|_|_(___/ 
                                     

    --help  show help
    --path  required path of apk file
    --manifest show manifest informations
    --infra find all infra addresses included ip,domain ex. --infra ip,domain
    --whoise whoise all infra included ip,domain ex. --whoise ip,domain
    --output set output files ex. --output out.txt
    """
    print(banner)



def is_valid_ip_address(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or int(part) > 255 or part.startswith("0") or part.startswith("255"):
            return False
    return True

def exit_script():
    if os.path.exists('./uncompress'):
        shutil.rmtree('./uncompress')
    exit()


def is_valid_domain(domain):
    patterns_to_reject = [
        r'^R',
        r'^X\.org',
        r'^JSON\.org',
        r'^\.com',
        r'^Android',
        r'^\.properties',
        r'medi',
        r'init',
        r'final',
        r'\.below',
        r'\bwinSize\.width\b',
        r'\bMesh\.vertexBuffer\b',
        r'\bthescientificcommunity\.capitalismin\b',
        r'\btheequationsdownload\.regularlydeveloperabove\b',
    ]

    domain_extensions = ['.com', '.ir', '.io', '.tk', '.net', '.org', '.gov', '.edu', '.mil', '.int', '.eu', '.biz', '.info', '.name', '.pro', '.museum', '.coop', '.aero', '.jobs', '.travel', '.mobi', '.cat', '.tel', '.xxx', '.asia', '.post', '.arpa', '.xyz', '.club', '.site', '.online', '.store', '.app', '.tech', '.blog', '.news', '.media', '.agency', '.digital', '.services', '.academy', '.shop', '.company', '.consulting', '.design', '.events', '.marketing', '.software', '.solutions', '.world', '.us', '.ca', '.uk', '.de', '.fr', '.au', '.in', '.it', '.es', '.nl', '.ch', '.se', '.no', '.fi', '.dk', '.at', '.be', '.ru', '.pl', '.cz', '.hu', '.ro', '.gr', '.tr', '.br', '.mx', '.ar', '.za', '.cn', '.jp', '.kr', '.sg', '.hk', '.tw', '.my', '.vn', '.th', '.id', '.ph', '.sa', '.ae', '.eg', '.ng', '.ke', '.gh', '.tn', '.ma', '.co', '.cl', '.pe', '.ec', '.ve']

    for pattern in patterns_to_reject:
        if re.search(pattern, domain):
            return False


    for extension in domain_extensions:
        if domain.endswith(extension):
            return True



def append_to_file(file_path, content):
    try:
        with open(file_path, 'a') as file:
            file.write(content + '\n')
        #print("Content appended to the file successfully.")
    except IOError:
        print(f"An error occurred while appending content to the file: {file_path}")



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
        starting_msg = colored("Starting ... ", "red") + Style.BRIGHT + emoji.emojize(":fire:")
        print(starting_msg)
        #print(f"ZIP file extracted successfully to {extract_path}")
    except Exception as e:
        print(f"Error extracting ZIP file: {e}")




def read_all_environment_variables():
    env_variables = {}
    for key, value in os.environ.items():
        env_variables[key] = value
    return env_variables



def read_config_file(file_path):
    all_env_variables = read_all_environment_variables()
    if os.path.exists('./config'):
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith("shodan="):
                    config['shodan'] = line.split('=')[1]
                else:
                    for key, value in all_env_variables.items():
                        if key == 'shodan':
                            config['shodan'] = value
                            break

                if line.startswith("virustotal="):
                    config['virustotal'] = line.split('=')[1]
                else:
                    for key, value in all_env_variables.items():
                        if key == 'virustotal':
                            config['virustotal'] = value
                            break
                        
                if line.startswith("urlscan="):
                    config['urlscan'] = line.split('=')[1]
                else:
                    for key, value in all_env_variables.items():
                        if key == 'urlscan':
                            config['urlscan'] = value
                            break
                       
                if line.startswith("criminalip="):
                    config['criminalip'] = line.split('=')[1]
                else:
                    for key, value in all_env_variables.items():
                        if key == 'criminalip':
                            config['criminalip'] = value
                            break
    else:
        print(Fore.RED + Style.DIM + 'Config File Nout Found!')
        for key, value in all_env_variables.items():
            if key == 'shodan':
                print(f"The value of {key} is {value}")
                config['shodan'] = value
                break
            if key == 'urlscan':
                print(f"The value of {key} is {value}")
                config['urlscan'] = value
                break
            if key == 'virustotal':
                print(f"The value of {key} is {value}")
                config['virustotal'] = value
                break
            if key == 'criminalip':
                print(f"The value of {key} is {value}")
                config['criminalip'] = value
                break



    
    return config



def perform_domain_lookup(domain):
    print(domain)
    perform_domain_lookup_output = ""

    data = {
        # Your JSON data here
    }

    if config['urlscan']:
        try:
            print("[-]Urlscan:")
            api_url = f"https://urlscan.io/api/v1/search/?q=domain:{domain}"
            response = requests.get(api_url)

            if response.status_code == 200:
                result = response.json()
                if result['total'] > 0:
                    print(Fore.GREEN + Style.DIM + '[*]Title: ' + result['results'][0]['page']['title'])
                    print(Fore.GREEN + Style.DIM + '[*]Server: ' + result['results'][0]['page']['server'])
                    print(Fore.GREEN + Style.DIM + '[*]IP: ' + result['results'][0]['page']['ip'])
                    print(Fore.GREEN + Style.DIM + '[*]ASN: ' + result['results'][0]['page']['asn'])
                    print(Fore.GREEN + Style.DIM + '[*]ASN Name: ' + result['results'][0]['page']['asnname'])
                    perform_domain_lookup_output = perform_domain_lookup_output + result['results'][0]
                else:
                    print("No WHOIS information found for domain: {domain}")
        except Exception as e:
            pass
            #print("An error occurred: {str(e)}")
    if config['shodan']:
        try:
            print("[-]Shodan:\n")
            api = Shodan(config['shodan'])
            data=api.dns.domain_info(domain=domain, history=False, type=None, page=1)

            # Convert the data to a formatted JSON string
            formatted_json = json.dumps(data, indent=4)

            # Print the formatted JSON
            print(Fore.GREEN + Style.DIM + formatted_json)

            #results = api.host(domain)
            #print(results)
            perform_domain_lookup_output = perform_domain_lookup_output + str(data)
            
        except shodan.APIError as e:
            print("Error: {e}")

    if config['virustotal']:
        try:
            print("[-]VirusTotal:\n")
            with virustotal_python.Virustotal(config['virustotal']) as vtotal:
                resp = vtotal.request(f"domains/{domain}")
                # Convert the data to a formatted JSON string
                formatted_json = json.dumps(resp.data, indent=4)

                # Print the formatted JSON
                print(Fore.GREEN + Style.DIM + formatted_json)

            perform_domain_lookup_output = perform_domain_lookup_output + resp.data

        except vt.APIError as e:
            pass
            # print(f"Error: {e}")

    return perform_domain_lookup_output



def perform_ip_lookup(ip):
    perform_ip_lookup_output = ""
    data = {
        # Your JSON data here
    }
    try:
        print("[-]Manual Method:")

        ip_info = IPWhois(ip)
        result = ip_info.lookup_rdap()

        # Convert the data to a formatted JSON string
        formatted_json = json.dumps(result, indent=4)

        # Print the formatted JSON
        print(formatted_json)

        print(f"[*]WHOIS information for IP: {ip}")
        print("[*]Organization: ", result['asn_description'])
        print("[*]Country: ", result['asn_country_code'])
        print("--------------------")
        perform_ip_lookup_output = perform_ip_lookup_output + str(result)
        if False:
            try:
                print("[-]Shodan:\n")
                api = Shodan(config['shodan'])
                data=api.host(ip)

                # Convert the data to a formatted JSON string
                formatted_json = json.dumps(data, indent=4)

                # Print the formatted JSON
                print(Fore.GREEN + Style.DIM + formatted_json)

                #results = api.host(domain)
                #print(results)
                perform_ip_lookup_output = perform_ip_lookup_output + data    
                
            except shodan.APIError as e:
                print("Error: {e}")
        if config['criminalip']:
            print("[-]CriminalIP:\n")
            url = "https://api.criminalip.io/v1/ip/data?ip="+ip+"&full=true"
            payload={}
            headers = {
              "x-api-key": config['criminalip']
            }

            response = requests.request("GET", url, headers=headers, data=payload)

            # Convert the data to a formatted JSON string
            formatted_json = json.dumps(response.text, indent=4)

            # Print the formatted JSON
            print(Fore.GREEN + Style.DIM + formatted_json)


            perform_ip_lookup_output = perform_ip_lookup_output + str(response.text)



                            


    
    except whois.parser.PywhoisError as e:
        pass

    return perform_ip_lookup_output




                                    
   


def search_infra_address(directory_path):

    try:
        extract_zip(directory_path, 'uncompress')
        directory_path = './uncompress'
        unique_ips = set()
        unique_domains = set()
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='latin-1') as file:
                        content = file.read()
                        if ip_infra_flag:
                            ip_addresses = re.findall(r"\b(?:\d{2,3}\.){3}\d{1,3}\b", content)
                            if ip_addresses:
                                for ip in ip_addresses:
                                    if is_valid_ip_address(ip) and ip not in unique_ips:
                                      unique_ips.add(ip)
                                      print(ip)
                                      if output_switch:
                                        append_to_file(output_switch_name, ip)
                        elif domain_infra_flag:
                            domains = re.findall(r"(?<!\S)((?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,})(?!\S)", content)
                            if domains:
                                for domitem in domains:
                                    if is_valid_domain(domitem) and domitem not in unique_domains:
                                        print(domitem)
                                        unique_domains.add(domitem)
                                        if output_switch:
                                            append_to_file(output_switch_name, domitem)

                except Exception as e:
                    print(f"Error searching IP address in {file_path}: {e}")
      
    except Exception as e:
        print(f"Error searching IP addresses: {e}")
    




def whoise_infra(directory_path):
    try:
        extract_zip(directory_path, 'uncompress')
        directory_path = './uncompress'
        unique_ips = set()
        unique_domains = set()
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='latin-1') as file:
                        content = file.read()                        
                        
                        
                        if ip_whoise_flag:
                            ip_addresses = re.findall(r"\b(?:\d{2,3}\.){3}\d{1,3}\b", content)
                            for ip in ip_addresses:
                                #print(unique_ips)
                                if is_valid_ip_address(ip) and ip not in unique_ips:
                                    unique_ips.add(ip)
                                    lookup_ip_output=perform_ip_lookup(ip)
                                    if output_switch:
                                            append_to_file(output_switch_name, lookup_ip_output)

                        if  domain_whoise_flag:
                            domains = re.findall(r"(?<!\S)((?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,})(?!\S)", content)
                            for domitem in domains:
                                if is_valid_domain(domitem) and domitem not in unique_domains:
                                    unique_domains.add(domitem)
                                    lookup_domain_output=perform_domain_lookup(domitem)
                                    if output_switch:
                                            append_to_file(output_switch_name, lookup_domain_output)


            
                                                
                except Exception as e:
                    #print(f"Error searching address in {file_path}: {e}")
                    pass

    except Exception as e:
        #print(f"Error searching addresses: {e}")
        pass
    exit_script()









def option_1():
    print("You selected Option 1")
    apk_path = input("Input APK Path: ")
    manifest(apk_path)


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
    read_config_file(config_path)
    path = ""
    ip_whoise_flag = False
    domain_whoise_flag = False
    ip_infra_flag = False
    domain_infra_flag = False
    output_switch = False

    if 'path' in script_parameters:
        path = script_parameters['path']
    elif 'help' in script_parameters:
        cli_show_banner()
        exit_script()
    else:
        print("Path parameter not provided.")
        exit_script()

    if 'output' in script_parameters:
        if  script_parameters['output'] is None:
            output_switch = True
            output_switch_name = "output.txt"
        else:
            output_switch = True
            output_switch_name = script_parameters['output']
    if 'manifest' in script_parameters:
        manifest(path)
    if 'infra' in script_parameters:
        if  script_parameters['infra'] is None:
            ip_infra_flag = True
            domain_infra_flag = True
            search_infra_address(path)
        else:
            if ',' in script_parameters['infra']:
                infra_parameters = script_parameters['infra'].split(",")
                for parameter in infra_parameters:
                    print(parameter)
                    if parameter == "ip":
                        ip_infra_flag = True
                        search_infra_address(path)
                    if parameter == "domain":
                        domain_infra_flag = True
                        search_infra_address(path)

            else:
                if script_parameters['infra'] == "ip":
                    ip_infra_flag = True
                    search_infra_address(path)
                if script_parameters['infra'] == "domain":
                    domain_infra_flag = True
                    search_infra_address(path)


    if 'whoise' in script_parameters:
        if  script_parameters['whoise'] is None:
            ip_whoise_flag = True
            domain_whoise_flag = True
            whoise_infra(path)
        else:
            if ',' in script_parameters['whoise']:
                whoise_parameters = script_parameters['whoise'].split(",")
                if whoise_parameters[0] == "ip" or whoise_parameters[1] == "ip":
                    ip_whoise_flag = True
                    whoise_infra(path)
                if whoise_parameters[0] == "domain" or whoise_parameters[1] == "domain":
                    domain_whoise_flag = True
                    whoise_infra(path)
            else:
                if script_parameters['whoise'] == "ip":
                    ip_whoise_flag = True
                    whoise_infra(path)
                if script_parameters['whoise'] == "domain":
                    domain_whoise_flag = True
                    whoise_infra(path)



        path = script_parameters['path']

        # colorize
        print('whoise')
        # please complete this
        whoise_infra(path)
    if 'help' in script_parameters:
        cli_show_banner()
        exit_script()
    else:
        #show_banner()
        pass
        
    
else:
    show_banner()
    selected_option = input("Select an option (1, 2, or 3): ")
    if selected_option == "1":
        apk_path = input("Input APK File Path: ")
        manifest(apk_path)
        exit_script()
    else:
        print("Invalid option selected!")
    





