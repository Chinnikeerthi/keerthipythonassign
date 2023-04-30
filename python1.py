book1price = 499.00   #cost of python programming book
book2price = 855.00   #cost of python libraries cookbook
book3price = 645.00  #cost of data science in python book
totalprice = book1price+book2price+book3price #total price of 3 books
gst = 0.12 #gst included
delivery = 250.00 #delivery charges
taxamount = gst * totalprice  #total tax for 3 books
totalamount = taxamount + delivery + totalprice #total amount for 3 books
print(totalamount)