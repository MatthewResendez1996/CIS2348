services = {'-': 0, 'Oil change' : 35, 'Tire rotation' : 19, 'Car wash' : 7, 'Car wax' : 12}
fs = ""
ss = ""
invoice = 0
print ("Davy's auto shop services")
print ("Oil change -- $35")
print ("Tire rotation -- $19")
print ("Car wash -- $7")
print ("Car wax -- $12\n")

fs = input ("Select first service:\n")
ss = input ("Select second service:\n")

print ("\nDavy's auto shop invoice\n")

if (fs == '-'):
    print ("Service 1: No service")
else:
    print ("Service 1: %s, $%d" % (fs, services.get (fs)))
if (ss == '-'):
    print ("Service 2: No service")
else:
    print ("Service 2: %s, $%d" % (ss, services.get (ss)))

invoice = services.get(fs) + services.get(ss)
print()
print ("Total: $%d" % (invoice))


