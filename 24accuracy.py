# Accuracy by Jonathan Raigosa

import math
import sys

def accuracy_f1(tp, fp, tn, fn):
	total = tp + fp + tn + fn
	
	if total == 0:
		sys.exit('error: total cannot be zero')
	
	if tp < 0:
		sys.exit('error: tp cannot be negative')
	elif fp < 0:
		sys.exit('error: tp cannot be negative')
	elif tn < 0:
		sys.exit('error: tn cannot be negative')
	elif fn < 0:
		sys.exit('error: fn cannot be negative')
	else:
		precision = tp / (tp + fp)
		recall = tp / (tp + fn)
		accuracy = (tp + tn) / (total)
		f1_score = 2 * (precision * recall) / (precision + recall)
		return accuracy, f1_score

print(accuracy_f1(12, 15, 17, 20))
print(accuracy_f1(3, 4, 8, 9))
print(accuracy_f1(-5, 4, 3, -2))
