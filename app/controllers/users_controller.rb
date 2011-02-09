class UsersController < ApplicationController
  def new
    @title = 'Sign up'
  end

  def show
    @user = User.find(1)
    @title = @user.name
  end
end
