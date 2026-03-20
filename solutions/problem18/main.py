import sys

def solve():
    list_a = list(map(int, sys.stdin.readline().split()))
    list_b = list(map(int, sys.stdin.readline().split()))
    
    merged_list = []
    ptr_a, ptr_b = 0, 0
    
    while ptr_a < len(list_a) and ptr_b < len(list_b):
        if list_a[ptr_a] < list_b[ptr_b]:
            merged_list.append(list_a[ptr_a])
            ptr_a += 1
        else:
            merged_list.append(list_b[ptr_b])
            ptr_b += 1
    
    merged_list.extend(list_a[ptr_a:])
    merged_list.extend(list_b[ptr_b:])
    
    print(*merged_list)

if __name__ == "__main__":
    solve()
