#encoding:utf-8

#このプログラムの説明-----
#共通する単語のチェック

def word_detecting(word_rank,word_ratio,word_lst,file_name,file_id):
  #変数の定義
  file_word_lst=[]
  file_word_rank={}
  file_word_ratio={}
  del_word_lst=[]

  #比較するファイルの読み込み(ランク、割合、単語)
  for line in open(file_name):
    line=line.strip().split(" ")
    rank=line[0]
    ratio=float(line[1])
    word=line[2]
    file_word_ratio[word]=ratio
    file_word_rank[word]=rank
    file_word_lst.append(word)

  for word in word_lst:
    #file_word_lstの単語が全てword_lstにあり、もう読み込むものがなくなった場合(絶対ありえないが、念のため)
    if len(file_word_lst)==0:
      del word_ratio[word]
    for cnt,file_word in enumerate(file_word_lst):
      if word==file_word:
        #リストから削除
        file_word_lst.remove(file_word)
        #ランクを追加する
        word_rank[word][file_id]=file_word_rank[file_word]
        #割合を足す
        word_ratio[word]+=file_word_ratio[file_word]
        break
    #breakせずにループが最後までいったかどうか。行った場合は共通項ではないのでその単語を削除
    if cnt==int(len(file_word_lst))-1:
      del_word_lst.append(word)
      del word_ratio[word]

  #リストの削除
  for word in del_word_lst:
    word_lst.remove(word)
