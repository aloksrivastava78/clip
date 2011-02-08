require 'spec_helper'

describe User do
 
 before (:each) do
    @user = {:name => "balu" , :email => "alok@chipmonk.in", :password => "foobar",:password_confirmation => "foobar"}
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


  describe "password validations" do

   before (:each) do
     @user = {:name => 'balu' , :email => 'alok@chipmonk.in', :password => 'foobar' , :password_confirmation => 'foobar'}
   end

    it "should require a password" do
      User.new(@user.merge(:password => "", :password_confirmation => "")).
        should_not be_valid
    end

    it "should require a matching password confirmation" do
      User.new(@user.merge(:password_confirmation => "invalid")).
        should_not be_valid
    end

    it "should reject short passwords" do
      short = "a" * 5
      hash = @user.merge(:password => short, :password_confirmation => short)
      User.new(hash).should_not be_valid
    end

    it "should reject long passwords" do
      long = "a" * 41
      hash = @user.merge(:password => long, :password_confirmation => long)
      User.new(hash).should_not be_valid
    end
  end
  



  describe "encrypted passwrord test" do
    before(:each) do
      @attr = User.create!(@user)
    end
   it "should have an encrypted password attribute" do
      @attr.should respond_to(:encrypted_password)
    end

   it "should set the encrypted password" do
      @attr.encrypted_password.should_not be_blank
   end
   it "should not match the submitted password and actual password" do
      @attr.has_password?("invalid").should be_false
   end
   it "should match the submitted password and actual password" do
      @attr.has_password?(@user[:password]).should be_true
   end
   
   describe "authenticate method" do

    it "should return nil on email/password mismatch" do
       wrong_password_user = User.authenticate(@user[:email], "wrongpass")
       wrong_password_user.should be_nil
    end

    it "should return nil for an email address with no user" do
      nonexistent_user = User.authenticate("bar@foo.com", @user[:password])
      nonexistent_user.should be_nil
    end

    it "should return the user on email/password match" do
      matching_user = User.authenticate(@user[:email], @user[:password])
      matching_user.should == @attr
    end
   end
  end
end
