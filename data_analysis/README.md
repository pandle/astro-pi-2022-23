# Data analysis

## [`elaborate_motion.py`](./elaborate_motion.py)

This file elaborates the motion data inside [`data_received/`](../data_received), by doing two things:

1. Each measurement is associated to a timestamp (in either microseconds or seconds)
relative to the start of the experiment
2. All the "holes" that are present inside the measurement data are filled by adding
estimated measurements that can be of any value (-1 or 0 for example).
    * The estimated measurements are evenly spaced inside the holes
    * The number of estimated measurements inside each "hole" is determined by 
    dividing the duration of the hole by the average delta of each measurement 

## [`motion_data/`](./motion_data)
This folder contains the files calculated by [`elaborate_motion.py`](./elaborate_motion.py).

## [`estimated_motion_microsecs_0`](./motion_data/estimated_motion_microsecs_0.csv)
**This file is useful for the data analysis**

* Inside this file there are all the motion sensor measurements and all the estimated
ones.
* The timestamp is represented in microseconds elapsed since the start of the experiment.
* All the estimated measurement have value "0". 

## [`estimated_motion_microsecs_-1`](./motion_data/estimated_motion_microsecs_-1.csv)
**This is useful only to see where there are "holes" in the data**

* Inside this file there are all the motion sensor measurements and all the estimated
ones.
* The timestamp is represented in microseconds elapsed since the start of the experiment.
* All the estimated measurement have value "-1". *(**not** useful for the data analysis)* 

## [`GeneralAnalysis.ipynb`](./GeneralAnalysis.ipynb)
**This is useful to have a macro overview of data received**

* The metrics of the magnetometer show a different behavior than that described in [Vidhya’s code](https://www.esa.int/Education/AstroPI/And_the_finalists_of_the_2019-20_Astro_Pi_Challenge_Mission_Space_Lab_are)
* The Pearson's correlation is very low between metrics and the feature named motion_detection
* The resolution is different among sensors and microgravity needs at least ${10^{-8}}$ and maybe it is possible to detect it
