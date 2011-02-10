class UsersController < ApplicationController
  def new
    @user = User.new
    @title = 'Sign up'
  end
  
  def create
    @user.save?
  end

  def show
    @user = User.find(params[:id])
    @title = @user.name
  end
end
