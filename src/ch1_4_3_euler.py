
def start():
  pass

if __name__ == '__main__':
    adj_list = [
      [1, 9], [0, 2], [1, 3, 10, 11], [2, 12], [5, 11], [4, 6], [5, 11], 
      [8, 12], [7, 9, 10, 11], [8, 0], [2, 8], [2, 8, 4, 6], [3, 7]
    ]
    # 인접점 표기 방식으로 그래프를 표현한다
    # adj_list[a] 가 list 이고 그 안에 b 가 있으면 a-b 간선이 있는 것으로 본다
    start_vertex = 0
    start()
