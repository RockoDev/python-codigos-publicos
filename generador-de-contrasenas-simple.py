# coding: utf-8

import random

def password(length):
    """Return the password"""
    res = ""
    for _ in range(int(length)):
        res = res + random.choice(random.choice([
            map(chr, xrange(ord('a'), ord('z')+1)),
            map(chr, xrange(ord('A'), ord('Z')+1)),
            map(str, range(10)),
            [
                'ñ', 'Ñ', '-', '.', ',', '_',
                '@', '#', '$', '%', '&', '/',
                '(', ')', '<', '>', '{', '}',
                '[', ']', '¿', '?', '¡', '!',
                '+', '*', '=',
            ]
        ]))
    return res

print password(input('Ingresa el número de caracteres que quieres que tenga la contraseña:'))
