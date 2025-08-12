
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        
        
        bool done = false;
        while (done == false){
        
            Console.WriteLine("what would you like to do: ");
            string intention = Console.ReadLine();
            
            
            
            
            if (intention == "calc"){
           	 Console.Write("First number: ");
         	   int num1 = Convert.ToInt32(Console.ReadLine());
           	 Console.Write("Second number: ");
        	    int num2 = Convert.ToInt32(Console.ReadLine());
         	   Console.Write("sign: ");
        	    string sign = Console.ReadLine();
          	  if (sign == "+"){
                   Console.WriteLine(num1 + num2);
        	    }
        
        	    if (sign == "-"){
        	      Console.WriteLine(num1 - num2);
        	    }
         
        	    if (sign == "/"){
      	        Console.WriteLine(num1 / num2);
      	      }
        
      	      if (sign == "*"){
    	          Console.WriteLine(num1 * num2);
  	          }
    	    }
            
            
            
            
            
            
            if (intention == "my info"){
               Console.Write("Name: ");
               string name = Console.ReadLine();
               Console.WriteLine(name + " ...");
               if (name == "nkosiyapha"){
                   Console.Write("Surname: ");
                   string surname = Console.ReadLine();
                   Console.WriteLine(surname + name);
               } else {
                   Console.WriteLine("loser");
               }
            }
            
            
            
            
            
            
            
            if (intention == "list"){
              List<string> list = new List<string>();
              Console.Write("what do you want to add: ");
         	 string tolist = Console.ReadLine();
              list.Add(tolist);
              Console.WriteLine(list);
            }
            
            
            
            
            
            if (intention == "done"){
  	         done = true;
 	       } 
            
            int i = 30;
            
            if (done == true){
               Console.WriteLine("Beginning termination procedure ...");
               while ( i > 0){
                   Console.WriteLine(i);
                   i--;
               }
               Console.WriteLine("Program Terminated ... Goodbye");
            }
            
            
            
        }  
    }
}



        
