
def solution(N):
    # write your code in Python 3.6
  return len(max(bin(N)[2:].strip('0').strip('1').split('1')))
