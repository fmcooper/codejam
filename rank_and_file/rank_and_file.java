// codejam rank and file
// https://code.google.com/codejam/contest/4304486/dashboard#s=p1

import java.util.*;
import java.io.*;

public class rank_and_file {

	public static void main(String[] args) {
		Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
		int t = in.nextInt();
		for (int i = 1; i <= t; ++i) {
			int n = in.nextInt();
			int numRows = 2 * n - 1;
			int[] flattened = new int[numRows * n];
			for (int j = 0; j < numRows; j++) {
				for (int k = 0; k < n; k++) {
					flattened[j * n + k] = in.nextInt();
				}
			}
			String solution = getMissingRow(flattened);
			System.out.println("Case #" + i + ": " + solution);
		}
	}

	// Idea is to find out which integers in the 2D array occur an odd number of times.
	// These integers will form the missing row and will occur in sorted order.
	public static String getMissingRow(int[] flattened) {
		// Sort the flattened 2D array.
		Arrays.sort(flattened);

		// Create an ArrayList to hold the missing row.
		ArrayList<Integer> missing = new ArrayList<Integer>();

		// Iterate over the sorted flattened array.
		int numSeen = 1;
		int current = flattened[0];
		for (int i = 1; i < flattened.length; i++) {
			// If we have already seen this integer then add to the count.
			if (flattened[i] == current) {
				numSeen++;
			}
			// If we have not seen this integer then check if the previous integer 
			// was seen an odd number of times.
			else if (numSeen % 2 == 1) {
				missing.add(current);
				current = flattened[i];
				numSeen = 1;
			}
			// Otherwise reset the variables.
			else {
				current = flattened[i];
				numSeen = 1;
			}
			// Need to check if the final integer should be added.
			if (i == flattened.length - 1 && numSeen % 2 == 1) {
				missing.add(current);
			}
		}

		// Output.
		String missingRow = "";
		for (int m : missing) {
			missingRow += m + " ";
		}
		return missingRow;
	}
}
