import numpy as np
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
import time
import pandas as pd
import cx_Oracle
import datetime as dt
from datetime import timedelta,datetime
from IPython import display
import math

fig, ax = plt.subplots()

max_x = 5
max_rand = 10

x = [0,1,2,3,4] #x축설정
print(x)
ax.set_ylim(0, max_rand) #y축의 최솟값, 최댓값을 0와 10로 설정
line, = ax.plot(x, np.random.randint(0, max_rand, max_x))#0부터 10까지 5개 고르기?
the_plot = st.pyplot(plt)#흠..이게뭘까

def init():  # give a clean slate to star ((((
    line.set_ydata([np.nan] * len(x))

def animate(i):  # update the y values (every 1000ms)
    line.set_ydata(np.random.randint(0, max_rand, max_x))#y축 데이터 업데이트
    the_plot.pyplot(plt)#보여주기2222222222222222222222222222222

init()
for i in range(100):
    animate(i)
    time.sleep(1)