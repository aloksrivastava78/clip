class UsersController < ApplicationController
  def new
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

  def show
    @user = User.find(1)
    @title = @user.name
  end
end
