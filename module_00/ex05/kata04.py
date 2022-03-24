t = (0, 4, 132.42222, 10000, 12345.67)

# module_00, ex_04 : 132.42, 1.00e+04, 1.23e+04
print("module_{module:02}, ex_{ex:0>2} : {round:.2f}, {expo:1.2e}, {power:.3}"
      .format(module=t[0], ex=t[1], round=t[2], expo=t[3], power=t[4]))
