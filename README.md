# qr-codifier

### Simple tool to generate VCARD QR Codes w/images

- **Note**: This uses a deprecated Google Charts API. It still works for now (7/2022). 
- This is to help [Tom Man](https://stackoverflow.com/users/14551400/tom-man) with [this question on StackOverflow](https://stackoverflow.com/questions/71199422/does-native-iphone-camera-allow-vcard-encoded-as-qr-code-to-have-photos/72778218?noredirect=1#comment128579772_72778218)

### How to use 

- Clone this repo using `git clone https://github.com/SeaDude/qr-codifier.git`
- **Optional:** 
  - Install a virtual environment using `python -m venv .venv`
  - Activate the venv: `.\.venv\Scripts\activate`
- Install Python modules:
  - `pip install -r requirements.txt`
- Customize the VCARD:
  - Open `qrcodifier.py`
  - Fill in the variables as needed
  - Save
- Create a small .png to use as VCARD image 
  - **NOTE:**
    - The image must be very small as QR Codes can only hold ~3500 characters and the Base64 encoded image must be well below this value to allow for the other parameters (name, org, phone, etc.).
  - Save the image as `logo.png` in this directory
- Run `qrcodifier.py` to execute the program
- This will create `qrcode.png`
- Scan it and you should see the image on the VCARD
