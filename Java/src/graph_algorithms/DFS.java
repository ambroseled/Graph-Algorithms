package graph_algorithms;

import java.util.Arrays;

public class DFS {
	
	public DFS(int[][] adj_list, int start) {
		int nVert = adj_list.length;
		int[] parentArray = new int[nVert];
		Arrays.fill(parentArray, (Integer) null);
		String[] states = new String[nVert];
		Arrays.fill(states, "Undiscovered");
		states[start] = "Discovered";
		dfsLoop(adj_list, start, states, parentArray);
		
	}
	
	
	public int[] dfsLoop(int[][] adj_list, int start, String[] states, int[] parentArray) {
		
		return parentArray;
	}
	public static void main(String[] args) {
		DFS dfs = new DFS([[(1, null), (2, null)], [(0, null), (2, null)], [(0, null), (1, null)]], );

	}

}


