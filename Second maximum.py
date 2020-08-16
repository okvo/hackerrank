#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr = set(arr)
    arr.remove(max(arr))
    print max(arr)