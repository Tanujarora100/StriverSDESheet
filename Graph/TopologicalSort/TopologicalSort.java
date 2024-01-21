package Graph;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class TopologicalSort {
    static int[] topoSort(int V, ArrayList<ArrayList<Integer>> adj) {
        // Store the indegree of each node
        int indegree[] = new int[V];

        // Calculate the indegree of each node
        for (int i = 0; i < V; i++) {
            for (int it : adj.get(i)) {
                indegree[it]++;
            }
        }

        // Initialize a queue to perform topological sorting
        Queue<Integer> q = new LinkedList<Integer>();

        // Add nodes with indegree 0 to the queue
        for (int i = 0; i < V; i++) {
            if (indegree[i] == 0) {
                q.add(i);
            }
        }

        // Initialize an array to store the topological ordering
        int topo[] = new int[V];
        int i = 0;

        // Perform topological sorting
        while (!q.isEmpty()) {
            int node = q.peek();
            q.remove();
            topo[i++] = node;

            // Update the indegree of adjacent nodes and add them to the queue if their
            // indegree becomes 0
            for (int it : adj.get(node)) {
                indegree[it]--;
                if (indegree[it] == 0) {
                    q.add(it);
                }
            }
        }

        // Return the topological ordering
        return topo;
    }
}
