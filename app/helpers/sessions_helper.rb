module SessionsHelper
<<<<<<< .merge_file_MvADQl

  def sign_in(user)
    cookies.permanent.signed[:remember_token] = [user.id, user.salt]
    self.current_user = user
  end
  
  def current_user=(user)
    @current_user = user
  end
  
  def current_user
    @current_user = user_from_remember_token
#    user = User.new
 #   user = @current_user
  #  puts "It testing content #{user.email}"
  end

  def signed_in?
    !current_user.nil?
  end
  
  def sign_out
    cookies.delete(:remember_token)
    self.current_user = nil
  end
  
  
  private

    def user_from_remember_token
      User.authenticate_with_salt(*remember_token)
    end

    def remember_token
      cookies.signed[:remember_token] || [nil, nil]
    end
 

=======
  def sign_in(user)
    cookies.signed.permanent[:remeber_user] = [user.id, user.salt]
    self.current_user = user
  end
  def current_usee = user
    @current_user = user
  end
>>>>>>> .merge_file_UbIC4k
end