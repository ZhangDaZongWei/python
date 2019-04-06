import os
import json
import readDoc

# 分离文件名与扩展名
# os.path.splitext()

#可以输入sourcePath目录

def getFilePath(sourcePath):
  targetFilePath = r"../cacheFilePath/filePath.json"
  fileList = []
  handleDirFile(sourcePath,fileList)
  with open(targetFilePath,'w') as write_file_json:
    json.dump(fileList,write_file_json)
    print("提取路径已经完成 !")
  return targetFilePath


def handleDirFile(fileDir,fileList):
  files = os.walk(fileDir)
  for dirpath,dirnames,filenames in files:
    for filename in filenames:
      absFilePath = os.path.abspath(os.path.join(dirpath,filename))
      fileList.append(absFilePath)
