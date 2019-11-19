# Dajun Gu
# 11/15/2019
# CS441 HW 3

import math
import sys

def output(res, fname):
  # cor_sum = res[0] + res[1]
  print(f'{fname} {res[0]+res[1]}/{res[2]}({(res[0]+res[1])/res[2]:.2f}) {res[0]}/{res[3]}({res[0]/res[3]:.2f}) {res[1]}/{res[4]}({res[1]/res[4]:.2f})')

# Naive Bayes classifier
class naive_bayes:
  def __init__(self):
    self.F = [[]]
    self.fnum = 0
    self.N = [0, 0]
    # final result: 0:abnormal, 1: normal, 2:test sum, 3:total abnormal, 4:total normal
    self.res = [0, 0, 0, 0, 0]

  def learner(self, fname) -> None:
    f = open(fname, 'r')
    for l in f:
      # change string to list
      one = [int(x) for x in l.split(",")]
      # for every feature
      for i in range(len(one)-1):
        # if this feature
        if one[i+1] == 1:
          self.F[one[0]][i] += 1
      # if this person have or not have heart anomaly
      self.N[one[0]] += 1
    f.close()

  def classifier(self, fname) -> None:
    L = [0, 0]
    f = open(fname, 'r')
    for l in f:
      ins = [int(x) for x in l.split(',')]
      for i in range(2):
        L[i] = math.log(self.N[i] + 0.5) - math.log(self.N[0] + self.N[1] + 0.5)
        for j in range(self.fnum):
          s = self.F[i][j]
          if ins[j+1] == 0:
            s = self.N[i] - s
          L[i] = L[i] + math.log(s + 0.5) - math.log(self.N[i] + 0.5)

      # print(L)
      self.res[2] += 1
      self.res[ins[0]+3] += 1
      cor = 0 if L[0] > L[1] else 1
      if ins[0] == cor:
        self.res[cor] += 1
      # print(self.res)

  def run_bayes(self, filename):
    self.N = [0, 0]
    self.res = [0, 0, 0, 0, 0]
    f = open(filename, 'r')
    one = f.readline().split(',')
    self.F = [[0 for x in one[1:]] for x in range(2)]
    # the number of the features
    self.fnum = len(one[1:])
    f.close()

    # begin learner
    self.learner(filename)
    # test file name
    self.classifier(filename[:-9] + 'test.csv')
    output(self.res, filename[14:-10])

if __name__ == "__main__":
  if len(sys.argv) <= 1:
    print("Please input the file path.")

  b = naive_bayes()
  for each in sys.argv[1:]:
    b.run_bayes(each)