package zooauthenticationsystem;

/**
 *
 * @author Robert Swanke
 */
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

class userCreds {
	private static String userName = "none";
	private static String userPassword = "none";
	private static String MD5ofPassword = "none";

	// returns name of item object when called
	public static String getName() {
		return userName;
	}

	// returns price of item object when called
	public static String getPasswd() {
		return userPassword;
	}

	// returns quantity of item object when called
	public static String getMD5() {
		return MD5ofPassword;
	}

	// sets item variable for name when called
	public static void setName(String newValue) {
		userName = newValue;
	}

	// sets item variable for price when called
	public static void setPasswd(String newValue) throws NoSuchAlgorithmException{
		userPassword = newValue;
		userCreds.setMD5();
	}

	// sets item variable for quantity when called
	public static void setMD5() throws NoSuchAlgorithmException {
		MD5ofPassword = md5Hasher();
	}

	private static String md5Hasher() throws NoSuchAlgorithmException {
		// Copy and paste this section of code
		String original = getPasswd();
		MessageDigest md = MessageDigest.getInstance("MD5");
		md.update(original.getBytes());
		byte[] digest = md.digest();
		StringBuilder sb = new StringBuilder();
		for (byte b : digest) {
			sb.append(String.format("%02x", b & 0xff));
		}
		// System.out.println("original:" + original);
		// System.out.println("digested:" + sb.toString()); //sb.toString() is
		return sb.toString();
	}
}
