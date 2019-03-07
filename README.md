# compy
- 競技プログラミング用のコードスニペット集
- Snippets for Competitive Programming

# snipetts
- UnionFind.py
  - Union Findを行うクラス
  - parentには以下を格納
    - 小の場合（正値）は親のインデックス
    - 親の場合（負値）はその集合のサイズ
- Deque.py
  - Pythonリストはスタック利用はOKだがキューは遅い
    - たとえば`pop(0)`はO(n); 先頭要素を削除→配列を1つずつ前にズラす
  - → colletions.dequeを利用
