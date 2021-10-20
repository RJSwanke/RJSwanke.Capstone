### Software Design and Engineering (IT-145: Foundation in Application Development)

[Zoo Authentication System: Pre-Enhancements](https://github.com/RJSwanke/RJSwanke.github.io/tree/main/ZooAuthenticationSystem%20-%20Pre-Enhancement)

[Zoo Authentication System: Final](https://github.com/RJSwanke/RJSwanke.github.io/tree/main/ZooAuthenticationSystem)

#### Artifact explanation:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;My artifact is based off of my final project from my IT-145: Foundation in Application Developmen course. The project is a Java program that 
implements a authentication system along with an MD5 password hashing function. I created this artifact a couple years ago initially as it was one of my first classes at SNHU. The 
artifact that is included in my portfolio is the same essential program but with minor improvements like in the structure, variables, arithmetic operations, loops and security.

#### Reason for inclusion in portfolio:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I decided to include this project in my ePortfolio because it shows my proficiency with the Java programming language. Java has been and still is one of the most commonly used object-oriented programming languages in the world. By showing my familiarity with Java it will also show that I understand things like software architecture, proper coding standards and other rules that the community follows. 

#### What the program does: 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The program opens a .txt file based on the user’s login information and then prints it out to the user. The login information contains a user type, a username, and a user password. The password and username are inputted while the type is assigned in the program based on the user’s credentials. The user’s type is passed along with the password to an MD5 conversion function to authenticate the user's login credientials.

#### Changes:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The log in code is now much simpler with a better structure. These improvements along with the addition to the security of the login help to showcase my skills in using well-founded and innovative techniques, skills, and tools that help to implement solutions that deliver while accomplishing a goal. The login now has 3 attempts that will display the correct information depending on if your log in matches that in the MD5digest. Other improvements that I did was to take out unnecessary things like import java.util.* and delete the e.printStackTrace() in the block catch (FileNotFoundException e) {    	e.printStackTrace();  	} as it was not being used. I corrected the structure so that everything is properly spaced and lined up so that it is as easy to read as possible. I also added to the comments and made sure they were visible and easy to understand while still giving a full picture. 
```


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
    //display user role information if login successful
                while (true) {
    //add display information
                    displayAuthorizedInformation(authFile);
                    System.out.print("Press \"Q\" to logout: ");
                    String choice = userInput.nextLine();

    //need to give logout option
                        if (choice.equalsIgnoreCase("Q")) {
                            System.out.println("\nLogging out now...");
                            numAttempts = 0;                           
                            logout = true;
                            break;
                        }
                        System.out.println();
                }
            }
            
    //3 attempts will give an unsuccessful login            
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
    
    //checks login against credentials
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
        }
        
        return null;
    }
```
#### What I learned: 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I learned a few things from revisiting this artifact. One of those things is how different but also how similar certain languages can be. I haven't been doing Java lately but it was very easy to pick back up and understand what is going on. I do believe my experience has helped with this but I am not sure if I had to do this a year ago I would be as successful. Things tend to be a bit more simplified in other languages but the implementation of some features can be much more confusing. Every language has it's pros and cons. Overall the code isn't that complex, so the main challenge for me came from brushing up on my Java knowledge and finding ways to implement certain functions. 
