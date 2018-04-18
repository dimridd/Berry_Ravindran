#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 11:32:12 2018

@author: divyanshu
"""

#%%

import time

table = [[0 for i in range(256)] for j in range(256)]

def bc1(pat, m, table):
	
	table = [[m+2 for i in range(256)] for j in range(256)]
	
	for i in range(256):
		table[i][ord(pat[0])-65] = m + 1
		
	for i in range(m-1):
		table[ord(pat[i])-65][ord(pat[i+1])-65] = m-i
		
	for i in range(256):
		table[ord(pat[m-1])-65][i] = 1
	
	return table

text = "GCATCGCAGAGAGTATACAGTACG"
pat = "GCAGAGAG"
sigma = "ACGT"

bc = bc1(pat.upper(), len(pat), table)		

def cmp(pat, text, j, m):
	count = 0
	for i in range(m):
		if pat[i] == text[i+j]:
			count += 1
	
	if count == m:
		return 1
	else:
		return 0

	
def BR(pat, m, text, n):
	j = 0
	matches = 0
	
	bc = bc1(pat.upper(), len(pat), table)		
	
	text = text + "["
	text = text + "["
	
	while j<=n-m:
		
		if cmp(pat, text, j, m):
			matches += 1
			
			
		j += bc[ord(text[j+m])-65][ord(text[j+m+1])-65]
		
	return matches


def main():
	with open('hi', 'r') as myfile:
		   data=myfile.read().replace('\n', '')
	
	
	text = data
	pat = "MAIKIGINGFGRIGRIVFRA"
	
	t1 = time.time()
	print ('start')
	print(BR(pat, len(pat), text, len(text)))
	t2 = time.time()
	print ( (t2 - t1) * 1000)
	
if __name__ == '__main__':
	main()
		
		
