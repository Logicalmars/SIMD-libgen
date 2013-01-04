
# Copyright (c) 2011, Hua Huang and Robert D. Cameron.
# Licensed under the Academic Free License 3.0. 

def GetResult(fw, data):
	(arg1, arg2) = (data[0], data[1])
	(i, sz, ans) = (0, len(arg1), "")
	while i<sz:
		for j in range(fw):
			curPos = i+j
			if(arg1[curPos]==arg2[curPos] and arg1[curPos]=="0"):
				ans += "0"
			else:
				ans += "1"
		i += fw
	return ans