# Copyright (c) 2022 Cisco and/or its affiliates.
#
# This software is licensed to you under the terms of the Cisco Sample
# Code License, Version 1.1 (the "License"). You may obtain a copy of the
# License at
#
#                https://developer.cisco.com/docs/licenses
#
# All use of the material herein must be in accordance with the terms of
# the License. All rights not expressly granted by the License are
# reserved. Unless required by applicable law or agreed to separately in
# writing, software distributed under the License is distributed on an "AS
# IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.


from flask import Flask, render_template, redirect, url_for, request, session
from netmiko import ConnectHandler


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def main_app():  # put application's code here
    if request.method == "POST":
        # Get information from WEBFORM
        device_type = request.form["device_type"]
        ip_address = request.form["ip_address"]
        username = request.form["username"]
        password = request.form["password"]
        secret = request.form["secret"]
        configuration_commands = request.form["configuration_commands"].splitlines()
        configuration_commands.append('do wr')
        configuration_commands.append('end')
        print(device_type)
        print(ip_address)
        print(username)
        print(password)
        print(secret)
        print(configuration_commands)

        # Netmiko STUFF
        connector = {
            "device_type": device_type,
            "ip": ip_address,
            "username": username,
            "password": password,
            "secret": secret
        }

        try:
            network_connect = ConnectHandler(**connector)
            network_connect.enable()
            print('Configuring Device')
            configure_device = network_connect.send_config_set(configuration_commands)
            print(configure_device)

            print('*** Device has been configured ***')
            print('*** End Status Configuration ***')
            network_connect.disconnect()
            return render_template('result.html',
                                   device_type=device_type,
                                   ip_address=ip_address,
                                   username=username,
                                   device_message = configure_device)
        except Exception as err:
            exception_type = type(err).__name__
            exception_message = str(err)
            return render_template('result.html',
                                   exception_type=exception_type,
                                   exception_message=exception_message)
    else:
        return render_template('main.html')


if __name__ == '__main__':
    app.run()
