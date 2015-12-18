import my_module

celsius = float(raw_input("Input a temperature in Celsius: "))
fahrenheit = my_module.c_to_f(celsius)
print "This is ", fahrenheit, "degrees Fahrenheit."
