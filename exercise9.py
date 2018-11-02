#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 10:41:03 2018

@author: charrington
"""

import numpy
import pandas
from plotnine import *

#script to import age.txt and create a scatterplot with trendline
age=pandas.read_csv("female_age_height.txt",header=0,sep=("\t"))

a=ggplot(age,aes(x="age",y="height"))+xlab("age")+ylab("height")
a+geom_point()+stat_smooth(method="lm")

#script to import data.txt and create a bar graph and scatter plot
data=pandas.read_csv("data.txt",header=0,sep=",")

d=ggplot(data,aes(x="factor(region)",y="observations"))+xlab("region")+ylab("mean observations")
d+geom_bar(stat="summary",fun_y=numpy.mean)

e=ggplot(data,aes(x="factor(region)",y="observations"))+xlab("region")+ylab("observations")
e+geom_jitter()

#the bar graph makes it seem like the observations across all the areas are essential equal, however the scatterplot shows you that there is a wide range of observations in the north and west regions and concentrations of numbers of observations within the north and south regions. These distributions in observations are not apparent in the averages on the bar graph.