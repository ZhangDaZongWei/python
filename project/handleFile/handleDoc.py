# from docx import Document
from docx.shared import Pt,RGBColor
from docx.enum.style import WD_STYLE_TYPE

def changeColor(p):
  for r in p.runs:
    r.font.color.rgb = RGBColor(255,0,0)
