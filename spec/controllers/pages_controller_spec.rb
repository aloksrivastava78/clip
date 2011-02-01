require 'spec_helper'

describe PagesController do

  render_view

  before(:each) do
    @base_title = 'Clipper App'
  end

  describe "GET 'home'" do
    it "should be successful" do
      get 'home'
      response.should be_success
    end

    it "should be successful in displaying title" do
      get 'home'
      response.should has_selector("title",:content => " #{@base_title} | Home " )
    end

  end

  describe "GET 'contact'" do
    it "should be successful" do
      get 'contact'
      response.should be_success
    end

    it "should be successful in displaying title" do
      get 'contact'
      response.should has_selector("title",:content => " #{@base_title} | Contact " )
    end
 

  end

  describe "GET 'about'" do
    it "should be successful" do
      get 'about'
      response.should be_success
    end

    it "should be successful in displaying title" do
      get 'about'
      response.should has_selector("title",:content => " #{@base_title} | About" )
    end


  end
  describe "GET 'help'" do
    it "should be successful" do
      get 'help'
      response.should be_success
    end

    it "should be successful in displaying title" do
      get 'help'
      response.should has_selector("title",:content => " #{@base_title} | Help" )
    end


  end


end
