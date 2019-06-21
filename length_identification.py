# -*- coding: utf-8 -*-
# __author__ = 'Snowming'

from common_function import print_encryption

# TODO(Snowming, kirioxiang1@gmail.com):或者后面单独把输入字符串处理这一段取出来。
HEX_DICT = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','A',
'B','C','D','E','F']

def length_identify(user_input):
    cipher = user_input.strip()
    # 这一行好像没有用到？
    encryption_type = "Sorry cannot identify."
    one_word = 'Encryption method may be: %s.'

    # TODO(Snowming, kirioxiang1@gmail.com):字符集检验是不是可以单独拆出来?
    # TODO(Snowming, kirioxiang1@gmail.com):这一段后面用正则表达式改写。
    if len(cipher) in [16,32,40,56,64,96,128]:
        for i in cipher:
            if i not in HEX_DICT:
                # 这里加入异常
                # 其实如果恰好为32位包括F之后的字母的话也可能是base64
                encryption_type = "Sorry cannot identify."
            elif len(cipher) == 16:
                encryption_type = one_word % 'MySQL323'
            elif len(cipher) == 32:
                # encryption_type = "This is on kind of authentication method. Encryption method May be:MD5, LM hash, NTLMv1, NTLMv2."
                encryption_type = one_word % 'MD5'
            elif len(cipher) == 40:
                encryption_type = one_word % 'sha1, MySQL4.1, MySQL5+'
            elif len(cipher) == 56:
                encryption_type = one_word % 'SHA-224'
            elif len(cipher) == 64:
                encryption_type = one_word % 'SHA-256'
            elif len(cipher) == 96:
                encryption_type = one_word % 'SHA-384'
            elif len(cipher) == 128:
                encryption_type = one_word % 'SHA-512'
    # TODO(Snowming, kirioxiang1@gmail.com):下面的判断多次重复，可以设为一个方法。
    if(encryption_type != "Sorry cannot identify."):
        print_encryption(encryption_type)
    return encryption_type
