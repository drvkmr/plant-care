<a href="http://balena.io"><img src="https://raw.githubusercontent.com/drvkmr/plant-care/master/img/balena_logo.jpg" width=300 title="balena" ></a>

***balena.io***

# plantCare

An IoT system to automate plant maintenance built on Raspberry Pi with Balena.

## Table of Contents

- [Introduction](#introduction)
- [Hardware required](#hardware%20required)
- [Physical setup](#physical%20setup)
- [Video demo](#video)
- [Wiring Diagram](#wiring%20diagram)
- [Understanding plant](#understanding%20plant)
- [Code snippets](#code%20snippets)
- [FAQs](#faqs)
- [Support](#support)
- [Licence](#licence)

## Introduction

We all love plants. But in this busy lifestyle, sometimes it's tricky to maintain and take care of them in daily basis, specially if you have a lot of them.

This project attempts to automate the process simply and sensibly. It uses balena to stay online so you can keep an eye on your beloved plants even when you are on a holiday.

## Hardware Required

- 1 x Raspberry Pi 3 b+
- 1 x LDR sensor
- 1 x 5v pump
- 3 x <a href="https://www.amazon.co.uk/QLOUNI-Moisture-Hygrometer-Detection-Automatic/dp/B077FGS3C1/ref=sr_1_9?keywords=moisture+sensor&qid=1576455999&sr=8-9" target="_blank">**Moisture sensors**</a>
- <a href="https://www.amazon.co.uk/Function-Anywhere-Charging-Horticultural-Growing/dp/B07GB28WCH/ref=sr_1_1_sspa?keywords=grow+lights&qid=1576455923&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExWTJNN1hYTEVDRTNWJmVuY3J5cHRlZElkPUEwMjMxMDY0MlMzSEhQUUM4Vko1MCZlbmNyeXB0ZWRBZElkPUEwMzcyODY5Sk4zVEFTWkNQTEJHJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==" target="_blank">**Grow Lights**</a> as needed
- 2 x <a href="http://www.irf.com/product-info/datasheets/data/irlz44n.pdf" target="_blank">**IRLZ44N Mosfets**</a>
- 1 x 5v (minimum 2A) power supply
- 1 x RPi power supply
- Water atomiser (not implemented yet)

## Physical Setup

[![Setup1](https://raw.githubusercontent.com/drvkmr/plant-care/master/img/setup.jpg)]()
[![Setup2](https://raw.githubusercontent.com/drvkmr/plant-care/master/img/setup2.jpg)]()
[![Moisture](https://raw.githubusercontent.com/drvkmr/plant-care/master/img/moisture.jpg)]()
[![LDR](https://raw.githubusercontent.com/drvkmr/plant-care/master/img/ldr.jpg)]()
[![circuit](https://raw.githubusercontent.com/drvkmr/plant-care/master/img/messy_circuit.jpg)]()


## Video

//Youtube link

## Wiring Diagram

//Add fritzing diagram

## Understanding plant

[![rubber](https://raw.githubusercontent.com/drvkmr/plant-care/master/img/rubber_plant.jpg)]()

<a href="https://www.patchplants.com/gb/en/plants/rubber-plant-176/" target="_blank">**Patch Plants**</a>

All plants have different needs and requirements and it's crucial to understand them before diving into the code.

For this project I am using a Rubber plant which needs to be watered once per week. This is crucial as roots of some plants get infested if they are watered too much. The soil needs to get a little dry before it's watered again.

It also likes moisture on its leaves. This can be achieved using a mist maker or an atomiser of some kind. This is not yet implemented into the system.

Finally, sunlight is essential for every plant. Where I am right now, most days come without it. But we can easily substitute it with full spectrum LED lights.

## Code Snippets

Plants don't need 24x7 care. They need someone to check in periodically and adjust little things. But interfacing with a real time clock and setting up activities over it can get quite frustrating.

<a href="https://schedule.readthedocs.io/en/stable/" target="_blank">**Schedule**</a> comes to rescue. It handles all the backend and enables us to trigger functions at the right time consistently. For instance, we don't want the soil to be drenched in water all the time, so it's a good idea to only trigger watering once every week.

```python
schedule.every().monday.at("11:00").do(water)
```

One of the limitations of Raspberry Pi is the absence of an ADC converter. Which means there's no straightforward way to read values from light and humidity sensors. But with a little bit of creativity, engineering and googling, nothing is unachievable.

Check out this <a href="https://www.instructables.com/id/Raspberry-Pi-GPIO-Circuits-Using-an-LDR-Analogue-S/" target="_blank">**instructable**</a> overcoming the problem using a single dirt cheap capacitor!!! If that's not clever, I don't know what is.

Moisture sensor is easier to handle. It has two outputs, analog and digital. Mysterious... It also comes with a tiny knob. Plot thickens...

Well the knob lets you set a limit to how 'moist' it should be when the digital pin goes high. Bravo whoever designed this sensor !!!

<img src="https://raw.githubusercontent.com/drvkmr/plant-care/master/img/moisture_knob.jpg" width=600 title="Humidity Sensor" >


## FAQs

- If you don't know balena, <a href="https://www.balena.io/docs/learn/getting-started/raspberrypi3/python/" target="_blank">**start here**</a>.

## Support

## Licence