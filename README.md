# restconf_flask_app
Restconf-Flask is a simple web application that utilizes the Restconf API to retrieve information from the Cisco IOS XE datastore. This app allows you to explore and manage your devices using the provided features.

Restconf-Flask is a simple web application that utilizes the Restconf API to retrieve information from the Cisco IOS XE datastore. This app allows you to explore and manage your devices using the provided features.

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
    from restconf_flask import db
    db.create_all()
    exit()
5. Run the Flask application:
    ```bash
    flask run
Open your web browser and go to http://127.0.0.1:5000 to access the Restconf-Flask app.
![Alt Text](https://ibb.co/cbXZBXZ)
   
   
