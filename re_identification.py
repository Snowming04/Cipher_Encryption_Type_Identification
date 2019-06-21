# -*- coding: utf-8 -*-
# __author__ = 'Snowming'

import re
from common_function import print_encryption


# TODO(Snowming, kirioxiang1@gmail.com):在想这个要不要写成类，再在其中 def bcrypt(): 这样
def re_identify(user_input):
    # $id$salt$hashed
    cipher = user_input.strip()
    encryption_type = "Sorry cannot identify."
    bcrypt_pattern = r'^\$2[abxy]\$(0[4-9]|1[0-8])\$[.\/A-Za-z0-9]{53}$'
    bcrypt_result = re.match(bcrypt_pattern, cipher)
    if (bcrypt_result != None):
        # TODO(Snowming, kirioxiang1@gmail.com): 这句过长。
        encryption_type = "Authentication method may be: Bcrypt. Bcrypt is one kind of Key derivation functions."
    # TODO(Snowming, kirioxiang1@gmail.com):下面的判断多次重复，可以设为一个方法。
    if(encryption_type != "Sorry cannot identify."):
        print_encryption(encryption_type)
    return encryption_type
