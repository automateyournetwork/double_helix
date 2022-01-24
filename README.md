# double_helix
Mind Maps of Cisco Digital Network Architecture Centre (DNA-C) REST APIs 

![Device](/images/sampledevice.png)

## Ready to Run with DevNet Always On Sandbox

This repository is ready to go with the Cisco DevNet Always On Sandbox for DNA-C !

In your project directory, create your virtual environment

``` console
python3 -m venv env
```

Activate (use) your new virtual environment (Linux):

``` console
source env/bin/activate
```

Download or clone the brainfreeze repository:

``` console
git clone https://github.com/automateyournetwork/double_helix.git
```

``` console
cd double_helix
cd MindMaps
python3 double_helix.py
```

## Customization

To run this against your own DNA-C Update the following:

Update your target DNA-C FQDN / IP Address on lines 20

```python

dnac = "https://sandboxdnac.cisco.com"

```

You will need to generate a new Base64 encoded string to replace the Basic Authorization key on line 17

Using a Base64 encoder take your API authorized username and password and encode them

username:password

You will get a string like the Basic auth string on line 17 

ZGV2bmV0dXNlcjpDaXNjbzEyMyE=

```python

auth_headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

```

## View the Mindmaps 

Install the markmap VS Code Extension

![Mark Map](/images/markmap.png)

Open the markdown file and click the "Open as markmap" 