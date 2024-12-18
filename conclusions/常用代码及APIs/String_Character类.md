# String

## `java.lang.String`
* https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html

### 常用 methods
* `char     charAt(int index)                   Returns the char value at the specified index.`
* `int 	    compareTo(String anotherString) 	Compares two strings lexicographically.`
* `int 	    compareToIgnoreCase(String str) 	Compares two strings lexicographically, ignoring case differences.`
* `boolean 	equalsIgnoreCase(String anotherString)  Compares this String to another String, ignoring case considerations.`
* `String 	concat(String str) 	                Concatenates the specified string to the end of this string.`
* `boolean 	contains(CharSequence s) 		    Returns true if and only if this string contains the specified sequence of char values.`
* `int 	indexOf(String str)                     Returns the index within this string of the first occurrence of the specified substring.`
* `int 	indexOf(String str, int fromIndex) 	    Returns the index within this string of the first occurrence of the specified substring, starting at the specified index.`
* `boolean 	endsWith(String suffix) 	        Tests if this string ends with the specified suffix.`
* `boolean 	isBlank() 	                        Returns true if the string is empty or contains only white space codepoints, otherwise false.`
* `boolean 	isEmpty() 	                        Returns true if, and only if, length() is 0.`
* `int 	lastIndexOf(String str) 	            Returns the index within this string of the last occurrence of the specified substring.`
* `int 	lastIndexOf(String str, int fromIndex)  Returns the index within this string of the last occurrence of the specified substring, searching backward starting at the specified index.`

### `public String[] split(String regex, int limit)`
* `split()` 方法根据匹配给定的正则表达式来拆分字符串。
* 注意： `* ^ .  $ | \` 这六个转义字符，必须得加 `\\`。
* 注意：多个分隔符，可以用 | 作为连字符。

**Reference:**
* [Java split() 方法](https://www.runoob.com/java/java-string-split.html)


## `java.lang.Character`
* https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Character.html

### 常用 methods
* `static int		compare(char x, char y)     			Compares two char values numerically.`
* `int				compareTo(Character anotherCharacter)  	Compares two Character objects numerically.`
* `static boolean	isAlphabetic(int codePoint) 			Determines if the specified character (Unicode code point) is an alphabet.`
* `static boolean	isDigit(char ch)  						Determines if the specified character is a digit.`
* `static boolean	isLetter(char ch)  						Determines if the specified character is a letter.`
* `static boolean	isLetterOrDigit(char ch)  				Determines if the specified character is a letter or digit.`
* `static boolean	isLowerCase(char ch)  					Determines if the specified character is a lowercase character.`
* `static boolean	isUpperCase(char ch)  					Determines if the specified character is an uppercase character.`
* `static char		toLowerCase(char ch)  					Converts the character argument to lowercase using case mapping information from the UnicodeData file.`
* `static char		toUpperCase(char ch)  					Converts the character argument to uppercase using case mapping information from the UnicodeData file.`