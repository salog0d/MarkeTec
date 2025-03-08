# MarketTEC

## A Marketplace Exclusively for Tecnológico de Monterrey Community

MarketTEC is a web application designed to facilitate buying, selling, and exchanging goods within the Tecnológico de Monterrey community. This platform connects students, faculty, and staff across all campuses, creating a trusted environment for transactions among community members.

## Features

- **Secure Authentication**: Access limited to verified `@tec.mx` and `@tecmilenio.mx` email addresses
- **Campus-Specific Browsing**: Filter listings by campus to find items nearby
- **Categories**: Browse through organized categories including textbooks, electronics, furniture, and more
- **Direct Messaging**: Built-in messaging system to communicate with sellers/buyers
- **Rating System**: Community-based trust system to rate transaction experiences
- **Exchange Option**: List items for exchange instead of selling
- **Watchlist**: Save interesting items to review later
- **Notification System**: Get alerts for price drops, new messages, or when items of interest are posted

## Technology Stack

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: PostgreSQL
- **Authentication**: Django Auth with institutional email validation
- **Hosting**: AWS
- **Version Control**: Git/GitHub

## Installation for Development

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/markettec.git
   cd markettec
   ```

2. Create and activate virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   ```
   cp .env.example .env
   # Edit .env with your database credentials and other settings
   ```

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Start development server:
   ```
   python manage.py runserver
   ```

7. Access the site at `http://localhost:8000`

## Project Structure

```
markettec/
├── accounts/          # User authentication and profiles
├── marketplace/       # Core marketplace functionality
├── messaging/         # Direct messaging system
├── notifications/     # User notification system
├── static/            # Static files (CSS, JS, images)
├── templates/         # HTML templates
├── media/             # User-uploaded content
├── markettec/         # Project settings
├── requirements.txt   # Project dependencies
└── manage.py          # Django management script
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Security Considerations

- Only verified institutional emails can register
- Transactions are conducted in person on campus
- User data is encrypted and protected according to best practices
- Reporting system for suspicious listings or users

## Future Enhancements

- Mobile application
- Integration with institutional payment systems
- Verified student discounts
- Event-based temporary marketplace (beginning/end of semester)
- Sustainability tracking (items reused rather than purchased new)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Project Coordinator: your.email@tec.mx

---

© 2025 MarketTEC - Developed for the Tecnológico de Monterrey Community
