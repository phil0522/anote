import google  # provided by GAE
import os
import sys

print 'google=', google.__path__
# add vendorized protobuf to google namespace package
vendor_dir = os.path.join(os.path.dirname(__file__), '../lib')
google.__path__.append(os.path.join(vendor_dir, 'google'))

# add vendor path
sys.path.insert(0, vendor_dir)