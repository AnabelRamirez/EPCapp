# Postcode Energy Efficiency App

This app uses the [Domestic Energy Performance Certificates API](https://epc.opendatacommunities.org/docs/api/domestic) of Ministry of Housing, Communities & Local Government to obtain energy performance certificate information about an address or postcode, as well as a current energy efficiency graph of the domestic properties in the postcode.

### Prerequisites

This app requires:
* Python 3.4 and above

## Getting Started

* First, obtain an API key by signing up in the Ministry of Housing, Communities & Local Government's page [here](https://epc.opendatacommunities.org/login#register).
* Clone or download this repository.
* Create an istances folder with a epcconfig.y file with the Basic Authentication information in the step above
* Now, you can further develop or test this API creating and activating a virtual environment in your computer. I have called it "Anabel_venv".
  ```
  python3 -m venv Anabel_venv
  source Anabel_venv/bin/activate
  ```
* Install the libraries specified in [requirements.txt](https://github.com/AnabelRamirez/EPCapp/blob/master/requirements.txt) by running 
  ```
  python -m pip install -U -r requirements.txt
  ```
* and run the app:
  ```
  python epc_app.py
  ```
  
You should be able to open the app in your browser using the prompted link.

See deployment for notes on how to deploy the project on a live system.

### App details

The app is formed by three get methods accessible by adding the following path to the API provided:

* /epcchart/postcode-withouth-spaces
* /epc/postcode/postcode
* /epc/address/address
  
For example:
  
```
curl -i http://localhost:5000/epcchart/AL12DE
curl -i http://localhost:5000/epc/postcode/AL12DE
curl -i http://localhost:5000/epc/address/2 alma road
```

## Deployment

To deploy on a live system:


```
Give an example
```

## Built With

* [Docker](https://github.com/docker) - Container to run the application
* [Kubernetes](https://github.com/kubernetes/kubernetes) - Load Balancer for the cluster
* [Cassandra](https://github.com/apache/cassandra) - Used to store the API requests information

## Author

* **Anabel Ramirez**


## License

Please read carfully the copyright information provided in (https://epc.opendatacommunities.org/docs/copyright)

