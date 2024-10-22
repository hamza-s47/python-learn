# BASH

# ONE
chmod +x (Executable permission)
/usr/local/bin  (move ur .sh file in this dir to exectute globally)

# TWO
intro=My name is (Assign value to variable)
read _name  (Taking user input an saved in variable _name)
echo intro $_name (Output that variable _name)

echo My name is $1 and age $2  ($1 is first arg in terminal with executable file and so on...)
./script.sh Hamza 27  (Example)

# THREE
x=5
y=10

echo $((x + y))

let "ans = $x / $y"
echo $ans

echo "scale=2; $x / $y" | bc  (scale is telling how much values need after decimal)

# FOUR
read -p "What is the password " _pass

if [ "$_pass" = "3598" ]
then
    echo You are Hamza
else
    echo Who are you?
fi

# FIVE
read _money

if [ "$_money" -lt 4000 ]
OR
if (( "$_money" < 4000 ))

Operators:
-gt, -ge, -lt, -le, -eq, -ne with []
>, >=, <, <=, = or ==, != with ()