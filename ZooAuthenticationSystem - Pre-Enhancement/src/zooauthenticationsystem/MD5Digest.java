/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package zooauthenticationsystem;

/**
 *
 * @author Robert
 */
import java.security.MessageDigest;

public class MD5Digest {

     public static String md5HashCode(String input) {
        StringBuffer sb = new StringBuffer();
        MessageDigest md;

        try {
            md = MessageDigest.getInstance("MD5");
            md.update(input.getBytes());
            byte[] digest = md.digest();
            
            for (byte b : digest) {
                sb.append(String.format("%02x", b & 0xff));
            }            
        }

        catch (Exception e) {
            e.printStackTrace();
        }

        return sb.toString();                                

    }

}
    

