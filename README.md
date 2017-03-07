# theseus
Theseus aims to be an open source library of maze creation and solving tools. The Theseus platform is implemented in Python and C#. The Daedalus platform creates randomized 2D mazes which can be used for a diverse set of tasks most notably as the underlying data structure for Game Design. The Ariadne platform aims to become a competent maze solving AI which does not require problem set Omniscience. Using machine learning we are teaching Ariadne how to solve mazes without prior knowledge of the course.

Future features:
More diverse maze generation algorithms
The ability to produce 3D mazes
built in A\* implmentation
Neaural Network fitness evaluator
Neaural Network generation producer
Neural Network trial executor

The Basic organization of this project is a simple heirarchy of modules and packages. 
The naming convention for packages stem from the Greek Myth of the Labyrinth.
Seeing as this project is intended to solve mazes I thought the story was apt source
material. 

Daedalus -> package consiting of classes, utilities and scripts meant to model and display mazes of various kinds
Ariadne -> package consisting of classes, utilities and scripts mean to setup a neural network which will solve the mazes.
