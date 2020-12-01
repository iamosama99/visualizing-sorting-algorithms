# -*- coding: utf-8 -*-
"""
Created on Wed May  6 14:56:48 2020

@author: Osama
"""

import pygame
import random

WIDTH = 1800
HEIGHT = 920
BAR_HEIGHT_RANGE = (20,900)
no_of_bars = 200  #(should be less than [WIDTH/2] )
bars = []
BAR_WIDTH = (WIDTH - (1 + no_of_bars )) / no_of_bars 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
swaps = 0


surface = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class bar():
    
    def __init__(self, height):
        self.width = BAR_WIDTH
        self.height = height
        self.color = BLACK
    
    def __lt__(self,other):
        return (self.height < other.height)
    
    def __le__(self,other):
        return (self.height <= other.height)
    
    def __gt__(self,other):
        return (self.height > other.height)
    
    def __ge__(self,other):
        return (self.height >= other.height)
    
      
def draw_environment(bars):
    pygame.time.delay(20)
    surface.fill(WHITE)
    bar_position = -BAR_WIDTH 
    for bar in  bars:
        bar_position += BAR_WIDTH + 1    
        pygame.draw.rect(surface, bar.color, (bar_position, HEIGHT - bar.height, bar.width, bar.height),0)
    pygame.display.update()
   
def swap(bars, i, j):
    bars[i], bars[j] = bars[j], bars[i]

def check_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit
  
def reverse(arr, start, end):
    while start < end:
        arr[start].color = arr[end].color = RED
        swap(arr, start, end)
        draw_environment(arr)
        arr[start].color = arr[end].color = BLACK
        start += 1
        end -= 1
        
def bubble_sort(bars): 
    n = len(bars) 
    for i in range(n-1): 
        for j in range(0, n-i-1):
            bars[j].color = bars[j + 1].color = BLUE
            if bars[j].height > bars[j+1].height : 
                swap(bars, j, j+1)
                bars[j + 1].color = bars[j].color = RED
            draw_environment(bars)
            bars[j].color = bars[j + 1].color = BLACK
            check_quit()
        bars[n-i-1].color = GREEN
            
def insertion_sort(bars, left, right):
    for i in range(left, right): 
        key = bars[i] 
        j = i-1
        while j >= 0 and key < bars[j] : 
            bars[j].color = BLUE
            bars[j+1] = bars[j]
            j -= 1
            draw_environment(bars)
            check_quit() 
            bars[j].color = BLACK
        bars[j + 1] = key
        bars[i].color = bars[j + 1].color = RED
        draw_environment(bars)
        check_quit()
        temp = j
        while temp >= 0:
            bars[temp].color = BLACK
            temp -= 1

def selection_sort(bars):
    for i in range(len(bars)):
        min_idx = i
        bars[i].color = BLUE
        draw_environment(bars)
        bars[i].color = BLACK
        for j in range(i+1, len(bars)): 
            if bars[min_idx] > bars[j]:
                min_idx = j
                check_quit()
            bars[min_idx].color = bars[j].color = BLUE
            draw_environment(bars)
            bars[min_idx].color = bars[j].color = BLACK             
        bars[min_idx].color = bars[i].color = RED
        swap(bars,min_idx,i)
        draw_environment(bars)
        bars[min_idx].color = BLACK
        bars[i].color = GREEN
        check_quit()         
        
def shell_sort(bars):
    n = len(bars) 
    gap = n//2
    while gap > 0: 
        for i in range(gap,n): 
            temp = bars[i]
            bars[i].color = BLUE
            j = i
            while j >= gap and bars[j-gap].height > temp.height:
                bars[j] = bars[j-gap]
                bars[j].color = bars[j-gap].color = RED
                draw_environment(bars)
                bars[j].color = bars[j-gap].color = BLACK
                j -= gap
            bars[j] = temp
            bars[i].color = bars[j].color = BLUE
            draw_environment(bars)
            bars[i].color = bars[j].color = BLACK
            check_quit()  
        gap //= 2
        draw_environment(bars) 
        check_quit()
    
def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
  
    L = [0] * (n1) 
    R = [0] * (n2) 
  
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
   
    i = 0    
    j = 0     
    k = l     
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]:
            arr[k] = L[i]
            if k == l+i:
                arr[k].color = arr[l+i].color = BLUE
            else:
                arr[k].color = arr[l+i].color = RED
            draw_environment(bars)
            arr[k].color = arr[l+i].color = BLACK
            i += 1
        else:
            arr[k] = R[j]
            if k == m+j:
                arr[k].color = arr[m+j+1].color = BLUE
            else:
                arr[k].color = arr[m+j+1].color = RED
            draw_environment(bars)
            arr[k].color = arr[m+j+1].color = BLACK
            j += 1
        k += 1
        check_quit() 
        
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
        draw_environment(bars) 
        check_quit()   

    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
        draw_environment(bars) 
        check_quit()   

def merge_sort(arr,l,r): 
    if l < r: 
        m = (l+(r-1))//2
        merge_sort(arr, l, m) 
        merge_sort(arr, m+1, r) 
        merge(arr, l, m, r) 

def sorted_(bars):
    for i in range(0, len(bars)):
        bars[i].color = GREEN
        draw_environment(bars)            

def partition(arr,low,high): 
    global swaps
    i = ( low-1 )
    pivot_index = random.randrange(low, high)        
    swap(arr, pivot_index, high)
    pivot = arr[high]
    for j in range(low , high): 
        if   arr[j] < pivot: 
            i = i+1
            swap(arr, i, j); swaps += 1
            arr[i].color = arr[j].color = BLUE
            draw_environment(bars)
            arr[i].color = arr[j].color = BLACK
        check_quit()
    swap(arr, i+1, high); swaps += 1 
    arr[i+1].color = arr[high].color = RED
    draw_environment(bars)
    arr[i+1].color = arr[high].color = BLACK
    check_quit()
    return ( i+1 ) 
  
def hoare_partition(arr, low, high):
    global swaps
    i = low 
    j = high + 1 
    pivot_index = random.randrange(low, high)      
    swap(arr, pivot_index, low)
    pivot = arr[low]

    while i < j:
        while True:
            i += 1
            if not ( i < j and arr[i] < pivot ):
                break
            arr[i].color = BLUE
            draw_environment(arr)
            arr[i].color = BLACK
            
        while True:
            j -= 1
            if not ( j >= i and arr[j] >= pivot ):
                break
            arr[j].color = BLUE
            draw_environment(arr)
            arr[j].color = BLACK

        if i < j:
            arr[i].color = arr[j].color = RED
            swap(arr, i, j); swaps += 1
            draw_environment(arr)
            check_quit()
            arr[i].color = arr[j].color = BLACK
    arr[low].color = arr[j].color = RED
    swap(arr, low, j); swaps += 1
    draw_environment(arr)
    arr[low].color = arr[j].color = BLACK
    check_quit()
    return j          
        
def quick_sort(arr,low,high): 
    if low < high: 
        pi = partition(arr,low,high)
        arr[pi].color = GREEN
        quick_sort(arr, low, pi-1) 
        quick_sort(arr, pi+1, high)
    else :
        arr[low].color = GREEN
        draw_environment(bars)
        return
    
def quick_sort_optimized(arr,low,high): 
    if low < high: 
        pi = hoare_partition(arr,low,high)
        arr[pi].color = GREEN
        quick_sort_optimized(arr, low, pi - 1) 
        quick_sort_optimized(arr, pi+1, high)
    elif low > -1:
        arr[low].color = GREEN
        draw_environment(bars)
        return
    
def heapify(arr, n, i): 
    largest = i  # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]:
        arr[i].color = arr[l].color = BLUE
        draw_environment(bars)
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]:
        arr[i].color = arr[r].color = BLUE
        draw_environment(bars)
        largest = r
        
    if r < n:
        arr[i].color = arr[r].color = BLACK
    if l < n:
        arr[i].color = arr[l].color = BLACK
        
    # Change root, if needed 
    if largest != i: 
        swap(arr, i, largest)  # swap
        arr[i].color = arr[largest].color = RED
        draw_environment(bars)
        check_quit()
        arr[i].color = arr[largest].color = BLACK
        # Heapify the root. 
        heapify(arr, n, largest) 
  
def heap_sort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        swap(arr, i, 0)   # swap
        arr[i].color = GREEN
        draw_environment(bars)
        heapify(arr, i, 0) 
    arr[0].color = GREEN

def bogo_sort(arr): 
    while (is_sorted(arr)== False): 
        shuffle(arr)
        check_quit()
    sorted_(arr)
  
def is_sorted(arr): 
    n = len(arr) 
    for i in range(0, n-1): 
        if (arr[i] > arr[i+1] ):
            arr[i].color = arr[i+1].color = BLUE
            draw_environment(arr)
            check_quit()
            arr[i].color = arr[i+1].color = BLACK
            return False
    return True
  
def shuffle(arr): 
    n = len(arr) 
    for i in range (0,n): 
        r = random.randint(i,n-1)
        arr[i].color = arr[r].color = RED
        swap(arr, i, r)
        draw_environment(arr)
        arr[i].color = arr[r].color = BLACK

def binary_search(the_array, item, start, end):
    if start == end:
        if the_array[start] > item:
            return start
        else:
            return start + 1
    if start > end:
        return start

    mid = round((start + end)/ 2)
    the_array[mid].color = BLUE
    draw_environment(the_array)
    the_array[mid].color = BLACK
    if the_array[mid] < item:
        return binary_search(the_array, item, mid + 1, end)

    elif the_array[mid] > item:
        return binary_search(the_array, item, start, mid - 1)

    else:
        return mid

def binary_insertion_sort(the_array, start, end):
    for index in range(start, end + 1):
        value = the_array[index]
        pos = binary_search(the_array, value, start, index - 1)
        j = index - 1
        while j >= pos:
            the_array[j].color = BLUE
            the_array[j+1] = the_array[j]
            draw_environment(the_array)
            j -= 1
        the_array[pos] = value
        the_array[pos].color = RED
        draw_environment(the_array)
        check_quit()
        temp = index
        while temp >= pos:
            bars[temp].color = BLACK
            temp -= 1
    return the_array

def binary_search_not_visualized(the_array, item, start, end):
    if start == end:
        if the_array[start] > item:
            return start
        else:
            return start + 1
    if start > end:
        return start

    mid = round((start + end)/ 2)
    
    if the_array[mid] < item:
        return binary_search_not_visualized(the_array, item, mid + 1, end)

    elif the_array[mid] > item:
        return binary_search_not_visualized(the_array, item, start, mid - 1)

    else:
        return mid
    
def binary_insertion_sort_not_visualized(the_array, start, end):
    for index in range(start, end + 1):
        value = the_array[index]
        pos = binary_search_not_visualized(the_array, value, start, index - 1)
        j = index - 1
        while j >= pos:
            the_array[j+1] = the_array[j]
            j -= 1
        the_array[pos] = value
    return the_array

def merge_batch(arr, ls, le, rs, re): 
    print("merging : ",ls, le, rs, re)
    L = arr[ls : le + 1] 
    R = arr[rs : re + 1]
    
    i = 0    
    j = 0     
    k = ls     
  
    while i < len(L) and j < len(R) : 
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        arr[k].color = RED
        draw_environment(arr)
        check_quit()
        k += 1

    while i < len(L) : 
        arr[k] = L[i] 
        arr[k].color = RED
        draw_environment(arr)
        i += 1
        k += 1
       
        
    while j < len(R) :
        arr[k] = R[j]
        arr[k].color = RED
        draw_environment(arr)
        j += 1
        k += 1
        
        
def main():
    
    for i in range (no_of_bars):
        bars.append(bar(random.randrange(BAR_HEIGHT_RANGE[0], BAR_HEIGHT_RANGE[1])))
    
    #reverse(bars, 0 , no_of_bars-1)
    #bars.sort(reverse=True)
    #bars.sort()
    #bubble_sort(bars)
    #insertion_sort(bars, 0, no_of_bars )
    #selection_sort(bars)
    shell_sort(bars)
    #merge_sort(bars, 0, no_of_bars - 1)
    #quick_sort(bars, 0, no_of_bars - 1)
    #quick_sort_optimized(bars, 0, no_of_bars - 1)
    #heap_sort(bars)
    #bogo_sort(bars)
    sorted_(bars)
    print(swaps)
    draw_environment(bars) 
    while True:
        check_quit()        

if __name__ == '__main__':
    main()