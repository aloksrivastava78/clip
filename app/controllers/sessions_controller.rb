class SessionsController < ApplicationController
  def new
    @title = "Sign in"
  end
  
  def create
    user = User.authenticate(params[:session][:email],
                             params[:session][:password])
    if user.nil?
      flash.now[:error] = "Invalid email/password combination."
      @title = "Sign in"
      render 'new'
    else
      # Sign the user in and redirect to the user's show page.
    end
  end
 
  def destroy
    @user = User.find(params[:user])
    if @user.destroy
       flash[:notice]= "Well thats embarrasing!! We are missing you"
       redirect_to root_path
    else
       flash[:notice] = "Deletion is not successful"
       redirect_to (user_path(@user))
    end
  end
end
