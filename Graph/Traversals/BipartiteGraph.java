package Graph.Traversals;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class BipartiteGraph {

    public boolean isBipartite(int[][] graph) {
        // zero based indexed graph
        // no self edges are there
        // adjacency List is given already
        // graph is not connected
        int n = graph.length;
        Queue<Integer> q = new LinkedList<>();
        int[] colorArray = new int[graph.length];
        Arrays.fill(colorArray, -1);
        for (int i = 0; i < n; i++) {
            if (colorArray[i] == -1) {
                q.offer(i);
                colorArray[i] = 0;
                // push it to the queue and mark it as visited.
                while (!q.isEmpty()) {
                    int currNode = q.poll();

                    // check all its neighbours
                    for (int neighbour : graph[currNode]) {
                        if (colorArray[neighbour] == colorArray[currNode])
                            // if the neighbour has same color as the current node then return false.
                            return false;
                        // if the neighbour is not visited
                        else if (colorArray[neighbour] == -1) {
                            colorArray[neighbour] = 1 - colorArray[currNode];
                            // push it to the queue and mark it as visited.
                            q.offer(neighbour);
                        }
                    }
                }
            }
        }
        return true;

    }
}
