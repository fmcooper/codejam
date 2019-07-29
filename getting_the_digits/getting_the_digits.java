// codejam getting the digits
// https://code.google.com/codejam/contest/11254486/dashboard

import java.util.*;
import java.io.*;

public class getting_the_digits {

	public static void main(String[] args) {
		Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
		int t = in.nextInt();
		for (int i = 1; i <= t; ++i) {
			String s = in.next();
			String solution = getNumber(s);
			System.out.println("Case #" + i + ": " + solution);
		}
	}

	public static String getNumber(String s) {
		char[] sequence = s.toCharArray();
		int letterCount = sequence.length;

		// Create a counts array which has the total number of these letters in the sequence.
		int[] counts = new int[26];
		for (char letter : sequence) {
			int index = letter - 'A';
			counts[index]++;
		}

		// Stores the digits of the phone number.
		ArrayList<Integer> phoneNumber = new ArrayList<Integer>();

		// Go over the counts array removing numbers.
		while (letterCount > 0) {
			if (counts['Z' - 'A'] > 0) {
				removeWord("ZERO", counts);
				phoneNumber.add(0);
				letterCount -= 4;
			}
			else if (counts['W' - 'A'] > 0) {
				removeWord("TWO", counts);
				phoneNumber.add(2);
				letterCount -= 3;
			}
			else if (counts['X' - 'A'] > 0) {
				removeWord("SIX", counts);
				phoneNumber.add(6);
				letterCount -= 3;
			}
			else if (counts['G' - 'A'] > 0) {
				removeWord("EIGHT", counts);
				phoneNumber.add(8);
				letterCount -= 5;
			}
			else if (counts['U' - 'A'] > 0) {
				removeWord("FOUR", counts);
				phoneNumber.add(4);
				letterCount -= 4;
			}
			else if (counts['F' - 'A'] > 0) {
				removeWord("FIVE", counts);
				phoneNumber.add(5);
				letterCount -= 4;
			}
			else if (counts['V' - 'A'] > 0) {
				removeWord("SEVEN", counts);
				phoneNumber.add(7);
				letterCount -= 5;
			}
			else if (counts['R' - 'A'] > 0) {
				removeWord("THREE", counts);
				phoneNumber.add(3);
				letterCount -= 5;
			}
			else if (counts['O' - 'A'] > 0) {
				removeWord("ONE", counts);
				phoneNumber.add(1);
				letterCount -= 3;
			}
			else if (counts['N' - 'A'] > 0) {
				removeWord("NINE", counts);
				phoneNumber.add(9);
				letterCount -= 4;
			}
		}

		// Output.
		Collections.sort(phoneNumber);
		String phoneString = "";
		for (int n : phoneNumber) {
			phoneString += "" + n;
		}
		return phoneString;
	}

	// removes a word from the counts array
	public static void removeWord(String word, int[] counts) {
		char[] wordChars = word.toCharArray();
		for (char c : wordChars) {
			counts[c - 'A']--;
		}
	}
}
