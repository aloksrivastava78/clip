#!/home/alok/.rvm/rubies/ruby-1.9.2-p136/bin/ruby

class User
  attr_accessor :name, :email
  
  def initialize(attributes = {})
    @name = attributes[:name]
    @email = attributes[:email]
  end

  def formatted_email
    "#{@name} <#{@email}"
  end
  
  def string_shuffle
    @name.split('').shuffle.join
  end
end

