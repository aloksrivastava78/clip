ActionMailer::Base.smtp_settings = {
  :address              => "smtp.gmail.com",
  :port                 => 587,
  :domain               => "localhost:3000",
  :user_name            => "aloksrivastava78",
  :password             => "mhwy8skq",
  :authentication       => "plain",
  :enable_starttls_auto => true

}

ActionMailer::Base.default_url_options[:host] = "localhost:3000" 
