#!/usr/bin/python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

# For more fun!
from random import shuffle

# https://hu.wikipedia.org/wiki/Hangut%C3%A1nz%C3%B3_sz%C3%B3#Hangut%C3%A1nz%C3%B3_szavak_alkot%C3%A1sa

# TODO: There is still room for improvement!
verbal_particles = ['', 'agyon', 'át', 'be', 'bele', 'el', 'elő', 'fel', 'föl', 'hátra', 'haza', 'helyre', 'hozzá',
                    'ide', 'keresztbe', 'keresztül', 'készen', 'ki', 'körbe', 'körül', 'közbe', 'le', 'meg', 'mellé',
                    'neki', 'oda', 'össze', 'rá', 'rendbe', 'széjjel', 'szembe', 'szét', 'tele', 'túl', 'végig',
                    'vissza', 'viszont']
# TODO: Improve this further!
suffixes = {('a', 'á', 'u', 'ú', 'í', 'o', 'ó'): ['an', 'ag', 'og'],
            ('e', 'é', 'i'): ['en', 'eg', 'ol'],
            ('ö', 'ő', 'ü', 'ű'): ['ög', 'ít']}
Vowels = ['a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'ö', 'ő', 'u', 'ú', 'ü', 'ű']
Consonants = ['b', 'c', 'cs', 'd', 'dz', 'dzs', 'f', 'g', 'gy', 'h', 'j', 'k', 'l', 'ly', 'm', 'n', 'ny', 'p', 'r', 's',
              'sz', 't', 'ty', 'v', 'z', 'zs']
DoubleConsonants = ['bb', 'cc', 'ccs', 'dd', 'ddz', 'ddzs', 'ff', 'gg', 'ggy', 'hh', 'jj', 'kk', 'll', 'lly', 'mm',
                    'nn', 'nny', 'pp', 'rr', 'ss', 'ssz', 'tt', 'tty', 'vv', 'zz', 'zzs']

onomatopoeic_words = []

for c in Consonants:
    for v in Vowels:
        for dc in DoubleConsonants:
            suff = ''
            for s, suffs in suffixes.items():
                shuffle(suffs)
                suff = suffs[0]
                if v in s:
                    break
            for part in verbal_particles:
                onomatopoeic_words.append('{0}{1}{2}{3}{4}'.format(part, c, v, dc, suff))


shuffle(onomatopoeic_words)

for w in onomatopoeic_words:
    print(w)
