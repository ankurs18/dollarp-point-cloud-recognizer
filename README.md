# $P Point-Cloud Gesture Recognizer

## About

The $P Point-Cloud Recognizer is a 2-D stroke-gesture recognizer designed for rapid prototyping of gesture-based user interfaces. By representing gestures as point-clouds, $P can handle both unistrokes and multistrokes equivalently, and without the combinatoric overhead of $N, as stroke number, order, and direction are all ignored. When comparing two point-clouds, $P finds a solution to the classic assignment problem between two bipartite graphs using an approximation of the Hungarian algorithm.

## Implementation

This python (python3 to be specific) implementation is created in accordance with the original paper: [https://github.com/user/repo/blob/branch/other_file.md](https://github.com/user/repo/blob/branch/other_file.md)

## How To Run

python3 pdollar.py (needs arguments as follows)

pdollar has the following commands: 
  * python3 pdollar –t <gesturefile>
      *Adds the gesture file to the list of gesture templates*
  * python3 pdollar -r 
      *Clears the templates*
  * python3 pdollar <eventstream>
       *Prints the name of gestures as they are recognized from the event stream*
  
## Input Formats
### Gestures file Format

GestureName  
BEGIN  
x,y <- List of points, a point per line
…  
x,y  
END

### Eventstream File Format

MOUSEDOWN  
x,y <- List of points, a point per line  
MOUSEUP  
RECOGNIZE <- When you see this you should output the result

### Example Run:

*python3 pdollar.py eventstream.txt*  
CROSS  
CIRCLE
