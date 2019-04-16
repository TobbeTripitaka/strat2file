#!/usr/bin/env python3

# Tobias Staal 2019
# tobias.staal@utas.edu.au
# version = '0.0.1'
#

#GNU GENERAL PUBLIC LICENSE#

#Copyright (c) 2019 Tobias Stål#


import numpy as np
import pandas as pd

def geo_to_year(age, 
        chart, 
        gauge = 0.5,
        early=0.75, 
        mid=0.5, 
        late=0.25, 
        latest = 0, 
        earliest = 1,
        late_labels = None,
        early_labels = None,
        mid_labels = None, 
        use_descriptive = True,
        m = True, 
        age_col = 7, 
        uncertainty = False, 
        uncertainty_col = 9, 
        format_chart = False):
    '''Function to convert name of startigraphic age to years in million years
    age -- string with geological age
    chart -- The International Chronostratigraphic Chart as pandas data array
    gauge -- a scalafr to set time from 0 (min for period) to 1 (max for period)
    mid, late, latest, early, earliest = predefined gauges
    use_descriptive -- True if prefixes defined in labels should change returned time
    m -- rerturne Ma, else years
    age_col -- colomn on chart that contains age in Ma
    uncertainty -- if uncertainty of period definitions should be included
        False if not, 'min' for min age and 'max' for max age
    '''
    
    in_phrase = age.strip().lower().split()
    chart = np.array(chart)
    find = np.zeros((chart.shape[0], len(in_phrase))).astype('bool')
    
    if format_chart: 
    	chart = chart.applymap(lambda s:s.strip().lower() if type(s) == str else s)

    if late_labels==None:
        late_labels = ['upper', 'later', 'late']
    
    if early_labels==None:
        early_labels = ['lower', 'early', 'earlier']
        
    if mid_labels==None:
        mid_labels = ['mid', 'middle']
        
    for i, in_p in enumerate(in_phrase):
        find[:,i] = np.any(chart == in_p, axis=1)
        
    here = np.sum(find, axis=1)
    max_here = np.max(here)
    ii = np.where(here==max_here)[0]
    
    if max_here == 1 and len(in_phrase) == 2 and use_descriptive:
        print('Not defined expression.')
        if in_phrase[0] in late_labels:
            gauge = late
        elif in_phrase[0] in ['latest']:
            gauge = latest
        elif in_phrase[0] in early_labels:
            gauge = early
        elif in_phrase[0] in ['earliest']:
            gauge = earliest
        elif in_phrase[0] in mid_labels:
            gauge = mid
        else:
            print('Unknown prefix.')
    
    if uncertainty==False:
        e_top = e_bottom = 0
    elif uncertainty=='max':
        e_top = np.nan_to_num(- chart[ii-1, uncertainty_col][0])
        e_bottom = np.nan_to_num(chart[ii, uncertainty_col][-1])
    elif uncertainty=='min':
        e_top = np.nan_to_num(chart[ii-1, uncertainty_col][0])
        e_bottom = np.nan_to_num(- chart[ii, uncertainty_col][-1])
        
          
    min_my = chart[ii-1, age_col][0]-e_top # ii-1 because start of next time is end of this
    max_my = chart[ii, age_col][-1]+e_bottom
    my = min_my + gauge*(max_my-min_my)
    
    # Option to return years instead of Ma
    if not m:
        min_my *= 1e6
        max_my *= 1e6
        
    return min_my, max_my


def year_to_geo(
	years, 
	chart, 
	m=False):
	'''
	Convert year to stratigraphic age. 
	'''
	if m:
		years /= 1e6

	A = chart.ix[(chart['Ma']-years).abs().argsort()[:2]]

	print(A)





	return 


