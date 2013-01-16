#encoding:utf-8

#このプログラムの説明------
#複数のファイルで共通する単語を取り出し、出現頻度順にソートする。また、ファイルごとにおけるその単語のランキングも添える
#--------------

import sys
from word_check_all import word_detecting

#もととなるファイルのfile_idは0
#もとのファイルはsys.readlineで読み込む
#ファイル数(つまり、このプログラムでは2つ以上)
file_number=2
#ファイル名を格納するリスト
file_name=[]
file_name.append("default")
#2つ目以降のファイルはargvで読み込む
#file_name[1]が始めて読み込むファイル(2番目のファイル)
for num in range(1,file_number):
  file_name.append(sys.argv[num])

#単語を格納するリスト
word_lst=[]
#単語とランキングを対応させるもの
word_rank={}
#単語と割合を対応させるもの
word_ratio={}

while(True):
#for line in range(0,lowest_rank):
  line=sys.stdin.readline().strip()
  if line=="":
    break
  line=line.split(" ")
  rank=line[0]
  ratio=float(line[1])
  word=line[2]
  word_ratio[word]=ratio
  #単語のランキングは単語ごとにファイル番号:ランキングという辞書を持たせる
  word_rank[word]={}
  #今後word_rank[word]に各ファイルのランクが入る
  word_rank[word][0]=rank
  word_lst.append(word)
  
#単語が存在するかをチェックする
#0番は元となるファイル
for i in range(1,file_number):
  #iはファイルの番号
  file_id=i
  word_detecting(word_rank,word_ratio,word_lst,file_name[i],file_id)

#ランキング,割合,単語を出力する
for word,ratio in sorted(word_ratio.items(),key=lambda x:x[1],reverse=True):
  print ratio,word,
  for file_id in range(0,file_number):
    print word_rank[word][file_id],
  print ""
