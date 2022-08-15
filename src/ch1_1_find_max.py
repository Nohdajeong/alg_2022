from vis import FindMaxVisualizer as Visualizer
# from vis import Dummy as Visualizer

def find_max(array):
  max = float('-inf')
  at = -1
  for i in range(len(array)):
    vis.compare(i)
    if max < array[i]:
      max = array[i]
      at = i
      vis.update()
  vis.compare(-1)
  return max, at

if __name__ == '__main__':
  vis = Visualizer('Find Max Value')
  array = [45,20,35,60,55,10,90,85,25,75]
  vis.setup(vis.get_main_module())
  max, at = find_max(array)
  print(f'{max=}, {at=}')
  vis.end()


