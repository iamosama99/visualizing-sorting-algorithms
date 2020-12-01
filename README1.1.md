# visualizing-sorting-algorithms
i used pygame to visualize some popular comparison based algorithms.

i did not created GUI as i just wanted to see how they works.

Explanation of main function: 

~binary_insertion_sort_not_visualized(bars, 0 , no_of_bars-1)

~reverse(bars, 0 , no_of_bars-1)

These two functions are not visualized

~bars.sort(reverse=True)

~bars.sort()

These two functions are inbuilt python function.

The main purpose of using/creating these function was to check performance and behaviour of sorting algorithms in already sorted/reversed or partially sorted/reversed array.

The rest commented funtions are visualized sorting algorithms using pygame library. Just uncomment the function of which algorithm you want to see.

Explanation of Visualization : 

WIDTH = 1800

HEIGHT = 920

Initialize these according to your screen resolution.

i have used bars and sorted them in ascending order. 

BAR_HEIGHT_RANGE = (20,900)   

no_of_bars = 200  (should be less than [WIDTH/2] because we wont be able to create bars with width less than 1 px)

Initialize these according to what you want to see.

In visualization bars can have upto 4 diffeent colors. They all signify different meaning :

Blue color : When Bar is Being traversed or compared.

Red color : It represents swap operation. (Red because its most expensive operation here)

Green color : When bar is sorted. (not all algorithms sorts elements sequentially. So its helpful in Visualizing algorithms like Quick Sort)



  
 

