# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
from unittest import main
# import pprint as pprint

print(mean_var_std.calculate([0,1,2,3,4,5,6,7,8]))
# If desirable you could use the pprint func:
# pprint(mean_var_std.calculate([0,1,2,3,4,5,6,7,8]))

# Run unit tests automatically
# main(module='test_module', exit=False)
