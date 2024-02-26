# Solar Energy API

## Overview
A Flask API to calculate the amount of solar energy(kWh) produced by solar panels based on the formula E = A x r x H x PR

- E = Energy (kWh)
- A = total area of the panel(m²)
- r = yield/efficiency of the solar panel given by the ratio : electrical power (in kWp) of one solar panel (default value = 0.18)
- H = annual average solar radiation on tilted panels (kWh)
- PR = Performance ratio, constant for losses (range between 0.5 and 0.9, default value = 0.80)

Solar Energy API harnesses API chaining, notably using Global Solar Atlas responses for accurate, location-specific solar radiation data. It is deployed on the Azure Virtual Machine. Gunicorn is utilized as the web server interface, ensuring efficient handling of concurrent requests.

## Getting Started
- For direct API use, go to [Azure VM](#Azure-VM)
- For setting up locally, see below

### Requirements for local set up
Docker is required for deploying the API locally.

- **Installation:** Head to the [Install Docker Engine](https://www.docker.com/get-started) page.
- **Learning:** If Docker is unfamiliar, consider this [quick introduction](https://docs.docker.com/get-started/overview/).

### Setting up Locally
1. Clone the repository
 ```shell
 git clone https://github.com/jayjayjjpro/SolarEnergy_API.git
   ```
2.  Build the docker image
```shell
docker build -t <your-image-name> .
```
3. Run the docker container
```shell
docker run -d -p <your-port>:8000 <your-image-name>
```

## How to use the API
### Azure VM
1. url
```shell
http://4.193.193.171:5050/
```
3. Use the url on web broswer or Postman
4. Example
```shell
http://4.193.193.171:5050/?latitude=1.359433&longitude=103.852386&area=150&efficiency=&performance_ratio=0.7
```
### Local Docker
1. url
```shell
http://<your-ip-address>:<your-port>/
```
2. Use the url on web broswer or Postman
3. Example
```shell
http://<your-ip-address>:<your-port>/?latitude=1.359433&longitude=103.852386&area=150&efficiency=&performance_ratio=
```
## Help
If you encounter any issues, please contact Da Jie(	hiverlab.djchiam@gmail.com)

## Authors and Contributors
- Chiam Da Jie (AI/Backend developer Intern)
