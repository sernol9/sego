#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05\SelfCheck170-2.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05
# Created Date: Friday, May 1st 2020, 4:25:25 pm
# Author: Olivia Serna
# Description: 
# -----
# Last Modified: Fri May 01 2020
# Modified By: Olivia Serna
# -----
# Copyright (c) 2020 OLI CO. LTD.
# 
# Know thy self, know thy enemy. A thousand battles, a thousand victories
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	----------------------------------------------------------
###

numbers = list(range(1,16))
print(numbers)

del numbers[:4]
print(numbers)

del numbers[::2]
print(numbers)