# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 03:44:20 2021

nama:sarah sakinah
nim:065002100033
prodi:sistem informasi
"""

print('tuple 1: ')
s=('1031','1032', '1033', '1034', '1035', '1036', '1037', '1038', '1039', '1040', '1050')
a = ", ".join(s[0:3])
r = ", ".join(s[4:7])
a= ", ".join(s[8:11])
print((a,r,a))
print('rata rata nilai dari masing masing tuple adalah: ')
print ([sum(map(float, filter(None, s[0:3])))/(len(s)-1),(sum(map(float, filter(None, s[4:7])))/(len(s)-1)),(sum(map(float, filter(None, s[8:11])))/(len(s)-1))])  
print('====== SARAH SAKINAH ======')
print('========= 065002100033 =========')