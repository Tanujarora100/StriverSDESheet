package Graph;

import java.util.ArrayList;

public class DFS {
    public void dfs(int start, ArrayList<ArrayList<Integer>> adj,
            int V, boolean visited[], ArrayList<Integer> ans) {
        visited[start] = true;
        ans.add(start);
        for (int u : adj.get(start)) {
            if (!visited[u]) {
                dfs(u, adj, V, visited, ans);
            }
        }
    }

    public ArrayList<Integer> dfsOfGraph(int V, ArrayList<ArrayList<Integer>> adj) {
        boolean visited[] = new boolean[V + 1];
        ArrayList<Integer> ans = new ArrayList<>();
        for (int i = 0; i < V; i++) {
            if (!visited[i]) {
                dfs(i, adj, V, visited, ans);
            }
        }
        return ans;
    }
}
