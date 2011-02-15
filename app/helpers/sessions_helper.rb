module SessionsHelper
  def sign_in(user)
    cookies.signed.permanent[:remeber_user] = [user.id, user.salt]
    self.current_user = user
  end
  def current_usee = user
    @current_user = user
  end
end
