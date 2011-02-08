require 'spec_helper'

describe User do
 
  before(:each) do
    @attr = { :name => "Example User", :email => "user@example.com" }
  end
 

  it "should not accept null names" do
    u = User.new (@attr.merge(:name => ""))
    u.should_not be_valid
  end
  


   it "should reject email addresses identical up to case" do
    upcased_email = @attr[:email].upcase
    u=User.create!(@attr.merge(:email => upcased_email))
    user_with_duplicate_email = User.new(@attr)
    p user_with_duplicate_email 
    #u.each do |term|
     # puts term[:name], term[:email]
      #puts user_with_duplicate_email[:name], user_with_duplicate_email[:email] 
    #end 
    user_with_duplicate_email.should_not be_valid
  end

end
