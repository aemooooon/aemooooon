---
layout: post
subtitle: ruby
categories: [Ruby]
header:
    image: header.jpg
    align:
    text: light
---

A simple notes when programming 4 comes with Ruby, just for done a small assignment to learn it.

# Ruby basic

```ruby
# this is a single line comment

=begin
multiple line comment
=end

puts # 换行
print # 不换行

print "Enter a Value: "
first_number = gets.to_i # 转换成整数
print "Enter another Value: "
second_number = gets.to_i
puts first_num.to_s + " + " + second_num.to_s + 
" = " + (first_number + second_number).to_s # 转换成字符串

# Arithmetic Operators
+ - * / %

puts 1.class
puts "abc".class
puts ["a","b","c"].calss

# CONSTANT
A=3.1415926
```

# 文件操作
```ruby
write_handler = File.new("test.txt", "w")
write_handler.puts("Hello ruby file").to_s
write_handler.close

data_from_file=File.read("test.txt")
puts "Data from File: " + data_from_file

write_handler = File.new("test.txt", "a") # 追加内容
write_handler.puts "new content"
write_handler.close


file=File.new("aemon.txt","w")

file.puts "hua,English,swimming,1000"
file.puts "ke,Chinese,jump,800"
file.puts "ting,French,run,99"
file.puts "li,German,fly,387"
file.close

File.open("aemon.txt") do |record|
  record.each do |item|
    name,lang,spec,sales=item.chomp.split(',')
    puts "#{name} was an #{lang} author that spec #{spec} with #{sales}"
  end
end

```

# 加载其它的可执行rb文件

> load "otherRubyFile.rb"

# 条件运算符

```ruby
Comparison: ==  !=  <  >  <=  >=
Logical: && || ! and or not

puts 5 <=> 10  # -1
puts 5 <=> 5   # 0
puts 10 <=> 5  # 1

age = 12
if (age >= 5) $=&& (age <= 6)
  puts "You are in Kindergarten"
elsif (age >= 7) && (age <= 13)
  puts "You are in the middle school"
  puts "Yeah"
else
  puts "Stay Home"
end

unless age > 4
  puts "no school"
else
  puts "go to school"
end

puts "you are young" if age < 30

print "Enter Greeting: "
greeting = gets.chomp

case greeting
when "French","french"
  puts "Bojour"
  exit
when "Spanish", "spanish"
  puts "Hola"
  exit
else "English"
  puts "Hello"
end

puts (age >= 50) ? "old" : "young"

```


# 循环语句

```ruby

#display even numbers from 0 to 100

x=0
loop do
  x += 1
  next unless (x % 2) == 0
  puts x
  break if x >= 100
end

y=1
while y<=10
  y+=1
  next unless(y % 2)==0
  puts y
end

a=1
until a >= 10
  a += 1
  next unless (a  % 2) == 0
  puts a
end

numbers = [1,2,3,4,5]
for number in numbers
  puts "#{number}, "
end

groceries=["bananas", "sweet potatoes", "pasta", "tomatoes"]
groceries.each do |food|
  puts "Get some #{food}"
end

(0..5).each do |i|
  puts "# #{i}"
end

# Function
def add_nums(num_1, num_2)
  return num_1.to_i + num_2.to_i
end

puts add_nums(3,4)


x=1
def change_x(x)
  x=4
end
change_x(x)
puts "x = #{x}" # the result is 1 函数内部不会改变外部变量的值
```

# 异常

```ruby
print "Enter a Number"
first_num = gets.to_i
print "Enter another Number"
second_num = gets.to_i

begin
  answer = first_num / second_num

rescue
  puts "You can't divide by zero"
  exit
end

puts "#{first_num} / #{second_num} = #{answer}"


age = 12
def check_age(age)
  raise ArgumentError, "Enter Positive Number" unless age>0
end

begin
  check_age(-1)
rescue ArgumentError
  puts "That is an impossible age"
end
```

# String

```ruby
single quote and double quote:
puts "Add them #{4+5}\n\n"
puts 'Add them #{4+5}\n\n'

output result:
Add them 9

Add them #{4+5}\n\n

multi line string

multiline_string= <<EOM
This is a very long string
that contains interpolation
like #{4+5} \n\n
EOM

puts multiline_string


first_name = "Hua"
last_name = "Wang"

full_name = first_name + last_name

middle_name = "Tang"

full_name = "#{first_name} #{middle_name} #{last_name}"

puts full_name
puts full_name.include?("Tang ")
puts full_name.size

puts "Vowels: " + full_name.count("aeiou").to_s
puts "Consonants: "+ full_name.count("^aeiou").to_s # 计数不包含的

puts full_name.start_with?("Wang")
puts "Index: " + full_name.index("Tang").to_s

puts "a == a" + ("a" == "a").to_s
puts "\"a\".equal?(\"a\"): " +("a".equal?"a").to_s

puts first_name.eql?first_name

puts full_name.upcase
puts full_name.downcase
puts full_name.swapcase

full_name="        " + full_name
full_name=full_name.lstrip
full_name=full_name.rstrip
full_name=full_name.strip

puts full_name.rjust(30, '.')
puts full_name.ljust(30,'.')
puts full_name.center(30,'.')

puts full_name.chop # cut 1
puts full_name.chomp('ang') # cut all we found

puts full_name.delete("a")

name_array=full_name.split(//)
puts name_array

name_array=full_name.split(/ /)
puts name_array

to_i # convert int
to_f # convert float
to_sym 

# Escape sequences
# \\ Backslash
# \' Single-quote
# \" Double-quote
# \a Bell
# \b Backspace
# \f Formfeed
# \n Newline
# \r Carriage
# \t Tab
# \v Vertical tab
```

# 类，属性，方法，继承

```ruby
class Animal
  def initialize
    puts "Creating a new animal"
  end

  def set_name(new_name)
    @name=new_name
  end

  def get_name
    @name
  end

  def name
    @name
  end

  def name=(new_name)
    if new_name.is_a?(Numeric)
      puts "Name can't be a number"
    else
      @name=new_name
    end
  end
end

cat = Animal.new
cat.set_name("Peekaboo")

puts cat.get_name

puts cat.name

cat.name="Sophie"
puts cat.name

class Dog
  attr_accessor :name, :height, :weight

  def break
    return "Generic Bark"
  end
end

rover = Dog.new

rover.name="Rover"
puts rover.name


class GermanShepard < Dog
  def bark
    return "Loud Bark"
  end
end

max =GermanShepard.new
max.name="Max"

printf "%s goes %s \n", max.name, max.bark() # 格式化变量with字符串

```
# module

> human.rb
```ruby
module Human
  attr_accessor :name, :height, :weight

  def run
    puts self.name + " runs"
  end
end
```

> smart.rb
```ruby
module Smart
  def act_smart
    return "E = mc2"
  end
end
```

> main.rb
```ruby
require_relative "human"
require_relative "smart"

module Animal
  def make_sound
    puts "Grrrrr"
  end
end

class Dog
  include Animal
end

rover = Dog.new
rover.make_sound

class Scientist
  include Human
  prepend Smart

  def act_smart
    return "E=mc^2"
  end
end

einstein=Scientist.new
einstein.name="Albert"
puts einstein.name
einstein.run

puts einstein.name + " says " + einstein.act_smart
```

# 多态 Polymorphism

```ruby
class Bird
  def tweet(bird_type)
    bird_type.tweet
  end
end

class Cardinal < Bird
  def tweet
    puts "Tweet tweet"
  end
end

class Parrot < Bird
  def tweet
    puts "Squawk"
  end
end

generic_bird=Bird.new
generic_bird.tweet(Cardinal.new)
generic_bird.tweet(Parrot.new)
```

# Symbol
```ruby
:hua

puts :hua
puts :hua.to_s
puts :hua.class
puts :hua.object_id

```

# 数组 Array
```ruby
array_1 = Array.new
array_2 = Array.new(5)
array_3 = Array.new(5, "empty")
array_4 = [1,"two",3,5.5]

puts array_1
puts array_2
puts array_3 # 5个元素，每一个都默认是“empty”
puts array_4

puts array_4[1,3].join("-") #从第一个索引开始，连续join 3个元素
puts array_4.values_at(0,1,3).join("~")

array_4.unshift(0) # 从头部添加元素
array_4.shift() # 从头部删除元素

array_4.push(100,200) # push 或者 << 表示添加元素到尾部 
array_4.pop # 从尾部删除元素

array_4.concat([10,20,30])
puts array_4.to_s
puts "Array size: "+ array_4.size().to_s
puts "Array contains 100: " + array_4.include?(100).to_s
puts "how many 100s: "+ array_4.count(100).to_s
puts "Array empty: "+ array_4.empty?.to_s

puts array_4.join("~")
p array_4 # p把数组的格式也一起打印出，看起来比较友好

array_4.each do |v|
  print v
end

```

# Hash key value
```ruby
number_hash = {"PI"=> 3.14, "Glolden" => 1.618, "e" => 2.718 }
puts number_hash["PI"]

superheroes = Hash["Clark Kent", "Superman", "Bruce Wayne", "Batman"]

puts superheroes["Clark Kent"]

superheroes["Barry Allen"]="Flask"

samp_hash = Hash.new("No such Key")
puts samp_hash["Dog"]

superheroines=Hash["Lisa Model", "Aquagirl", "Betty Kane", "Batgirl"]

superheroes.update(superheroines) # merge 

superheroes.each do |key, value|
  puts key.to_s + " : " +value
end

superheroes.has_key?("Lisa Model")
superheroes.has_value?("Aquagirl")
superheroes.empty?.to_s
superheroes.size.to_s

superheroes.delete("Barry Allen")
```

# Enumerable
```ruby
class Menu
  include Enumerable

  def each 
    yield "pizza"
    yield "spaghetti"
    yield "salad"
    yield "water"
    yield "bread"
  end
end

menu_options = Menu.new

menu_options.each do |item|
  puts "would you like: #{item}"
end

p menu_options.find{|item| item="pizza"}

p menu_options.select{|item| item.size <= 5}

p menu_options.reject{|item| item.size <= 5}

p menu_options.first

p menu_options.take(2)

p menu_options.drop(2)

p menu_options.min

p menu_options.max

p menu_options.sort

menu_options.reverse_each{|item| puts item}


```