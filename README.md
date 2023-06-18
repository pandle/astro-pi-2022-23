# Astro Pi 2022/23

This repository contains the study and report of experiments with the [Astro Pi](https://github.com/raspberrypilearning/astro-pi-guide)
for the [European Astro Pi Challenge 2022/23](https://astro-pi.org/), [Mission Space Lab](https://astro-pi.org/mission-space-lab/) (see [details](https://www.raspberrypi.org/blog/768-teams-entered-astro-pi-mission-space-lab-2022-23/) to know some numbers).
It is part of the [educational repositories](https://github.com/pandle/materials) to learn how to manage a project.

## Study

Before to subcribe the team, we have evaluated some experiments and the public data [described here](study/README.md).

What we have learned:

* [how to](TOOLS.md) use the tools for this project
* [how to](study/README.md) read the graphics of the Astro PI metrics
* what the machine learning [steps](https://github.com/mrdbourke/zero-to-mastery-ml/blob/master/section-1-getting-ready-for-machine-learning/a-6-step-framework-for-approaching-machine-learning-projects.md) are

## Project details

## Experiment on the Earth

What we have learned:

* how to get the Astro PI metrics
* how to recognize the move on the Astro PI metrics graphics
* a simple machine learning algorithm to recognize humans

## Training model to recognize the objects in the ISS

What we have learned:

* creation of the [catalogue](CATALOGUE.md) of the objects (and people) on the ISS is very challenging
* there are models pre-trained are ready to use

## Experiment on the Space

What we have learned:

* PIR sensor detect a person up to approximately 30/15 ft away ([details](https://www.parallax.com/package/pir-sensor-rev-b-product-guide/))
  * we have used only [MotionSensor class](https://gpiozero.readthedocs.io/en/stable/api_input.html?highlight=MotionSensor#gpiozero.MotionSensor)
  * it would have been interesting to have an ultrasonic distance sensor for using [DistanceSensor class](https://gpiozero.readthedocs.io/en/stable/api_input.html?highlight=MotionSensor#gpiozero.DistanceSensor)
* [HOGDescriptor class](https://docs.opencv.org/4.x/d5/d33/structcv_1_1HOGDescriptor.html) of [opencv-python](https://pypi.org/project/opencv-python/) is less sensitive than the PIR sensor
  * humans were not entirely visible in the image
  * humans were too close, occupying the whole image with an arm or body
