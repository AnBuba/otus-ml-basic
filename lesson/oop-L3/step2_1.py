from step2_0 import Notebook, Phone

# prod_1 = Notebook('ZenBook 4', 589.5)
prod_1 = Notebook('ZenBook 4', Notebook.convert_price(589.5, 1))
#
# prod_2 = Phone('Galaxy S22', 472.4)
prod_2 = Phone('Galaxy S22', Phone.convert_price(975.4, 0.650))
print(prod_1)
print(prod_2)