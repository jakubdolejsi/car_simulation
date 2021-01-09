# Car simulation model

Simulation model of electric cars and charging stations in Brno in Czech Republic.


## Configuration
Model configuration is enabled via config.ini file located in config folder.


### Syntax
```
cars=integer
chargers=integer
sim_len=integer
```

### Legend

- **cars**: integer value of number of cars that will be available 
- **chargers**: integer value of number of chargers that will be available 
- **sim_len**: Simulation time in weeks 



### Example values
```
cars=10_000
chargers=500
sim_len=5
```


## Requirements
- **Docker** 

Application could be alternatively run in non container environment. In this case you will
need to install followings:
- **Python 3.x**
- **SimPy 4.x**
- **matplotlib**



## Run

Application could be easily run via docker-compose service.

```
docker-compose up
```
In non docker environment, application could be run directly via python.

```
python3 app.py
```
