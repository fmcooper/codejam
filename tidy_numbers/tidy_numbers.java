// codejam tidy numbers
// https://code.google.com/codejam/contest/3264486/dashboard#s=p1

import java.util.*;
import java.io.*;

public class tidy_numbers {

	public static void main(String[] args) {
		Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
		int t = in.nextInt();
		for (int i = 1; i <= t; ++i) {
			String n = in.next();
			long solution = getLargestTidy(n);
			System.out.println("Case #" + i + ": " + solution);
		}
	}

	/**
	* Returns the largest tidy number smaller than the given number.
	*/
	public static long getLargestTidy(String num) {
		char firstProbDigit = '.';
		int firstProbPosition = -1;

		// Calculate the first problem digit and position.
		for (int i = 0; i < num.length() - 1; i++) {
			char lDigit = num.charAt(i);
			char rDigit = num.charAt(i + 1);
			if (lDigit > rDigit) {
				firstProbDigit = lDigit;
				firstProbPosition = i;
				break;
			}
		}

		// If there is not problem digit then return the number as it is.
		if (firstProbPosition == -1) {
			return Long.parseLong(num);
		}

		String newNum = "";

		// If the problem is at index 0, then we minus 1 from the first digit and
		// set the rest of the digits equal to 9.
		if (firstProbPosition == 0) {
			int newFirst = Integer.parseInt("" + firstProbDigit) - 1;
			newNum = "" + newFirst;
			// System.out.print("newNum: " + newNum);
			for (int i = 0; i < num.length() - 1; i++) {
				newNum = newNum + "9";
				// System.out.print("newNum: " + newNum);
			}
			return Long.parseLong(newNum);
		}

		// Otherwise, let our return number be equal to the old number up until we 
		// reach the same digit as the problem. Then, set the rest of the digits equal to 0.
		// Convert to a long and -1 from it.
		boolean found = false;
		for (int i = 0; i < num.length(); i++) {
			if (!found) {
				if (num.charAt(i) == firstProbDigit) {
					found = true;
				}
				newNum = newNum + num.charAt(i);
			}
			else {
				newNum = newNum + "0";
			}
		}
		long newNumLong = Long.parseLong(newNum);
		newNumLong--;
		return newNumLong;
	}
}
