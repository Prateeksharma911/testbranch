
from pydash import find


tests_price = [{'practo_lab_dos_id': 1056042, 'vendor_lab_dos_id': 1051330, 'vendor_lab_id': 2413, 'max_price': 300, 'margin_price': 250, 'discounted_price': 200}]
print((str(type(tests_price))))
test_price = find(tests_price, {'vendor_lab_dos_id': 1051330})

max_price = test_price.get('max_price')



print(max_price)
