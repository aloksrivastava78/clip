class UsersController < ApplicationController
  def new
    @user = User.new
    @title = 'Sign up'
    @user = User.new
  end

  def create
    @user = User.new(params[:user])
    if @user.save
      #handle success
    else
      @title = "Sign up"
      render 'new'
    end
  end
  
  def create
    @user.save?
  end

  def show
    @user = User.find(params[:id])
    @title = @user.name
  end
end
