Task number 1

My first action is sort dataset. It is necessary because sorted dataset allows find
duplicates (all duplicates wll be near) and sorted data also allows go through the list from first to last record
only one time.

Bottleneck of this script is sorting of data set. I recommend develop custom sort algorithm for this one data set.

This script has computational complexity O(n * 2)
All lines will treatment two times because all lines will compare with past line.