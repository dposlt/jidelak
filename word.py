# -*- coding: cp1250 -*-
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, SimpleDocTemplate, Image, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.colors import red
from reportlab.lib.units import cm,mm, inch

pdfmetrics.registerFont(TTFont('AmorSerifRegularPro.ttf', 'AmorSerifRegularPro.ttf'))
pdfmetrics.registerFont(TTFont('AmorSerifRegularProBold.ttf', 'AmorSerifRegularProBold.ttf'))
styles = getSampleStyleSheet()
import export

#global names
kc = u'Kč'
def name():
    pdf_file_name = 'jidelni listek '
    datum = export.den()
    name = pdf_file_name+' '+datum+'.pdf'
    return name


#function
def getDatum():
    datum = export.den()
    return datum

def getImage(width,height):
    I = Image('obr/logo.png')
    I.drawHeight = height
    I.drawWidth = width

    return I

def newLine(staff):
    import textwrap
    dedented_text = textwrap.dedent(staff).strip()
    return textwrap.fill(dedented_text,width=65)
    


def createPdf():
    #vlastnosti
    fontsize = 14
    headsize = 16
    colwidths = (550, 52)
    rolheight = 19
    Story = []

    #obsah

    ###  page 1   ###
    
    mezera = ParagraphStyle('text',
                              fontName='AmorSerifRegularPro.ttf',
                              fontSize=fontsize,
                              spaceAfter = 15,
                              alignment = TA_CENTER
                              )
    p = Paragraph('',mezera)
    Story.append(p)
    
    text = u'TÝDENNÍ MENU'+' '+getDatum() 
    headtext = ParagraphStyle('text',
                              fontName='AmorSerifRegularPro.ttf',
                              fontSize = headsize,
                              spaceAfter = 15,
                              alignment = TA_CENTER
                              )
    
    p = Paragraph(text,headtext)
    Story.append(p)

    mezera = ParagraphStyle('text',
                              fontName='AmorSerifRegularPro.ttf',
                              fontSize=fontsize,
                              spaceAfter = 35,
                              alignment = TA_CENTER
                              )
    p = Paragraph('',mezera)
    Story.append(p)
    '''
    Story.append(getImage(220,250))

    text = u'U Žíznivého'
    jelentext = ParagraphStyle('jelentext',
                               fontName='AmorSerifRegularPro.ttf',
                               fontSize= headsize,
                               spaceAfter = 15,
                               alignment = TA_CENTER
                               )

    p = Paragraph(text,jelentext)
    Story.append(p)

    text = u'jelena'
    jelentext = ParagraphStyle('jelentext',
                               fontName='AmorSerifRegularPro.ttf',
                               fontSize= headsize,
                               alignment = TA_CENTER
                               )

    p = Paragraph(text,jelentext)
    #Story.append(p)
    '''

    '''
    #tydenni
    (pole,obsah,h1) = export.tydenni()
    h1Obsah = ParagraphStyle('h1',
                        fontName='AmorSerifRegularProBold.ttf',
                        fontSize= fontsize,
                        spaceAfter = 0,
                        alignment = TA_CENTER
                        )

    p = Paragraph(h1,h1Obsah)
    Story.append(p)
    
    #rowheights = (24, 16)
    for i in pole:
        data = [[newLine(i),str(int(obsah[i]))+kc]]
        t = Table(data, colwidths,rolheight)
        
        t.setStyle(TableStyle([('FONT',(0,0),(-1,-1),'AmorSerifRegularProBold.ttf'),
                               ('ALIGN',(0,0),(0,0),'LEFT'),
                               ('SIZE',(0,0),(-1,-1),fontsize)]))
    
        
        Story.append(t)
    '''
    #pondeli	
    (pole,obsah,h1) = export.pondeli()
    h1Obsah = ParagraphStyle('h1',
                        fontName='AmorSerifRegularProBold.ttf',
                        fontSize= fontsize,
                        spaceAfter = 0,
                        spaceBefore = 0,
                        alignment = TA_CENTER
                        )

    p = Paragraph(h1,h1Obsah)
    Story.append(p)
    
    for i in pole:
        data = [[newLine(i),str(int(obsah[i]))+kc]]
        t = Table(data, colwidths,rolheight)
        
        t.setStyle(TableStyle([('FONT',(0,0),(-1,-1),'AmorSerifRegularProBold.ttf'),
                               ('ALIGN',(0,0),(0,0),'LEFT'),
                               ('SIZE',(0,0),(-1,-1),fontsize)]))
    
        
        Story.append(t)

    
    
    mezera = ParagraphStyle('text',
                              fontName='AmorSerifRegularPro.ttf',
                              fontSize=fontsize,
                              spaceAfter = 0,
                              alignment = TA_CENTER
                              )
    p = Paragraph('',mezera)
    Story.append(p)

    #utery	
    (pole,obsah,h1) = export.utery()
    h1Obsah = ParagraphStyle('h1',
                        fontName='AmorSerifRegularProBold.ttf',
                        fontSize= fontsize,
                        spaceAfter = 0,
                        spaceBefore = 0,
                        alignment = TA_CENTER
                        )

    p = Paragraph(h1,h1Obsah)
    Story.append(p)
    
    for i in pole:
        data = [[newLine(i),str(int(obsah[i]))+kc]]
        t = Table(data, colwidths,rolheight)
        
        t.setStyle(TableStyle([('FONT',(0,0),(-1,-1),'AmorSerifRegularProBold.ttf'),
                               ('ALIGN',(0,0),(0,0),'LEFT'),
                               ('SIZE',(0,0),(-1,-1),fontsize)]))
    
        
        Story.append(t)

    
    
    mezera = ParagraphStyle('text',
                              fontName='AmorSerifRegularPro.ttf',
                              fontSize=fontsize,
                              spaceAfter = 0,
                              alignment = TA_CENTER
                              )
    p = Paragraph('',mezera)
    Story.append(p)

    #streda	
    (pole,obsah,h1) = export.streda()
    h1Obsah = ParagraphStyle('h1',
                        fontName='AmorSerifRegularProBold.ttf',
                        fontSize= fontsize,
                        spaceAfter = 0,
                        spaceBefore = 0,
                        alignment = TA_CENTER
                        )

    p = Paragraph(h1,h1Obsah)
    Story.append(p)
    
    for i in pole:
        data = [[newLine(i),str(int(obsah[i]))+kc]]
        t = Table(data, colwidths,rolheight)
        
        t.setStyle(TableStyle([('FONT',(0,0),(-1,-1),'AmorSerifRegularProBold.ttf'),
                               ('ALIGN',(0,0),(0,0),'LEFT'),
                               ('SIZE',(0,0),(-1,-1),fontsize)]))
    
        
        Story.append(t)

    
    
    mezera = ParagraphStyle('text',
                              fontName='AmorSerifRegularPro.ttf',
                              fontSize=fontsize,
                              spaceAfter = 0,
                              alignment = TA_CENTER
                              )
    p = Paragraph('',mezera)
    Story.append(p)

    #ctvrtek
    (pole,obsah,h1) = export.ctvrtek()
    h1Obsah = ParagraphStyle('h1',
                        fontName='AmorSerifRegularProBold.ttf',
                        fontSize= fontsize,
                        spaceAfter = 0,
                        spaceBefore = 0,
                        alignment = TA_CENTER
                        )

    p = Paragraph(h1,h1Obsah)
    Story.append(p)
    
    for i in pole:
        data = [[newLine(i),str(int(obsah[i]))+kc]]
        t = Table(data, colwidths,rolheight)
        
        t.setStyle(TableStyle([('FONT',(0,0),(-1,-1),'AmorSerifRegularProBold.ttf'),
                               ('ALIGN',(0,0),(0,0),'LEFT'),
                               ('SIZE',(0,0),(-1,-1),fontsize)]))
    
        
        Story.append(t)

    
    
    mezera = ParagraphStyle('text',
                              fontName='AmorSerifRegularPro.ttf',
                              fontSize=fontsize,
                              spaceAfter = 0,
                              alignment = TA_CENTER
                              )
    p = Paragraph('',mezera)
    Story.append(p)

    #patek	
    (pole,obsah,h1) = export.patek()
    h1Obsah = ParagraphStyle('h1',
                        fontName='AmorSerifRegularProBold.ttf',
                        fontSize= fontsize,
                        spaceAfter = 0,
                        spaceBefore = 0,
                        alignment = TA_CENTER
                        )

    p = Paragraph(h1,h1Obsah)
    Story.append(p)
    
    for i in pole:
        data = [[newLine(i),str(int(obsah[i]))+kc]]
        t = Table(data, colwidths,rolheight)
        
        t.setStyle(TableStyle([('FONT',(0,0),(-1,-1),'AmorSerifRegularProBold.ttf'),
                               ('ALIGN',(0,0),(0,0),'LEFT'),
                               ('SIZE',(0,0),(-1,-1),fontsize)]))
    
        
        Story.append(t)

    
    
    mezera = ParagraphStyle('text',
                              fontName='AmorSerifRegularPro.ttf',
                              fontSize=fontsize,
                              spaceAfter = 0,
                              alignment = TA_CENTER
                              )
    p = Paragraph('',mezera)
    Story.append(p)


    #napoje	
    (pole,obsah,h1) = export.napoje()
    h1Obsah = ParagraphStyle('h1',
                        fontName='AmorSerifRegularProBold.ttf',
                        fontSize= fontsize,
                        spaceAfter = 0,
                        spaceBefore = 0,
                        alignment = TA_CENTER
                        )

    p = Paragraph(h1,h1Obsah)
    Story.append(p)
    
    for i in pole:
        data = [[newLine(i),str(int(obsah[i]))+kc]]
        t = Table(data, colwidths,rolheight)
        
        t.setStyle(TableStyle([('FONT',(0,0),(-1,-1),'AmorSerifRegularProBold.ttf'),
                               ('ALIGN',(0,0),(0,0),'LEFT'),
                               ('SIZE',(0,0),(-1,-1),fontsize)]))
    
        
        Story.append(t)

    
    '''
        Story.append(getImage(220,250))
    
    text = u'Otevírací doba:'+getDatum() 
    headtext = ParagraphStyle('text',
                              fontName='AmorSerifRegularPro.ttf',
                              fontSize = fontsize,
                              spaceAfter = 15,
                              alignment = TA_CENTER
                              )
    
    p = Paragraph(text,headtext)
    Story.append(p)


    mezera = ParagraphStyle('text',
                              fontName='AmorSerifRegularPro.ttf',
                              fontSize=fontsize,
                              spaceAfter = 170,
                              alignment = TA_CENTER
                              )
    p = Paragraph('',mezera)
    Story.append(p)
    
    text = u'PO-PÁ 10:00 - 24:00'
    p = Paragraph(text,headtext)
    Story.append(p)

    text = u'SO-NE 12:00 - 24:00'
    p = Paragraph(text,headtext)
    Story.append(p)

    text = u'TEL.: 257 322 525'
    p = Paragraph(text,headtext)
    Story.append(p)

    text = u'Email: info@uziznivehojelena.cz'
    p = Paragraph(text,headtext)
    Story.append(p)


    mezera1 = ParagraphStyle('text',
                              fontName='AmorSerifRegularPro.ttf',
                              fontSize=fontsize,
                              spaceBefore = 30,
                              spaceAfter = 15,
                              alignment = TA_CENTER
                              )
    p = Paragraph('',mezera1)
    text = u'Provozuje:'
    p = Paragraph(text,mezera1)
    Story.append(p)

    text = u'AKORÁT s.r.o.'
    p = Paragraph(text,headtext)
    Story.append(p)
     '''   
     ###  page 4   ###
    doc = SimpleDocTemplate(name(),pagesize=letter, topMargin=-20)
    doc.build(Story)


createPdf()
