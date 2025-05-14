# Java String 的常见操作

## 常用 constructor

## 常用 method
### 1. isEmpty()
```java
public boolean isEmpty()
```
* Returns true if, and only if, length() is 0.

### 2. substring()
```java
public String substring(int beginIndex)
```
* Returns a string that is a substring of this string. The substring begins with the character at the specified index and extends to the end of this string.

```java
public String substring(int beginIndex, int endIndex)
```
* Returns a string that is a substring of this string. The substring begins at the specified `beginIndex` and extends to the character at index `endIndex - 1`. Thus the length of the substring is `endIndex-beginIndex`.

### 3. StringUtils.isEmpty(CharSequence cs)
```java
static boolean isEmpty(CharSequence cs)
```
* Checks if a CharSequence is empty ("") or null.


## Reference
* https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html
* https://commons.apache.org/proper/commons-lang/apidocs/org/apache/commons/lang3/StringUtils.html