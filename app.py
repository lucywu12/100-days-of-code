# 1/9 Packages
# Method 1: import the package and file you need
import ecommerce.shipping
ecommerce.shipping.calc_shipping()

# Method 2: import the specific function you need
from ecommerce.shipping import calc_shipping
calc_shipping()

# Method 3: import all of the functions in a specific file
from ecommerce import shipping
shipping.calc_shipping()
