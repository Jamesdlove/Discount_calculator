import sys

def calculate_discount(item_cost, relative_discount, absolute_discount):
	"""calcuates a discount on a price of an item"""
	item_cost =float(item_cost)
	relative_discount = float(relative_discount)
	absolute_discount = float(absolute_discount)

	first_discount = item_cost-item_cost*relative_discount/100
	final_cost = first_discount-first_discount*absolute_discount/100
	if final_cost <= 0:
		raise ValueError("discount to large")
	if final_cost > item_cost:
		raise ValueError("thats not a discount")

	print "Final Cost is ${0:.2f}".format(final_cost)

if __name__ == '__main__':
	calculate_discount(*sys.argv[1:])
