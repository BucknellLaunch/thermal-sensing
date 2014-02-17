# Thermal Sensing

How many times have you walked into a classroom and it was uncomfortably warm or cold? Did you then open a window to compensate? Large commercial buildings are difficult to keep comfortable because the heating demand is strongly influenced by the occupants. For example, a classroom filled with 100 students requires a lot more ventilation than when it is empty. Unfortunately automatically sensing occupancy is a difficult task. However, almost everyone carries around a smartphone and can quickly and easily sense these environmental problems.

The idea behind participatory sensing is rather than design and build fancy (and expensive) occupancy sensors, we instead rely and the building’s occupants to participate in the sensing process. After all, the occupants are the ones that the building is trying to keep comfortable anyway.

For more information, visit this [link](http://www.eg.bucknell.edu/~cs475/wordpress/?page_id=114).

## Installation

To install and run this application, make sure you have [Node.js](http://nodejs.org/), [npm](https://www.npmjs.org/), and [mongodb](http://www.mongodb.org/) installed. Spin up your mongo server and then clone this repository:

```
$ git clone https://github.com/jcomo/thermal-sensing.git
$ cd thermal-sensing
$ npm install
$ PORT=8080 node web.js
```

## About

This is a project for a senior level undergraduate computer science design project. The code is licensed under the MIT license but should be used for educational and learning purposes only.