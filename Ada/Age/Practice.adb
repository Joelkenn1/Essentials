with Ada.Text_IO; use Ada.Text_IO;
with Ada.Strings; use Ada.Strings;
with Ada.Integer_Text_IO; use Ada.Integer_Text_IO;
with age;


procedure Practice is 

    -- nested procedure
    procedure Summary is
    begin
        Put_Line("This file will be used for practicing/learning code in Ada.");
        Put_Line(" ");

        Put_Line("Is this your first time coding in Ada? (Yes or No)");

        declare
            answer : string := Ada.Text_IO.Get_Line;
        
        begin

        Put_Line(if answer = "No" then "Time to get some more practice."
        elsif answer = "no" then "Time to get some more practice." 
        elsif answer = "Yes" then "It's never too late too late to start learning."
        elsif answer = "yes" then "It's never too late too late to start learning."
        else "Cool, happy coding!");
        Put_Line(" ");

        end;

    end Summary;
    
    x : Integer := -1;
    
    N : Natural;

    sum : Integer := 0;
        
begin 

    -- call to nested program
    Summary;

    -- Age Program
    begin
    Put_Line("What does your age mean?");
    Put_Line(" ");
    Put_Line("Enter your age:");


    N := Integer'Value(Ada.Text_IO.Get_Line);

    if N < 0 then
        loop exit when N >= 0;
            Put_Line("Enter a valid age:");
            N := Integer'Value(Ada.Text_IO.Get_Line);
            Put_Line(age(N));
        end loop;
    else 
        Put_Line(age(N));

    end if;
    
    exception
         when Constraint_Error =>
            Put_Line("Make sure your only inputing numerical values:");
            N := Integer'Value(Ada.Text_IO.Get_Line);
            if N < 0 then
                loop exit when N >= 0;
                    Put_Line("Enter a valid age:");
                    N := Integer'Value(Ada.Text_IO.Get_Line);
                    Put_Line(age(N));
                end loop;
             else 
                Put_Line(age(N));

            end if;
    
    end;
    Put_Line(" ");

    -- Christmas Program
    begin
    -- for loops
    Put_Line("Ada For Loops:");
    for i in reverse 1..5 loop
        if i = 5 then
            Put_Line(Integer'Image(i) & " golden rings!");

        elsif i = 4 then 
            Put_Line(Integer'Image(i) & " calling birds.");

        elsif i = 3 then 
            Put_Line(Integer'Image(i) & " french hens.");

        elsif i = 2 then 
            Put_Line(Integer'Image(i) & " turtle doves");

        else
            Put_Line("..and a partridge in a pear tree!");
        end if;
    end loop;

    Put_Line(" ");
    end;

    -- Sum Program
    begin
    -- bare loops
    
    Put_Line("Calculate the sum! Input one integer at a time, enter the number zero('0') in the prompt when finished. ");
    Put_Line(" ");
    loop exit when x = 0;

            Put_Line("Enter an integer to be added: ");
            x := Integer'Value(Ada.Text_IO.Get_Line);
            sum := sum + x;
    end loop;

    exception
         when Constraint_Error =>
            Put_Line("Make sure your only inputing numerical values:");
            loop exit when x = 0;

            Put_Line("Enter an integer to be added: ");
            x := Integer'Value(Ada.Text_IO.Get_Line);
            sum := sum + x;

            end loop;


    end;
    Put_Line("The sum of the numbers you entered is " & Integer'Image(sum));

    

end Practice;
