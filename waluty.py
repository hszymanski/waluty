#!/usr/bin/env python
# -*- coding: utf-8 -*-
# skrypt wyświetla aktualny kurs walut Narodowego Banku Polskiego

import urllib2
import re

www = urllib2.urlopen("http://www.nbp.pl/home.aspx?f=/kursy/kursya.html")
html = www.read()

format = r"(?<=<div>Tabela z dnia ).+(?=</div>)"
wzor1 = r"(?<=<tr><td>1 EUR</td><td>).+(?=</td></tr>)"
wzor2 = r"(?<=<tr><td>1 USD</td><td>).+(?=</td></tr>)"
wzor3 = r"(?<=<tr><td>1 CHF</td><td>).+(?=</td></tr>)"
wzor4 = r"(?<=<tr><td>1 GBP</td><td>).+(?=</td></tr>)"

data = re.findall(format, html)
euro = re.findall(wzor1, html)
dolar = re.findall(wzor2, html)
frank = re.findall(wzor3, html)
funt = re.findall(wzor4, html)

print "Kurs walut z dnia:", data[0]
print "Euro:", euro[0]
print "Dolar amerykański:", dolar[0]
print "Frank szwajcarski:", frank[0]
print "Funt brytyjski:", funt[0]
