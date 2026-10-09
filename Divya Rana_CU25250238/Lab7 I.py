import heapq

# ---------- MIN HEAP ----------
min_heap = []

heapq.heappush(min_heap, 30)
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 20)
heapq.heappush(min_heap, 5)

print("Min Heap:", min_heap)
print("Smallest element:", heapq.heappop(min_heap))

 
# ---------- MAX HEAP ----------
max_heap = []

heapq.heappush(max_heap, -30)
heapq.heappush(max_heap, -10) 
heapq.heappush(max_heap, -20)
heapq.heappush(max_heap, -5)

print("\nMax Heap:", [-x for x in max_heap]) 
+print("Largest element:", -heapq.heappop(max_heap))
   

# ---------- PRIORITY QUEUE ----------
priority_queue = []

heapq.heappush(priority_queue, (1, "Emergency"))
heapq.heappush(priority_queue, (3, "Normal"))
heapq.heappush(priority_queue, (2, "Important"))

print("\nPriority Queue:")

while priority_queue:
    priority, task = heapq.heappop(priority_queue)
    print(priority, task)


# ---------- HEAP SORT ----------
arr = [5, 2, 8, 1, 9, 3]

heap = []

for x in arr:
    heapq.heappush(heap, x)

sorted_arr = []

while heap:
    sorted_arr.append(heapq.heappop(heap))

print("\nOriginal Array:", arr)
print("Heap Sort:", sorted_arr) 