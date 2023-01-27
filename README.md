# gve_devnet_cisco_router_switch_simple_configurator
A simple portal to push Cisco IOS, IOS XR/XR, NXOS configurations to a Cisco enterprise device, using Python Netmiko. 


## Contacts
* Max Acquatella

## Solution Components
* Python Flask
* Netmiko

## Related Sandbox Environment
Access via SSH to a Cisco IOS, IOS-XE/XR, NX-OS device. 

## Limitations
THIS IS SAMPLE CODE. It is not intended to be used in production environments. It is limited to pushing VERY simple configurations to Cisco devices. Its intention is to demonstrate the Python Flask/Netmiko packages and its possibilities.

## Prerequisites
**Device SSH Credentials**: The code will access the device using SSH (Netmiko). SSH has to be configured in the device beforehand, please consult the available Cisco documentation.  


## Installation/Configuration
1. Clone this repository with `git clone [repository name]`
2. Set up a Python virtual environment. Make sure Python 3 is installed in your environment, and if not, you may download Python [here](https://www.python.org/downloads/). Once Python 3 is installed in your environment, you can activate the virtual environment with the instructions found [here](https://docs.python.org/3/tutorial/venv.html).
3. Install the requirements with `pip3 install -r requirements.txt`

## Usage
To run the code, use the command:
```
$ python3 app.py
```
With a browser, navigate to `http://127.0.0.1:5000`. The 'Home' screen should open as shown:

![/IMAGES/1image.png](/IMAGES/1image.png)

Select the type of device. For this iteration if the code only 4 options are available:
* Cisco IOS (can be old Cisco IOS routers or switches)
* Cisco XE
* Cisco XR
* NX-OS

Add the IP address or hostname. This has to be a reachable/routable IP address or hostname (via ping) from the machine where you are running this script. 
Add the SSH credentials: Username, Password and Secret.
Add the commands in the text box. One per line as if you were writing these commands directly in the router/switch. The code will send each command separately.
Click the "SEND" button

If everything is correct, you will be taken to a second page confirming your results. If there are any issues (credentials, config commands, etc.) you will get an alert explaining the situation. 

You can go back to the main page by clicking the "Back" hyperlink in the top-right corner of the screen.


# Screenshots

![/IMAGES/0image.png](/IMAGES/0image.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.