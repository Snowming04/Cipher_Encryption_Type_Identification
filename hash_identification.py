#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' main module '

__author__ = 'Snowming'

import banner
import length_identification
from char_identification import char_identify
from common_function import print_encryption
from detail_hash_type import get_type
from length_identification import length_identify
from re_identification import re_identify



# 预处理步骤
def _process(user_input):
    pass


def _identify():
    encryption_type = "Sorry cannot identify."
    user_input = input('Please input your cipher: ')
    '''
    length_identify(input)
    re_identify(input)
    char_identify(input)
    下面的判断中已经运行了一次了
    '''
    # TODO(Snowming, kirioxiang1@gmail.com):下面的判断多次重复，可以设为一个方法。
    length_result = length_identify(user_input)
    re_result = re_identify(user_input)
    if(length_result == "Sorry cannot identify." and re_result==
    "Sorry cannot identify."):
        print_encryption(encryption_type)
    else:
        if length_result == "Encryption method may be: MD5.":
            answer = input('Do you want to know more detailed hash-mode?(y/n): ')
            # TODO(Snowming, kirioxiang1@gmail.com):这里这个判断不顶用啊，用异常改写. no为什么也显示。
            if(answer == "y" or "Y" or "yes" or "YES"):
                get_type('md5_series')
        if length_result == "Encryption method may be :sha1, MySQL4.1, MySQL5+.":
            answer = input('Do you want to know more detailed hash-mode?(y/n): ')
            if(answer == "y" or "Y" or "yes" or "YES"):
                get_type('sha1_series')
        if length_result == "Encryption method may be: SHA-256.":
            answer = input('Do you want to know more detailed hash-mode?(y/n): ')
            if(answer == "y" or "Y" or "yes" or "YES"):
                get_type('sha256_series')
        if length_result == "Encryption method may be: SHA-512.":
            answer = input('Do you want to know more detailed hash-mode?(y/n): ')
            if(answer == "y" or "Y" or "yes" or "YES"):
                get_type('sha512_series')


def main():
    banner.banner()
    # TODO(Snowming, kirioxiang1@gmail.com):这里加入异常处理。
    while True:
        _identify()

if __name__ == '__main__':
    main()





'''
def next(self):
    retVal = None
    while True:
        self.counter += 1
        try:
            retVal = next(self.iter).rstrip()
        except zipfile.error as ex:
            errMsg = "something appears to be wrong with "
            errMsg += "the file '%s' ('%s'). Please make " % (self.current, getSafeExString(ex))
            errMsg += "sure that you haven't made any changes to it"
            raise SqlmapInstallationException(errMsg)
        except StopIteration:
            self.adjust()
            retVal = next(self.iter).rstrip()
        if not self.proc_count or self.counter % self.proc_count == self.proc_id:
            break
    return retVal
'''
