with Ada.Text_IO; use Ada.Text_IO;
with Ada.Integer_Text_IO; use Ada.Integer_Text_IO;

-- In Ada you have to implement functions in seperate "adb" files
function age (i : Integer) return string is


begin

    if i = 0 then
        -- "&" is for concat, "Integer'Image(i) " is to convert integer into string"
        return "Since you're" & Integer'Image(i)  & " years old, you're considered an infant.";

        -- "#..# is to check if an integer is in a specified range"
    elsif i in 1..3 then
        return "Since you're" & Integer'Image(i)  & " years old, you're considered a toddler.";

    elsif i in 4..12 then
        return "Since you're" & Integer'Image(i)  & " years old, you're considered a child.";

    elsif i in 13..19 then
        return "Since you're" & Integer'Image(i)  & " years old, you're considered a teenager.";

    elsif i in 20..65 then
        return "Since you're" & Integer'Image(i)  & " years old, you're considered an adult.";

    elsif i > 65 then
        return "Since you're" & Integer'Image(i)  & " years old, you're considered an elder."; 

    else 
        return " ";
    end if;


    -- Using a "case statement"

    --  case i is

    --      when 0 =>
    --          return "Since you're" & Integer'Image(i)  & " years old, you're considered an infant.";

    --      when 1..3 =>
    --          return "Since you're" & Integer'Image(i)  & " years old, you're considered a toddler.";
        
    --      when 4..12 =>
    --          return "Since you're" & Integer'Image(i)  & " years old, you're considered a child.";

    --      when 13..19 =>
    --          return "Since you're" & Integer'Image(i)  & " years old, you're considered a teenager.";

    --      when 20..65 =>
    --          return "Since you're" & Integer'Image(i)  & " years old, you're considered an adult.";

    --      -- every possible value for 'i' must be specified, so you can't use < or >
    --      when 66..150 =>
    --          return "Since you're" & Integer'Image(i)  & " years old, you're considered an elder."; 

    --      -- similar to "else"
    --      when others =>
    --          return "Something went wrong. You most likely didn't enter a valid age.";

    --  end case;

    -- Using a "case expression"

    --  Put_Line(case i is
    --          when 0 => "Since you're" & Integer'Image(i)  & " years old, you're considered an infant.",
    --          when 1..3 => "Since you're" & Integer'Image(i)  & " years old, you're considered a toddler.", 
    --          when 4..12 => "Since you're" & Integer'Image(i)  & " years old, you're considered a child.", 
    --          when 20..65 => "Since you're" & Integer'Image(i)  & " years old, you're considered an adult.", 
    --          when 66..150 => "Since you're" & Integer'Image(i)  & " years old, you're considered an elder.",
    --          when others => "Something went wrong. You most likely didn't enter a valid age.");
    --  return " ";

end age;
