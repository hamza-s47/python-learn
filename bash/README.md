#!/bin/bash

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

# SIX (LOOP)
my_arr=(Apple Banana Peach)

for idx in ${!my_arr[@]};
do
    echo $idx and ${my_arr[idx]};
done

# SEVEN (FUNCTION)
sum_num(){
    local num1=$1
    local num2=$2
    local sum=$((num1 + num2))
    echo $sum
}

result=$(sum_num 1 2)
echo $result

# EIGHT (SORT)
my_arr=(Peach Apple Banana)
result_arr=($(printf "%s\n" "${my_arr[@]}" | sort))  (Sorting Arrays)
echo ${result_arr[@]}

echo -e "Banana\nApple\nPeach\nGrape" > fruit.txt
sort fruit.txt -o fruit2.txt (Sorting files)
head fruit2.txt

# FILTER
countries=()
while IFS= read -r val; do
    [[ -z $val ]] && break
    countries+=($val)
done

my_arr=()

for c in ${countries[@]}; do
    if [[ "${c:0:1}" =~ [A-Z] ]]; then
        abc=".${c:1}"
        my_arr+=("$abc")
    else
        my_arr+=($c)
    fi
done

echo ${my_arr[@]}