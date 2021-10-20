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
import java.util.Scanner;
import java.io.FileReader;
import java.io.*;

public class ZooAuthenticationSystem {

    //add new variables
    public static void main(String args[]) {
        Scanner userInput = null;
        String continueApp = null;
        int numAttempts = 0;
        String userName, password;
        
        boolean logout = false;

        String authFile = null;

        //login loop
        //obtain userName & password
        while (true) {
            logout = false;
            userInput = new Scanner(System.in);
            System.out.print("Enter username: ");
            userName = userInput.nextLine();
            System.out.print("Enter password: ");
            password = userInput.nextLine();
            authFile = areCreditialsValid(userName, password);

            //successful login: display role info and logout option
            if (authFile != null) {
                
                //loop until logout
                //display user role information 
                while (true) {
                    //FIXME: add display information **FIXED**
                    displayAuthorizedInformation(authFile);
                    System.out.print("Press \"Q\" to logout: ");
                    String choice = userInput.nextLine();

                        //FIXME: need to give logout option **FIXED**
                        if (choice.equalsIgnoreCase("Q")) {
                            System.out.println("\nLogging out now...");
                            numAttempts = 0;                           
                            logout = true;
                            break;
                        }
                        System.out.println();
                }
            }
            
            //unsuccessful login: 3 attempts
            //FIXME: not giving 3 attempts **FIXED**
            else {
                numAttempts++;
                
                if (numAttempts == 3) {
                    System.out.println("\nTo many unsuccessful login attempts!\nExiting the program...");
                    break;
                }

                else {
                    System.out.println("Invalid username and/or password! Please try again!");
                    System.out.println((3 - numAttempts) + " attempts remain.\n");
                }
            }
            
            //logout with exit option
            if (logout) {
                System.out.print("\nPress \"Q\" to quit application. Press any other key to login as a different user.");
                continueApp = userInput.nextLine();

                if (continueApp.equalsIgnoreCase("Q")) {
                    System.out.println("\nExiting the application...");
                    break;
                }
            }
            
            System.out.println();
        }
    }


    //connect to MD5digest class and login
    //connect to main
    public static String areCreditialsValid(String userName, String password) {

        String md5Password = MD5Digest.md5HashCode(password);
        Scanner fileReader;
        String zooAuthRecord = null;
        
        try {
            fileReader = new Scanner(new File("credentials.txt"));

            while (fileReader.hasNextLine()) {
                zooAuthRecord = fileReader.nextLine();
                String credCols[] = zooAuthRecord.split("\t");
                
                if (credCols[0].trim().equals(userName)) {
                    
                    if (credCols[1].trim().equals(md5Password)) {
                        return credCols[3];
                    }
                }
            }
            
            fileReader.close();
        }

        catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        
        return null;
    }

    
    //connect to main
    public static void displayAuthorizedInformation(String userRole) {
        Scanner authRole = null;
         
        //FIXME: if-else doesn't work for displaying role info **FIXED**
        try {
            authRole = new Scanner(new File(userRole.trim() + ".txt"));
            System.out.println();
            
            while (authRole.hasNextLine()) {
                System.out.println(authRole.nextLine());
            }

            System.out.println();
            authRole.close();
        }

        catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}

