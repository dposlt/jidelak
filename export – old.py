# -*- coding: utf-8 -*-

from xlrd import open_workbook
book = open_workbook('poledni menu.xls',encoding_override="cp1250")

def list(book):
    sheet = book.sheet_by_index(0)
    return sheet

def den():
    cell = list(book).cell(3,1)
    return cell.value

def predkrm():
    h1 = list(book).cell(5,1).value
    obsah = dict()
    pole = []
    for row_index in range(list(book).nrows):
        if row_index >= 6 and row_index<=10:
            if list(book).cell(row_index,1).value != "":
                obsah[(list(book).cell(row_index,1).value)] = list(book).cell(row_index,2).value
                pole.append((list(book).cell(row_index,1).value))

    return (pole,obsah,h1)

def polevka():
    h1 = list(book).cell(12,1).value
    obsah = dict()
    pole = []
    for row_index in range(list(book).nrows):
        if row_index >= 13 and row_index<=15:
            if list(book).cell(row_index,1).value != "":
                obsah[(list(book).cell(row_index,1).value)] = list(book).cell(row_index,2).value
                pole.append((list(book).cell(row_index,1).value))
    
    return (pole,obsah,h1)

def tip():
    h1 = list(book).cell(16,1).value
    obsah = dict()
    pole = []
    for row_index in range(list(book).nrows):
        if row_index >= 17 and row_index<=24:
            if list(book).cell(row_index,1).value != "":
                obsah[(list(book).cell(row_index,1).value)] = list(book).cell(row_index,2).value
                pole.append((list(book).cell(row_index,1).value))
    
    return (pole,obsah,h1)
'''
def zverina():
    h1 = list(book).cell(20,1).value
    obsah = dict()
    pole = []
    for row_index in range(list(book).nrows):
        if row_index >= 21 and row_index<=23:
            if list(book).cell(row_index,1).value != "":
                obsah[(list(book).cell(row_index,1).value)] = list(book).cell(row_index,2).value
                pole.append((list(book).cell(row_index,1).value))
    return (pole,obsah,h1)

def hovezi():
    h1 = list(book).cell(24,1).value
    obsah = dict()
    pole = []
    for row_index in range(list(book).nrows):
        if row_index >= 25 and row_index<=30:
            if list(book).cell(row_index,1).value != "":
                obsah[(list(book).cell(row_index,1).value)] = list(book).cell(row_index,2).value
                pole.append((list(book).cell(row_index,1).value))
    
    
    return (pole,obsah,h1)

def veprove():
    h1 = list(book).cell(31,1).value
    obsah = dict()
    pole = []
    for row_index in range(list(book).nrows):
        if row_index >= 32 and row_index<=36:
            if list(book).cell(row_index,1).value != "":
                obsah[(list(book).cell(row_index,1).value)] = list(book).cell(row_index,2).value
                pole.append((list(book).cell(row_index,1).value))

    return (pole,obsah,h1)

def drubezi():
    h1 = list(book).cell(38,1).value
    obsah = dict()
    pole = []
    for row_index in range(list(book).nrows):
        if row_index >= 39 and row_index<=43:
            if list(book).cell(row_index,1).value != "":
                obsah[(list(book).cell(row_index,1).value)] = list(book).cell(row_index,2).value
                pole.append((list(book).cell(row_index,1).value))
    
    return (pole,obsah,h1)


def bezmasa():
    h1 = list(book).cell(44,1).value
    obsah = dict()
    pole = []
    for row_index in range(list(book).nrows):
        if row_index >= 45 and row_index<=49:
            if list(book).cell(row_index,1).value != "":
                obsah[(list(book).cell(row_index,1).value)] = list(book).cell(row_index,2).value
                pole.append((list(book).cell(row_index,1).value))
    
    return (pole,obsah,h1)

def salaty():
    h1 = list(book).cell(51,1).value
    obsah = dict()
    pole = []
    for row_index in range(list(book).nrows):
        if row_index >= 52 and row_index<=56:
            if list(book).cell(row_index,1).value != "":
                obsah[(list(book).cell(row_index,1).value)] = list(book).cell(row_index,2).value
                pole.append((list(book).cell(row_index,1).value))
    
    return (pole,obsah,h1)

def deserty():
    h1 = list(book).cell(58,1).value
    obsah = dict()
    pole = []
    for row_index in range(list(book).nrows):
        if row_index >= 59 and row_index<=64:
            if list(book).cell(row_index,1).value != "":
                obsah[(list(book).cell(row_index,1).value)] = list(book).cell(row_index,2).value
                pole.append((list(book).cell(row_index,1).value))
    return (pole,obsah,h1)
'''
def napoje():
    h1 = list(book).cell(31,1).value
    obsah = dict()
    pole = []
    for row_index in range(list(book).nrows):
        if row_index >= 32 and row_index<=35:
            if list(book).cell(row_index,1).value != "":
                obsah[(list(book).cell(row_index,1).value)] = list(book).cell(row_index,2).value
                pole.append((list(book).cell(row_index,1).value))
    
    return (pole,obsah,h1)

def dalsi():
    h1 = list(book).cell(38,1).value
    obsah = dict()
    for row_index in range(list(book).nrows):
        if row_index >= 39 and row_index <= 40:
            if list(book).cell(row_index,1).value != "":
                obsah[(list(book).cell(row_index,1).value)] = list(book).cell(row_index,2).value
    
    return (obsah,h1)


def prevodHtml():
    (polePredkrm,obsahPredkrm,h1Predkrm) = predkrm()
    Kc = u" Kč"
    string = ""
    string += '<h3><strong><span style="color: #008000;">'+"{0}".format( den().encode('cp1250','ignore'))+'</span></strong></h3>&nbsp;<br>'
    string += '<span style="color: #800000;"><strong>'+"{0}".format( h1Predkrm.encode('cp1250','ignore'))+'</strong></span>'
    string += '<table class="jidlo" style="width: 100%;" border="0"><tbody>'
    for i in polePredkrm:
        if i in obsahPredkrm:
            string += '<tr><td><span style="color: #000000;">'+"{0}".format( i.encode('cp1250', 'ignore'))+'</span></td><td align="right" width="40"><span style="color: #000000;">'+"{0}{1}".format(str(int(obsahPredkrm[i])),Kc.encode('cp1250','ignore'))+'</span></td></tr>'
    string += '</tbody></table>'

    (polePolevky,obsahPolevky,h1Polevky) = polevka()
    string += '<span style="color: #800000;"><strong>'+"{0}".format( h1Polevky.encode('cp1250','ignore'))+'</strong></span>'
    string += '<table class="jidlo" style="width: 100%;" border="0"><tbody>'
    for i in polePolevky:
        if i in obsahPolevky:
            string += '<tr><td><span style="color: #000000;">'+"{0}".format( i.encode('cp1250', 'ignore'))+'</span></td><td align="right" width="40"><span style="color: #000000;">'+"{0}{1}".format(str(int(obsahPolevky[i])),Kc.encode('cp1250','ignore'))+'</span></td></tr>'
    string += '</tbody></table>'

    (poleTip,obsahTip,h1Tip) = tip()
    string += '<span style="color: #800000;"><strong>'+"{0}".format( h1Tip.encode('cp1250','ignore'))+'</strong></span>'
    string += '<table class="jidlo" style="width: 100%;" border="0"><tbody>'
    for i in poleTip:
        if i in obsahTip:
            string += '<tr><td><span style="color: #000000;">'+"{0}".format( i.encode('cp1250', 'ignore'))+'</span></td><td align="right" width="40"><span style="color: #000000;">'+"{0}{1}".format(str(int(obsahTip[i])),Kc.encode('cp1250','ignore'))+'</span></td></tr>'
    string += '</tbody></table>'
'''
    (poleZverina,obsahZverina, h1Zverina) = zverina()
    string += '<span style="color: #800000;"><strong>'+"{0}".format( h1Zverina.encode('cp1250','ignore'))+'</strong></span>'
    string += '<table class="jidlo" style="width: 100%;" border="0"><tbody>'
    for i in poleZverina:
        if i in obsahZverina:
            string += '<tr><td><span style="color: #000000;">'+"{0}".format( i.encode('cp1250', 'ignore'))+'</span></td><td align="right" width="40"><span style="color: #000000;">'+"{0}{1}".format(str(int(obsahZverina[i])),Kc.encode('cp1250','ignore'))+'</span></td></tr>'
    string += '</tbody></table>'

    (poleHovezi,obsahHovezi, h1Hovezi) = hovezi()
    string += '<span style="color: #800000;"><strong>'+"{0}".format( h1Hovezi.encode('cp1250','ignore'))+'</strong></span>'
    string += '<table class="jidlo" style="width: 100%;" border="0"><tbody>'
    for i in poleHovezi:
        if i in obsahHovezi:
            string += '<tr><td><span style="color: #000000;">'+"{0}".format( i.encode('cp1250', 'ignore'))+'</span></td><td align="right" width="40"><span style="color: #000000;">'+"{0}{1}".format(str(int(obsahHovezi[i])),Kc.encode('cp1250','ignore'))+'</span></td></tr>'
    string += '</tbody></table>'

    (poleVeprove,obsahVeprove, h1Veprove) = veprove()
    string += '<span style="color: #800000;"><strong>'+"{0}".format( h1Veprove.encode('cp1250','ignore'))+'</strong></span>'
    string += '<table class="jidlo" style="width: 100%;" border="0"><tbody>'
    for i in poleVeprove:
        if i in obsahVeprove:
            string += '<tr><td><span style="color: #000000;">'+"{0}".format( i.encode('cp1250', 'ignore'))+'</span></td><td align="right" width="40"><span style="color: #000000;">'+"{0}{1}".format(str(int(obsahVeprove[i])),Kc.encode('cp1250','ignore'))+'</span></td></tr>'
    string += '</tbody></table>'

    (poleDrubezi,obsahDrubezi, h1Drubezi) = drubezi()
    string += '<span style="color: #800000;"><strong>'+"{0}".format( h1Drubezi.encode('cp1250','ignore'))+'</strong></span>'
    string += '<table class="jidlo" style="width: 100%;" border="0"><tbody>'
    for i in poleDrubezi:
        if i in obsahDrubezi:
            string += '<tr><td><span style="color: #000000;">'+"{0}".format( i.encode('cp1250', 'ignore'))+'</span></td><td align="right" width="40"><span style="color: #000000;">'+"{0}{1}".format(str(int(obsahDrubezi[i])),Kc.encode('cp1250','ignore'))+'</span></td></tr>'
    string += '</tbody></table>'


    (poleBezmasa,obsahBezmasa, h1Bezmasa) = bezmasa()
    string += '<span style="color: #800000;"><strong>'+"{0}".format( h1Bezmasa.encode('cp1250','ignore'))+'</strong></span>'
    string += '<table class="jidlo" style="width: 100%;" border="0"><tbody>'
    
    for i in poleBezmasa:
        if i in obsahBezmasa:
            string += '<tr><td><span style="color: #000000;">'+"{0}".format( i.encode('cp1250', 'ignore'))+'</span></td><td align="right" width="40"><span style="color: #000000;">'+"{0}{1}".format(str(int(obsahBezmasa[i])),Kc.encode('cp1250','ignore'))+'</span></td></tr>'
            
    string += '</tbody></table>'

    (poleSalaty,obsahSalaty, h1Salaty) = salaty()
    string += '<span style="color: #800000;"><strong>'+"{0}".format( h1Salaty.encode('cp1250','ignore'))+'</strong></span>'
    string += '<table class="jidlo" style="width: 100%;" border="0"><tbody>'
    for i in poleSalaty:
        if i in obsahSalaty:
            string += '<tr><td><span style="color: #000000;">'+"{0}".format( i.encode('cp1250', 'ignore'))+'</span></td><td align="right" width="40"><span style="color: #000000;">'+"{0}{1}".format(str(int(obsahSalaty[i])),Kc.encode('cp1250','ignore'))+'</span></td></tr>'
    string += '</tbody></table>'

    (poleDeserty,obsahDeserty,h1Deserty) = deserty()
    string += '<span style="color: #800000;"><strong>'+"{0}".format( h1Deserty.encode('cp1250','ignore'))+'</strong></span>'
    string += '<table class="jidlo" style="width: 100%;" border="0"><tbody>'
    for i in poleDeserty:
        if i in obsahDeserty:
            string += '<tr><td><span style="color: #000000;">'+"{0}".format( i.encode('cp1250', 'ignore'))+'</span></td><td align="right" width="40"><span style="color: #000000;">'+"{0}{1}".format(str(int(obsahDeserty[i])),Kc.encode('cp1250','ignore'))+'</span></td></tr>'
    string += '</tbody></table>'
 '''
    (poleNapoje,obsahNapoje, h1Napoje) = napoje()
    string += '<span style="color: #800000;"><strong>'+"{0}".format( h1Napoje.encode('cp1250','ignore'))+'</strong></span>'
    string += '<table class="jidlo" style="width: 100%;" border="0"><tbody>'
    for i in poleNapoje:
        if i in obsahNapoje:
            string += '<tr><td><span style="color: #000000;">'+"{0}".format( i.encode('cp1250', 'ignore'))+'</span></td><td align="right" width="40"><span style="color: #000000;">'+"{0}{1}".format(str(int(obsahNapoje[i])),Kc.encode('cp1250','ignore'))+'</span></td></tr>'
    string += '</tbody></table>'

    (obsahDalsi, h1Dalsi) = dalsi()
    string += '<span style="color: #800000;"><strong>'+"{0}".format( h1Dalsi.encode('cp1250','ignore'))+'</strong></span>'
    string += '<table class="jidlo" style="width: 100%;" border="0"><tbody>'
    for i in sorted(obsahDalsi):
        string += '<tr><td><span style="color: #000000;">'+"{0}".format( i.encode('cp1250', 'ignore'))+'</span></td><td align="right" width="40"><span style="color: #000000;">'+"{0}{1}".format(str(int(obsahDalsi[i])),Kc.encode('cp1250','ignore'))+'</span></td></tr>'
    string += '</tbody></table>'

    string += '<h3><strong>[singlepic id=3 w=420 h=340 mode=watermark float=center]</strong></h3>'

    
    return string

    



