# Mushroom
An easy and convenient way to monitor and regulate mushroom growth using IoT sensors and Raspberry Pi.

## Motivation
Mushrooms are very hardy fungi and can grow in many places. However, the extent of that growth is highly dependent on its environmental factors. This means trying to figure out the best conditions to grow mushrooms in your local context requires quite a bit of experimentation. The problem is monitoring and regulating the environment for mushroom growth requires a lot of time and is labor intensive. As such we are looking to create a system where gathering and logging on data becomes much easier for mushroom growers. 

## Getting Started

### Prerequisites
- Python 3 and above
- [scd30-i2c library](https://pypi.org/project/scd30-i2c/)

### Built With
#### Miicrocontroller
- Raspberry Pi 3 Mobel B+

#### IoT Sensors
- SCD40-D-R1
- TT DC Motor

#### Additional Hardware Parts
- L239D Motor Driver IC
- 5v Battery 

### Circuit Diagram
![Circuit Diagram](/images/circuit_diagram.png)

### How to Run the Project
Run `/src/main.py` on any IDE in RPI.


## Resources
[Controlling DC Motor with Raspberry Pi](https://www.electronicshub.org/controlling-a-dc-motor-with-raspberry-pi/)