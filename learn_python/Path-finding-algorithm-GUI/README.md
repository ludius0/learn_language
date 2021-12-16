# Path-finding-algorithm-GUI

Tkinter GUI with path finding algorithm as visual medium. You draw start node and end node (goal), after that you can draw walls and choose algorithm. Later I want to add Astar algorithm. Right now there is only button for Astar without command. Program show steps and time of computing. After computation you can draw with highlight color. If you want use algorithm again, you need press restart button.

UPDATE: I cleaned code -> I replace structure of ("color", x, y, a, b) to only (x, y) coordinates, which made code cleaner.

Algorithm is also explained within the code.

![Screenshot_1](https://user-images.githubusercontent.com/57571014/80263671-a7b10e80-8691-11ea-8398-80e68fe6d12f.png)
![Screenshot_2](https://user-images.githubusercontent.com/57571014/80263680-af70b300-8691-11ea-8044-cf1a69601e18.png)




BTW: I tried this before without any knowledge how path finding algorihms works, I just made one similiar to breath first search, when I made bucket function for my pixel painter. Program actually worked, despite its size, which was excessively huge, but I didn't know how to properly track steps (path).
