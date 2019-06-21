#!先用于帮助内核找到Python解释器, 但是在导入模块时, 将会被忽略. 因此只有被直接执行的文件中才有必要加入#!.
# -*- coding: utf-8 -*-
# __author__ = 'Snowming'
# Description: Snowming is a tool that identifies the hash mode of ciphers. This tools can be used as the pre-step for password cracking. This tool can be used by both input cipher one by one or select the file of ciphers collection.

def banner():
# Snowming's banner, doubled slashes added for proper formatting when banner is shown in STDOUT.
    print("-" * 100)
    print("""
                          ___                       _
                         / __|_ _  _____ __ ___ __ (_)_ _  __ _
                         \__ \ ' \/ _ \ V  V / '  \| | ' \/ _` |
                         |___/_||_\___/\_/\_/|_|_|_|_|_||_\__, |
                                                          |___/

Snowming        | A tool for cipher identification. Supporting 300+ kinds of encryption types.
Support version | Python 3
Writer          | Written by Snowming
""")
    print("Usage           | python hash_identification.py")
    print("Next step       | Input the cipher you want to know its encryption type.")
    print()
    print("-" * 100)
    print()
