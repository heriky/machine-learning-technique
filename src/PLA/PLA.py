# -*- coding:utf-8 -*-
# PLA 算法

import numpy as np
import matplotlib.pyplot as plt
import operator
import time

train_data = array([
	[1, 1, 4],
	[1, 2, 3],
	[1, -2, 3],
	[1, 0, 1],
	[1, 1, 2]
	])

train_label = [1, 1, 1, -1, -1, -1]

def sign(X):
	return 1 if X>0 else -1
