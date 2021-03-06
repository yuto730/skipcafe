class Admin < ApplicationRecord

  belongs_to :user
  has_one_attached :image
  has_rich_text :content

  with_options presence: true do
    validates :title, length: { maximum: 20 }
    validates :start_on
    validates :image
    validates :content
  end
end
