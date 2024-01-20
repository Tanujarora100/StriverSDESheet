package Graph;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

// Represents a node in the graph
class Node {
    public int val; // Value of the node
    public List<Node> neighbors; // List of neighbors of the node

    // Default constructor
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }

    // Constructor with value
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }

    // Constructor with value and neighbors
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}

// Class for cloning a graph
public class CloneGraph {
    // HashMap to store the mapping of original nodes to cloned nodes
    HashMap<Node, Node> map = new HashMap<>();

    // Clone the given graph starting from the given node
    public Node cloneGraph(Node node) {
        // If the given node is null, return null
        if (node == null)
            return null;
        // Otherwise, perform depth-first search to clone the graph and return the
        // cloned node
        return dfs(node);
    }

    // Depth-first search to clone the graph
    public Node dfs(Node node) {
        // If the mapping for the node already exists, return the cloned node
        if (map.containsKey(node))
            return map.get(node);
        //DFS hai to same nodes aa sakte hain baar baar toh bhai kuch nahi karna baar baar thodi banayegey
        //check karlo ki agar pehle hi node banaya hua hai ki nahi.
        // Create a new cloned node with the value of the original node
        Node clone = new Node(node.val);
        // Store the mapping of original node to cloned node
        map.put(node, clone);
        // Recursively clone the neighbors of the original node and add them to the
        // cloned node
        for (Node it : node.neighbors) {
            clone.neighbors.add(dfs(it));
        }
        return clone; // Return the cloned node
    }
}