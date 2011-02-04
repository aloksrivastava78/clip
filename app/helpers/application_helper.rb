module ApplicationHelper

  # Return a title on a per-page basis.
  def title
    base_title = "Clipper"
    if @title.nil?
      base_title
    else
      "#{base_title} #{@title}"
    end
  end
  def logo
    image_tag("logo.jpeg", :alt => "Clipper App", :class => 'round' )
  end
end
