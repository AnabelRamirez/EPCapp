# Postcode Energy Efficiency App

This app uses the [Domestic Energy Performance Certificates API](https://epc.opendatacommunities.org/docs/api/domestic) of Ministry of Housing, Communities & Local Government to obtain energy performance certificate information about an address or postcode, as well as a current energy efficiency graph of the domestic properties in the postcode.

## Getting Started

First, obtain an API key by signing up in the Ministry of Housing, Communities & Local Government's page [here](https://epc.opendatacommunities.org/login#register).

You can further develop or test this API creating and activating a virtual environment in your computer. I have called it "Anabel_venv".
```
python3 -m venv Anabel_venv
source Anabel_venv/bin/activate
```
Install the libraries specified in [requirements.txt](https://github.com/AnabelRamirez/EPCapp/blob/master/requirements.txt) by running 
```
python -m pip install -U -r requirements.txt
```
and finally run the app:
```
python epc_app.py
```
You should be able to open the app in your browser using the prompted link.

See deployment for notes on how to deploy the project on a live system.

### Prerequisites

This API requires:
* Python 3.7


### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```
```
Give examples
```
End with an example of getting some data out of the system or using it for a little demo

## Deployment

Add additional notes about how to deploy this on a live system

```
Give an example
```

## Built With

* [Docker](https://github.com/docker) - Container to run the application
* [Kubernetes](https://github.com/kubernetes/kubernetes) - Load Balancer for the cluster
* [Cassandra](https://github.com/apache/cassandra) - Used to store the API requests information

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Anabel Ramirez**


## License

Please read carfully the copyright information provided in (https://epc.opendatacommunities.org/docs/copyright)

