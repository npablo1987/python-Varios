from mmap import PAGESIZE
import os

from reportlab.platypus import (SimpleDocTemplate, Spacer,Table)
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

doc = SimpleDocTemplate("prueba.pdf", pagesize = A4)
story = []

datos = [['nombre','etnia','edad', 'Sexo', 'año N.']]

tabla = Table(data = datos,
              style = [
                      ('GRID',(0,0),(-1,-1), 0.5, colors.grey),
                      ('BOX',(0,0),(-1,-1),1,colors.black),
                      ('BACKGROUND',(0,0), (-1,0), colors.blue),
                      ]
             )
story.append(tabla)
story.append(Spacer(0,15))
doc.build(story)
os.system("prueba.pdf")