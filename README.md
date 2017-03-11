# Infinite 2017

## About

This project uses the EV3 brick, motors and color sensors to move along the lines of Singapore's MRT railway system.

This project features 3 railway lines known as the East West Line (EWL), North South Line (NSL) and Circle Line (CCL). They are also known as green line, red line and yellow line respectively.

The stations featured in this project are:

| Station No.   | EWL           | NSL           | CCL               |
|:-------------:|---------------|---------------|-------------------|
| 1             | Jurong East   | Jurong East   | Habourfront       |
| 2             | Clementi      | Chua Chu Kang | Haw Par Villa     |
| 3             | Buona Vista   | Woodlands     | Buona Vista       |
| 4             | Outram Park   | Yishun        | Holland Village   |
| 5             | City Hall     | Bishan        | Botanic Gardens   |
| 6             | Bugis         | Toa Payoh     | Bishan            |
| 7             | Kallang       | Newton        | Serangoon         |
| 8             | Paya Lebar    | Orchard       | Paya Lebar        |
| 9             | Bedok         | Somerset      | Stadium           |
| 10            | Tanah Merah   | Dhoby Ghaut   | Esplanade         |
| 11            | Changi        | City Hall     | Dhoby Ghaut       |
| 12            | -             | Marina Bay    | -                 |

Users will select the starting station of a line and the destination station of any line on the railway system. The logic is powered by Python running on the EV3 using ev3dev OS.

The user interface for selecting the start point and end point is a website hosted locally on the EV3 brick that can be assessed by a computer connected to it via Wi-Fi. The web server hosted on the EV3 brick is powered by the [Flask microframework](http://flask.pocoo.org/) for Python.

## Installing

Load [ev3dev](http://www.ev3dev.org/) OS on the EV3. Details on how to do so can be found [here](http://www.ev3dev.org/docs/getting-started/).

Access the EV3 through [SSH](http://www.ev3dev.org/docs/tutorials/connecting-to-ev3dev-with-ssh/). Also, make sure that the EV3 has access to the Internet. Details on how to connect the EV3 to the Internet can be found [here](http://www.ev3dev.org/docs/networking/).

Install ```git``` on the EV3:
```bash
sudo apt-get install git
```

Clone this repository:
```bash
git clone https://github.com/zzereen/infinite-2017.git
```

## Run the project

On the EV3 brick:

```bash
python3 main.py
```
