CONTENTS OF THIS FILE
---------------------
   
 * Introduction
 * Requirements
 * How to use
 * Creators

INTRODUCTION
------------

The application was created for the project Python in the Enterprise. The application is designed to detect the matrix of the camera image, its decoding and display information about it encoded in the form of a slide.
Created a database of objects and slides and a graphical interface, which is able to add them to the database.

REQUIREMENTS
------------

This module requires the following modules:

 * Python 3.4
 * OpenCv 3.0 (http://opencv.org/)
 * TKinter (apt-get install python3-tk)
 * other (pip install -r requirements.txt)


HOW TO USE
----------

You should run the file interactive_display.py. After opening the interface is visible window containing objects and slides. Each object has an id number, which are assigned to individual slides. You can add both objects and slides giving them id numbers and file names (formerly the files should be placed in the "slides" directory). Press the "Run Detector" to start the camera. It should be applied in parallel to the DataMatrix not covering its field of application to detect it in the image. Once properly applied and decoded by the application, the image should appear loaded earlier slides. After the discontinuation of operations and its re-repetition, the order of the slides is saved and continued.

CREATORS
--------

 * Agnieszka Waryś
 * Konrad Mrozowski
 * Ryszard Mikulec

