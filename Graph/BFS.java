package Graph;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class BFS {
    public ArrayList<Integer> bfsOfGraph(int V, ArrayList<ArrayList<Integer>> adj) {
        // Code here
        ArrayList<Integer> bfs = new ArrayList<>();
        boolean visited[] = new boolean[adj.size()];
        Queue<Integer> q = new LinkedList<>();
        q.add(0);
        visited[0] = true;
        while (!q.isEmpty()) {
            Integer Node = q.poll();
            bfs.add(Node);
            for (Integer it : adj.get(Node)) {
                if (!visited[it]) {
                    visited[it] = true;
                    q.add(it);
                }
            }
        }
        return bfs;
    }
}
