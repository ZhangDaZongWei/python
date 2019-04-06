# 读取文档并将其存入列表里。

from docx import Document

def readDoc(path):
  docObject = Document(path)
  paragraph_list = []
  for p in docObject.paragraphs:
    # print(p.text)
    paragraph_list.append(p.text)
  return paragraph_list
