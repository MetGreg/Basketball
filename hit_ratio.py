#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:09:00 2017

@author: gregor

Script to visualize the history of my basketball hit ratio.

"""
# Import modules
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd


# =============================================================================
# # Configuration
# =============================================================================
data_file = 'hit_ratio_data.csv'
plt.style.use('seaborn')


# =============================================================================
# # Handle data
# =============================================================================
data = pd.read_csv(data_file)
time = pd.to_datetime(data['date'], format='%d.%m.%Y')
three_pt_shots = (data['3er_hits']/data['3er_attempts']*100).fillna(
        method='ffill'
        )
two_pt_shots = (data['2er_hits']/data['2er_attempts']*100).fillna(
        method='ffill'
        )
one_pt_shots = (data['1er_hits']/data['1er_attempts']*100).fillna(
        method='ffill'
        )
free_throws_game = (data['1er_hits_g']/data['1er_attempts_g']*100).fillna(
        method='ffill'
        )


# =============================================================================
# # Plot data
# =============================================================================
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.plot(time, one_pt_shots, label='1er')
plt.plot(time, two_pt_shots, label='2er')
plt.plot(time, three_pt_shots, label='3er')
plt.plot(time, free_throws_game, label='1er game')
plt.ylim(0, 100)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Hit ratio [%]', fontsize=16)
plt.title('My hit ratio', fontsize=20)
plt.legend()
plt.tight_layout()
plt.show()
