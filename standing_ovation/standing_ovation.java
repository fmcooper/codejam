// codejam standing ovation
// 

import java.util.*;
import java.io.*;

public class standing_ovation {

	public static void main(String[] args) {
		Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
		int t = in.nextInt();
		for (int i = 1; i <= t; ++i) {
			in.next(); // Don't need the max shyness in this solution.
			String s = in.next();
			int solution = getNumExtraAudience(s);
			System.out.println("Case #" + i + ": " + solution);
		}
	}

	public static int getNumExtraAudience(String s) {
		int runningTotal = 0;
		int numExtraRequired = 0;

		// Iterate over the string of numbers keeping track of how many people we need to add.
		for (int i = 0; i < s.length(); i++) {
			int currentDigit = Integer.parseInt("" + s.charAt(i));
			int numRequiredForStandUp = i + 1;
			runningTotal += currentDigit;

			// If the running total of people is too low, add extra people.
			if (runningTotal < numRequiredForStandUp) {
				numExtraRequired += (numRequiredForStandUp - runningTotal);
				runningTotal = numRequiredForStandUp;
			}
		}
		return numExtraRequired;
	}
}
