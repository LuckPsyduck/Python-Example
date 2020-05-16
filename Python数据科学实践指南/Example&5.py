
"""
zhangheng
2019.5.25
"""

def my_abs(num):
	if num < 0:
		return -num
	else:
		return nun

def my_max(a, b):
	if a > b:
		return a
	else:
		return b

def flip(a, b):
	return b, a


#tuple\dict
def func(*args, **kwargs):
	func(1, 2, 3 ,a=1, b=2)


def fact(n):
	if n > 1:
		return n * fact(n - 1)
	else:
		return n

def div(a, b):
	try:
		ret = a / b;
	except ZeroDivisionError:
		print("invalid \n")
		ret = 0
	return ret

def div(a, b):
	try:
		ret = a / b 
	except ZeroDivisionError:
		print("invalid \n")
		ret = 0
	except (ValueError, NameError):
		print("know invalid \n")
		ret = 1 
	except:
		raise StandardError("not know invalid \n")
	finally:
		print("over !!! \n")
	return ret

                        
                        


