# Marketec - Ruby on Rails Marketplace Application

Marketec is a full-featured marketplace application built with Ruby on Rails where users can buy and sell products, chat with other users, and manage their listings and orders.

## 🚀 Features

- **User Authentication**: Secure sign-up, login, and profile management using Devise
- **Product Listings**: Create, update, delete, and browse product listings with multiple images
- **Categories**: Browse products by category with filtering options
- **Search**: Find products with full-text search
- **Messaging System**: Real-time chat between buyers and sellers
- **Order Management**: Complete order lifecycle from purchase to delivery
- **User Dashboard**: Manage listings, orders, and conversations
- **Responsive Design**: Mobile-friendly interface built with Bootstrap

## 📋 Requirements

- Ruby 3.0.0+
- Rails 6.1.0+
- PostgreSQL 12.0+
- Redis (for ActionCable/real-time features)
- NodeJS 14.0.0+ and Yarn 1.22.0+ (for the asset pipeline)
- ImageMagick (for image processing)

## 🔧 Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/marketec.git
cd marketec
```

2. **Install dependencies**

```bash
bundle install
yarn install
```

3. **Configure the database**

Update `config/database.yml` with your PostgreSQL credentials.

```bash
rails db:create
rails db:migrate
rails db:seed  # Loads sample data if available
```

4. **Set up environment variables**

Create a `.env` file in the root directory and add necessary environment variables:

```
DATABASE_URL=postgres://username:password@localhost/marketec_development
REDIS_URL=redis://localhost:6379/1
```

5. **Start the servers**

```bash
redis-server
rails server
```

6. **Access the application**

Open your browser and navigate to `http://localhost:3000`

## 🧪 Running Tests

```bash
rails test                  # Run all tests
rails test:system           # Run system tests
rails test:controllers      # Run controller tests
```

## 🔄 Deployment

### Heroku Deployment

```bash
heroku create
heroku addons:create heroku-postgresql:hobby-dev
heroku addons:create heroku-redis:hobby-dev
git push heroku main
heroku run rails db:migrate
heroku run rails db:seed
```

### Docker Deployment

A `Dockerfile` and `docker-compose.yml` are provided for containerized deployment.

```bash
docker-compose build
docker-compose up
```

## 🔨 Project Structure

- `app/models`: Database models
- `app/controllers`: Controllers handling request/response logic
- `app/views`: View templates
- `app/helpers`: View helper methods
- `app/assets`: JavaScript, CSS, and images
- `app/channels`: ActionCable channels for real-time features
- `config`: Application configuration
- `db`: Database schema and migrations
- `lib`: Library modules
- `test`: Automated tests

## 📝 Development Guide

### Adding a New Category

1. Create a migration:
```bash
rails generate migration AddNewCategory name:string
```

2. Update the migration file:
```ruby
def change
  Category.create(name: "Electronics")
end
```

3. Run the migration:
```bash
rails db:migrate
```

### Adding a New Feature

1. Create a new branch:
```bash
git checkout -b feature/feature-name
```

2. Implement the feature with tests
3. Submit a pull request

## 🔌 API Endpoints

Marketec includes a JSON API for integration with other applications:

- `GET /api/v1/products` - List all products
- `GET /api/v1/products/:id` - Get a specific product
- `POST /api/v1/products` - Create a new product
- `PUT /api/v1/products/:id` - Update a product
- `DELETE /api/v1/products/:id` - Delete a product

Authentication for API endpoints is handled using JWT tokens.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


![imagen](https://github.com/user-attachments/assets/0a6414fc-b8bb-4a9c-b0cc-429ebec299ef)
