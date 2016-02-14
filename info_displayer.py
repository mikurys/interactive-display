#! /usr/bin/env python
import database_creator
import data_matrix_detector
import os
from peewee import *
from database_creator import TextToDisplay
import cv2
import time

class InfoDisplayer:
    def __init__(self):
        self;
    
    @staticmethod
    def display(id, dataMatrixDetec):
        id = int(id);
        database = SqliteDatabase('test.db')
        database.connect();
        query = (TextToDisplay.select().where(TextToDisplay.id == id))
        font = cv2.FONT_HERSHEY_SIMPLEX

        for texts in query:
            cv2.putText(dataMatrixDetec.frame,texts.text1,(10,500), font, 2,(255,255,255),2,cv2.LINE_AA)
            #cv2.putText(dataMatrixDetec.frame,texts.text2,(10,500), font, 2,(255,255,255),2,cv2.LINE_AA)
            #cv2.putText(dataMatrixDetec.frame,texts.text3,(10,500), font, 2,(255,255,255),2,cv2.LINE_AA)