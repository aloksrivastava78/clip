require 'spec_helper'

describe User do
  before (:each) do
    @user = {:name => 'balu' , :email => 'balu@chipmonk.in'}
  end
  it "should create a new instance given valid attributes" do
    User.create!(@user)
  end

  it "should require a name" do
    u = User.new(@user.merge(:name => "") )
    u.should_not be_valid
  end
  
  it "should have length with limits of 51 chars" do
     str = 'a' * 51
     u = User.new(@user.merge(:name => str) )
     u.should_not be_valid
  end
  it "should reject duplicate email addresses" do
    # Put a user with given email address into the database.
    User.create!(@user)
    user_with_duplicate_email = User.new(@user)
    user_with_duplicate_email.should_not be_valid
  end

end
