## Study

We have evaluated how to use the values metrics analyzing others experiments and the public data below
1. https://github.com/raspberrypilearning/astro-pi-flight-data-analysis
2. https://github.com/jcb55/iss-astro-pi-data-browser
3. https://github.com/astro-pi/SpaceCRAFT
4. https://github.com/jpalau-edu/AstroPi2021
5. https://github.com/giamby3000/RedsTeam_AstroPi22

### 1. [raspberrypilearning/astro-pi-flight-data-analysis](https://github.com/raspberrypilearning/astro-pi-flight-data-analysis)

It contains more csv files where it is saved one record every 10 seconds:

1. `astro_pi_data_20150824_085954.zip`, from 2015-08-20 23:58:30 to 2015-08-24 08:57:40
2. `Columbus_Ed_astro_pi_datalog.csv.zip`, from 2016-02-16 10:44:40 to 2016-02-29 09:25:00
3. `Columbus2_Ed_astro_pi_datalog.csv.zip`, from 2016-03-14 09:53:00 to 2016-04-13 11:09:20
4. `Node2_Izzy_astro_pi_datalog.csv.zip`, from 2016-03-09 15:46:20 to 2016-03-25 09:10:50

All these data have the same format, so we also could all join together or compare them.

#### 1.1 [Our2015Analysis.ipynb](Our2015Analysis.ipynb)

There are just over 3 days of data where we can see fluctuations in values for each metric.
* 'temp_cpu', 'temp_h', 'temp_p', 'humidity' metrics have a strong correlation
* 'temp_cpu', 'temp_h', 'temp_p', 'humidity' metrics have a good correlation with 'pressure'

There are 3 interesting moments that we can describe.
* at some point the Astro Pi has been rotated on the axes y for ~360° and z for ~10° (see the first figure, axis named roll is axis y)
  * there are 2 different strong correlations between compass and magnetometer values, and compass and accelerometer values
  * the gyroscope values have only a peak for each axis, but it continues to have the same fluctuations
* soon after, the experiment has been resetted and the Astro Pi has been rotated again but on axes x and z for ~70° and y for some degrees
  * there are 2 different strong correlations between compass and magnetometer values, and compass and accelerometer values
  * the gyroscope values have only a peak for each axis, but it continues to have the same fluctuations
* at some point the magnetometer values of the the axis z increase slightly and immediately stabilize at the new height
    * it is the point where the humidity value is the lowest and it begins to rise
    * it is the point where the metrics of temperature values are the highest and they begin to decrease
    * there is something subtly perceptible about
      * axes y and z of the compass values
      * each axis of the acceleration values
      * at least the axis y of the gyroscope values

The last one moment could be an interesting range to be explored.

#### 1.2 [OurColumbusAnalysis.ipynb](OurColumbusAnalysis.ipynb)

#### 1.3 [OurColumbus2Analysis.ipynb](OurColumbus2Analysis.ipynb)

#### 1.4 [OurNode2Analysis.ipynb](OurNode2Analysis.ipynb)

### 2. [jcb55/iss-astro-pi-data-browser](https://github.com/jcb55/iss-astro-pi-data-browser), [OurColumbusAnalysis.ipynb](OurColumbusAnalysis.ipynb)

It contains the same file describe above `Columbus_Ed_astro_pi_datalog.csv.gz`.

### 3. [astro-pi/SpaceCRAFT](https://github.com/astro-pi/SpaceCRAFT), [OurSpaceCRAFTAnalysis.ipynb](OurSpaceCRAFTAnalysis.ipynb)

It contains a csv file, `SpaceCRAFT_20160209_104426.csv`, where it is saved one record every 10 seconds from 2016-02-09 10:44:26.564993 to 2016-02-16 10:44:16.592219.

The data provided by the study spans over 7 days and it shows that:
* There is a correlation between the 'temp_cpu', 'temp_h', 'temp_p' and 'humidity' metrics.

* Said metrics do not seem to be correlated with the 'pressure' metric, as its change towards
the 25000th measurement does not seem to affect 'temp_cpu', 'temp_h', 'temp_p' and 'humidity'.

* There is, obviously, a correlation between the 'orientation radians' and 'orientation degrees'
metrics, since radians and degrees are different units of measurement for angles.

More specific observations can be made concerning the 'orientation', 'compass', 'gyroscope' 
and 'accelerometer' metrics, though.

* It can be observed clearly how the orientation of the device fluctuated constantly throughout
the analyzed time period.

  * At first (between times 0 and 4000), the device's yaw fluctuated between 1 and 3 radians 
  (0 and ~10000) degrees

  * From that point onwards, the yaw orientation fluctuated periodically between -3 and 0 radians 
  following a sine wave pattern. This pattern is interesting, though, because the peak of this sine
  wave was not constant, but flluctuated periodically between -1 and -0 radians 
  (~16000 and ~20000 deg)

  * Similarly, the device's roll orientation fluctuated between 0.9 and 1.1 radians (3300-3600 deg) 
  throughout the entire length of the experiment. Furthermore, the device's pitch orientation 
  fluctuated between -0.1 and 0.1 radians.

  * It can be derived that the device was oscillating constantly and periodically,
  throughout the entire experiment.

* The readings for the 'compass' metrics show how the magnetic field detected by the device changed.
They show that for all the three axes, the compass values oscillated periodically.

  * The 3d plot of the 'compass' metrics, show that, over time, that the magnetic field,
   detected by the compass sensor, followed a pseudo-circular motion, while also going 
   downwards.

  * The accelerometer values further confirm said motion, as the values for 'accelerometer raw y'
  and 'accelerometer raw z' were constantly fluctuating around the 0.02 and 0.01 mark, 
  respectively. This means that the device's position was changing continuously on the y and z axes.

* The gyroscope values were almost always fluctuating around -0.005 and 0.005, except for 
specific peaks at random intervals. Therefore, most of the time, the gyroscope never measured any
relevant change in value.


### 4. [jpalau-edu/AstroPi2021](https://github.com/jpalau-edu/AstroPi2021), [OurJunoAnalysis.ipynb](OurJunoAnalysis.ipynb)

It contains a csv file, `juno_data.csv`, where it is saved one record every 11-12 seconds from 2021-04-19 17:48:11 to 2021-04-19 20:46:04.

### 5. [giamby3000/RedsTeam_AstroPi22](https://github.com/giamby3000/RedsTeam_AstroPi22), [OurAstropiAnalisys.ipynb](OurAstropiAnalisys.ipynb)

It contains a csv file, `HeaderLog.csv`, where it is saved 3-6 records per second from 2022-04-18 19:57:14:422517 to 2022-04-18 22:54:12:650693.
