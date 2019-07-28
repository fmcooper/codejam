// codejam the last word
// https://code.google.com/codejam/contest/4304486/dashboard

import java.util.*;
import java.io.*;

public class the_last_word {

	public static void main(String[] args) {
		Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
		int t = in.nextInt();
		for (int i = 1; i <= t; ++i) {
			String s = in.next();
			String solution = getLastWord(s);
			System.out.println("Case #" + i + ": " + solution);
		}
	}

	public static String getLastWord(String s) {
		// Place the first character.
		String lastWord = "" + s.charAt(0);

		// Iterate over the rest of the characters in S.
		for (int i = 1; i < s.length(); i++) {
			char firstChar = lastWord.charAt(0);
			char charToPlace = s.charAt(i);

			// If the new character is bigger than or equal to the current word's
			// first character then place at the front.
			if (charToPlace >= firstChar) {
				lastWord = charToPlace + lastWord;
			}
			// Otherwise, place at the end.
			else {
				lastWord =  lastWord + charToPlace;
			}
		}
		return lastWord;
	}
}
