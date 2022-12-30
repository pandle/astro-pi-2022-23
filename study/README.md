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

### 4. [jpalau-edu/AstroPi2021](https://github.com/jpalau-edu/AstroPi2021), [OurJunoAnalysis.ipynb](OurJunoAnalysis.ipynb)

It contains a csv file, `juno_data.csv`, where it is saved one record every 11-12 seconds from 2021-04-19 17:48:11 to 2021-04-19 20:46:04.
Initially there are three metrics: 
* CPU_temp, 
* Sense_temp, 
* Sense_Hum
these are quite stable and have a good correlation, because initially as a single metric varies, it is noted that the other 2 also vary.
Looking at the orientation metrics in a graph, you notice that the graph is "noisy" or that the orientation is constantly changing. At a certain point, the orientation stabilizes for the metrics of the X and Y axes, while it stabilizes in 2 short periods for the metrics of the Z axis, and then resumes its continuous variation.
Same thing goes for the magnetometer, the metrics keep changing over time. The magnetometer metrics in the X and Y axes follow a similar pattern.
The gyroscope and accelerometer graphs do not show large variations (except for 2 peaks).

### 5. [giamby3000/RedsTeam_AstroPi22](https://github.com/giamby3000/RedsTeam_AstroPi22), [OurAstropiAnalisys.ipynb](OurAstropiAnalisys.ipynb)

It contains a csv file, `HeaderLog.csv`, where it is saved 3-6 records per second from 2022-04-18 19:57:14:422517 to 2022-04-18 22:54:12:650693.
