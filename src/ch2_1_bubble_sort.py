# from data_unsorted import numbers
from data_unsorted_a_lot import numbers
from random import randint, seed, shuffle
# from vis import BubbleSortVisualizer as Visualizer
# from vis import Dummy as Visualizer
from time import time

def main():
  # print('before:', array)
  count = len(array)
  end = count - 1
  while end > 0:
    last = 1
    for i in range(end):
      # vis.compare(i, i+1)
      if array[i] > array[i+1]:
        # vis.swap(i, i+1)
        array[i], array[i+1] = array[i+1], array[i]
        last = i + 1
    end = last - 1
    # vis.bubble_end(last)
  # vis.bubble_end(0)
  # print('after :', array)

''' 
count=100 elapsed=0.004
count=1000 elapsed=0.371
count=2000 elapsed=1.561
count=3000 elapsed=3.605
count=4000 elapsed=6.513
count=5000 elapsed=10.418
count=6000 elapsed=15.051
count=7000 elapsed=20.162
count=8000 elapsed=26.186
count=9000 elapsed=33.602
count=10000 elapsed=41.471

shuffle() 적용했을 때
count=100 elapsed=0.005
count=1000 elapsed=0.460
count=2000 elapsed=1.839
count=3000 elapsed=4.089
count=4000 elapsed=7.317
count=5000 elapsed=11.578
count=6000 elapsed=16.275
count=7000 elapsed=22.503
count=8000 elapsed=29.176
count=9000 elapsed=37.714
count=10000 elapsed=45.830

Dummy vis 를 뺐을 때
count=100 elapsed=0.000
count=1000 elapsed=0.095
count=2000 elapsed=0.381
count=3000 elapsed=0.863
count=4000 elapsed=1.510
count=5000 elapsed=2.337
count=6000 elapsed=3.296
count=7000 elapsed=4.812
count=8000 elapsed=6.369
count=9000 elapsed=7.827
count=10000 elapsed=9.684
count=15000 elapsed=22.029
count=20000 elapsed=39.720
'''

if __name__ == '__main__':
  seed('Hello') # 'Hello' 를 seed 로 고정하여 randint 가 항상 같은 결과가 나오게 한다
  # vis = Visualizer('Bubble Sort')

  counts = [ 100, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 15000, 20000 ]
  for count in counts:
    array = numbers[:count]
    shuffle(array)
    startedOn = time()
    main()
    elapsed = time() - startedOn
    print(f'{count=} {elapsed=:.3f}')

  exit() 

  while True:
    count = randint(10, 30)
    array = numbers[:count]
    vis.setup(vis.get_main_module())
    main()
    vis.draw()

    again = vis.end()
    if not again: break
