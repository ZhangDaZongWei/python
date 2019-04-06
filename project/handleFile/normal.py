import json
import handleFile.simDif as simDif
import handleFile.readDoc as readDoc
import handleFile.handleDoc as handleDoc
# import fileList
# 无需获取路径了
# sourcePath = r"../../document"

# targetPath = fileList.getFilePath(sourcePath)
def normal():
  targetPath = r'uploads.json'

  texts = []

  count = 0

  with open(targetPath) as read_file_json:
    filePaths = json.load(read_file_json)

  for filePath in filePaths:
    # readDoc.readDoc(filePath)
    texts.append(readDoc.readDoc(filePath))

  for fixTextParagraph  in texts:
    count += 1
    j = count + 1
    for activeTextParagraph in texts[count:]:
      # 这是第count文本和第几个文本比较
      # 划线
      print("这是第 " + str(count) + " 个文本和第 " + str(j) + " 个文本进行比较")
      print("***********************************")
      j = j+1
      h = 1
      for fixText in fixTextParagraph:
        # 这是第几段同各段比较
        # 划线
        print("这是第 " + str(h) + " 段和" + "各段进行比较" )
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for activeText in activeTextParagraph:
          simDif.simDif(fixText,activeText)
        h = h + 1
  
