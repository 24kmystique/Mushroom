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
- [SCD40-D-R1](https://sg.element14.com/sensirion/scd40-d-r1/gas-detection-sensor-co2-40000ppm/dp/3677905)
- [TT DC Motor](https://www.adafruit.com/product/3777)

#### Additional Hardware Parts
- [L239D Motor Driver IC](https://shopee.sg/L293D-L293-L293B-DIP-SOP-Push-Pull-Four-Channel-Stepper-Motor-Driver-IC-i.161496038.6002004709)
- 5V Battery 

### Circuit Diagram
![Circuit Diagram](/images/circuit_diagram.png)

### How to Run the Project
Run `/src/main.py` on any IDE in RPI.
The client side code has a default topic tied to a public realm : 42
Visit [BigBrain Realm 42](https://bigbrain.link/realms/42/42) to access the dashboard.
Only snippets of server side code can be found as its deeply integrated with our codebase


## Resources
[Controlling DC Motor with Raspberry Pi](https://www.electronicshub.org/controlling-a-dc-motor-with-raspberry-pi/)
