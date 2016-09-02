# -*- coding: utf-8 -*-

from xlrd import open_workbook
book = open_workbook('poledni menu.xls',encoding_override="cp1250")

def list(book):
    sheet = book.sheet_by_index(0)
    return sheet

# sekce pocinajici dnem
def den():
    cell = list(book).cell(3,1)
    return cell.value

def tydenni():
    h1 = list(book).cell(5,1).value
    obsah = dict()
    pole = []
    for row_index in range(list(book).nrows):
        if row_index >= 6 and row_index<=10:
            if list(book).cell(row_index,1).value != "":
                obsah[(list(book).cell(row_index,1).value)] = list(book).cell(row_index,2).value
                pole.append((list(book).cell(row_index,1).value))

    return (pole,obsah,h1)

def pondeli():
    h1 = list(book).cell(12,1).value
    obsah = dict()
    pole = []
    for row_index in range(list(book).nrows):
        if row_index >= 13 and row_index<=17:
            if list(book).cell(row_index,1).value != "":
                obsah[(list(book).cell(row_index,1).value)] = list(book).cell(row_index,2).value
                pole.append((list(book).cell(row_index,1).value))

    return (pole,obsah,h1)

def utery():
    h1 = list(book).cell(19,1).value
    obsah = dict()
    pole = []
    for row_index in range(list(book).nrows):
        if row_index >= 20 and row_index<=24:
            if list(book).cell(row_index,1).value != "":
                obsah[(list(book).cell(row_index,1).value)] = list(book).cell(row_index,2).value
                pole.append((list(book).cell(row_index,1).value))
    
    return (pole,obsah,h1)

def streda():
    h1 = list(book).cell(26,1).value
    obsah = dict()
    pole = []
    for row_index in range(list(book).nrows):
        if row_index >= 27 and row_index<=31:
            if list(book).cell(row_index,1).value != "":
                obsah[(list(book).cell(row_index,1).value)] = list(book).cell(row_index,2).value
                pole.append((list(book).cell(row_index,1).value))
    
    return (pole,obsah,h1)

def ctvrtek():
    h1 = list(book).cell(33,1).value
    obsah = dict()
    pole = []
    for row_index in range(list(book).nrows):
        if row_index >= 34 and row_index<=38:
            if list(book).cell(row_index,1).value != "":
                obsah[(list(book).cell(row_index,1).value)] = list(book).cell(row_index,2).value
                pole.append((list(book).cell(row_index,1).value))
    
    return (pole,obsah,h1)

def patek():
    h1 = list(book).cell(40,1).value
    obsah = dict()
    pole = []
    for row_index in range(list(book).nrows):
        if row_index >= 41 and row_index <= 45:
            if list(book).cell(row_index,1).value != "":
                obsah[(list(book).cell(row_index,1).value)] = list(book).cell(row_index,2).value
                pole.append((list(book).cell(row_index,1).value))
    return (pole,obsah,h1)

def napoje():
    h1 = list(book).cell(47,1).value
    obsah = dict()
    pole = []
    for row_index in range(list(book).nrows):
        if row_index >= 48 and row_index <= 52:
            if list(book).cell(row_index,1).value != "":
                obsah[(list(book).cell(row_index,1).value)] = list(book).cell(row_index,2).value
                pole.append((list(book).cell(row_index,1).value))
    return (pole,obsah,h1)

# hlavni metoda pro prevod jednotlivych sekci

def prevodHtml():
    # zobrazi den
    (poleTydenni,obsahTydenni,h1Tydenni) = tydenni()
    Kc = u" Kč"
    string = ""
    string += '<h3><strong><span style="color: #008000;">'+"{0}".format( den().encode('cp1250','ignore'))+'</span></strong></h3>&nbsp;<br>'
    string += '<span style="color: #800000;"><strong>'+"{0}".format( h1Tydenni.encode('cp1250','ignore'))+'</strong></span>'
    string += '<table class="jidlo" style="width: 100%;" border="0"><tbody>'
    for i in poleTydenni:
        if i in obsahTydenni:
            string += '<tr><td><span style="color: #000000;">'+"{0}".format( i.encode('cp1250', 'ignore'))+'</span></td><td align="right" width="40"><span style="color: #000000;">'+"{0}{1}".format(str(int(obsahTydenni[i])),Kc.encode('cp1250','ignore'))+'</span></td></tr>'
    string += '</tbody></table>'
    
    (polePolevky,obsahPolevky,h1Polevky) = pondeli()
    string += '<span style="color: #800000;"><strong>'+"{0}".format( h1Polevky.encode('cp1250','ignore'))+'</strong></span>'
    string += '<table class="jidlo" style="width: 100%;" border="0"><tbody>'
    for i in polePolevky:
        if i in obsahPolevky:
            string += '<tr><td><span style="color: #000000;">'+"{0}".format( i.encode('cp1250', 'ignore'))+'</span></td><td align="right" width="40"><span style="color: #000000;">'+"{0}{1}".format(str(int(obsahPolevky[i])),Kc.encode('cp1250','ignore'))+'</span></td></tr>'
    string += '</tbody></table>'
    
    (polePolevky,obsahPolevky,h1Polevky) = utery()
    string += '<span style="color: #800000;"><strong>'+"{0}".format( h1Polevky.encode('cp1250','ignore'))+'</strong></span>'
    string += '<table class="jidlo" style="width: 100%;" border="0"><tbody>'
    for i in polePolevky:
        if i in obsahPolevky:
            string += '<tr><td><span style="color: #000000;">'+"{0}".format( i.encode('cp1250', 'ignore'))+'</span></td><td align="right" width="40"><span style="color: #000000;">'+"{0}{1}".format(str(int(obsahPolevky[i])),Kc.encode('cp1250','ignore'))+'</span></td></tr>'
    string += '</tbody></table>'
    
    (poleTip,obsahTip,h1Tip) = streda()
    string += '<span style="color: #800000;"><strong>'+"{0}".format( h1Tip.encode('cp1250','ignore'))+'</strong></span>'
    string += '<table class="jidlo" style="width: 100%;" border="0"><tbody>'
    for i in poleTip:
        if i in obsahTip:
            string += '<tr><td><span style="color: #000000;">'+"{0}".format( i.encode('cp1250', 'ignore'))+'</span></td><td align="right" width="40"><span style="color: #000000;">'+"{0}{1}".format(str(int(obsahTip[i])),Kc.encode('cp1250','ignore'))+'</span></td></tr>'
    string += '</tbody></table>'

    (poleNapoje,obsahNapoje, h1Napoje) = ctvrtek()
    string += '<span style="color: #800000;"><strong>'+"{0}".format( h1Napoje.encode('cp1250','ignore'))+'</strong></span>'
    string += '<table class="jidlo" style="width: 100%;" border="0"><tbody>'
    for i in poleNapoje:
        if i in obsahNapoje:
            string += '<tr><td><span style="color: #000000;">'+"{0}".format( i.encode('cp1250', 'ignore'))+'</span></td><td align="right" width="40"><span style="color: #000000;">'+"{0}{1}".format(str(int(obsahNapoje[i])),Kc.encode('cp1250','ignore'))+'</span></td></tr>'
    string += '</tbody></table>'

    (poleDalsi,obsahDalsi, h1Dalsi) = patek()
    string += '<span style="color: #800000;"><strong>'+"{0}".format( h1Dalsi.encode('cp1250','ignore'))+'</strong></span>'
    string += '<table class="jidlo" style="width: 100%;" border="0"><tbody>'
    for i in poleDalsi:
        if i in obsahDalsi:
            string += '<tr><td><span style="color: #000000;">'+"{0}".format( i.encode('cp1250', 'ignore'))+'</span></td><td align="right" width="40"><span style="color: #000000;">'+"{0}{1}".format(str(int(obsahDalsi[i])),Kc.encode('cp1250','ignore'))+'</span></td></tr>'
    string += '</tbody></table>'

    (poleNapoje,obsahNapoje, h1Napoje) = napoje()
    string += '<span style="color: #800000;"><strong>'+"{0}".format( h1Napoje.encode('cp1250','ignore'))+'</strong></span>'
    string += '<table class="jidlo" style="width: 100%;" border="0"><tbody>'
    for i in poleNapoje:
        if i in obsahNapoje:
            string += '<tr><td><span style="color: #000000;">'+"{0}".format( i.encode('cp1250', 'ignore'))+'</span></td><td align="right" width="40"><span style="color: #000000;">'+"{0}{1}".format(str(int(obsahNapoje[i])),Kc.encode('cp1250','ignore'))+'</span></td></tr>'
    string += '</tbody></table>'
    
    string += '<h3><strong>[singlepic id=3 w=420 h=340 mode=watermark float=center]</strong></h3>'

    
    return string

    



