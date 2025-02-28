Rails.application.routes.draw do
  get "messages/create"
  get "conversations/index"
  get "conversations/show"
  get "orders/index"
  get "orders/show"
  get "orders/create"
  get "orders/update"
  get "categories/index"
  get "categories/show"
  get "products/index"
  get "products/show"
  get "products/new"
  get "products/create"
  get "products/edit"
  get "products/update"
  get "products/destroy"
  devise_for :users

  root "landing#index"
end
