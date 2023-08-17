# restconf_flask_app
Restconf-Flask is a simple web application that utilizes the Restconf API to retrieve information from the Cisco IOS XE datastore. This app allows you to explore and manage your devices using the provided features.
live site here: http://restconfflask.pythonanywhere.com

## Features

### Add Devices Tab

The "Add Device" tab enables you to create, update, and delete devices. You can also perform the following actions from the "With Selected" tab:

- **Get Interface Information:** Query device interface information.
- **Get Device Configuration:** Obtain the device configuration and save it in JSON format in the `config-files` directory.
- **Display Device Configuration:** Display the device configuration that was saved during the "Get Device Configuration" phase.
- - **More:**

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/yassinech-99/restconf_flask_app.git
2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt

3. Set the Flask app environment variable

   ```bash
    export FLASK_APP=restconf_flask
4. Initialize the database:

    ```bash
    export FLASK_APP=restconf_flask
    flask shell
    from restconf_flask import db
    db.create_all()
    exit()
5. Run the Flask application:
    ```bash
    flask run
Open your web browser and go to http://127.0.0.1:5000 to access the Restconf-Flask app.

![Alt Text](https://i.ibb.co/Fsqyrqy/1.jpg)

6. Navigate to Add Devices Tab and Create a Device From Cisco Developer Sandbox:
   am using Cisco IOS XE Always on:
   ```bash
   Host = sandbox-iosxe-latest-1.cisco.com
   Port = 443
   Username = admin
   password = C1sco12345

![Alt Text](https://i.ibb.co/k6T9qN0/2.jpg)

![Alt Text](https://i.ibb.co/G0vC0QY/3.jpg)


7. Now that you have created a device you can:

![Alt Text](https://i.ibb.co/nL2shHj/5.jpg)

Get Device Interfaces Inforamtion

![Alt Text](https://i.ibb.co/nkSX1vW/6.jpg)

Save Device Configuration

![Alt Text](https://i.ibb.co/f48CC00/7.jpg)

Display Device Save Configuration

![Alt Text](https://i.ibb.co/XXG4X1t/8.jpg)




   
  

   
   
