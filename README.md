# Online Food Ordering System

## About the Project
The Online Food Ordering System is a web application developed using Python and Django. It allows users to browse restaurants, explore menus, register or log in, add items to their cart, and place food orders online.

## Features
- User registration and login
- Browse restaurants and food menus
- Add food items to the cart
- Place orders and view order history
- Order success page
- Restaurant and order management through Django
- Responsive page styling using CSS

## Technologies Used
- **Backend:** Python, Django
- **Frontend:** HTML, CSS
- **Database:** SQLite
- **Version Control:** Git and GitHub

## Project Structure
- `accounts/` – User account functionality
- `restaurants/` – Restaurant and menu functionality
- `orders/` – Cart and order functionality
- `reviews/` – Reviews application
- `templates/` – HTML templates
- `static/` – CSS and static files
- `food_ordering/` – Django project configuration
- `manage.py` – Django management utility

## How to Run the Project

1. Install Python and Django.
2. Clone this repository:
   ```bash
   git clone https://github.com/asadiganesh23-hue/online-food-ordering.git
   ```
3. Open the project folder:
   ```bash
   cd online-food-ordering
   ```
4. Create and activate a virtual environment.
5. Install Django:
   ```bash
   pip install django
   ```
6. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
7. Start the development server:
   ```bash
   python manage.py runserver
   ```
8. Open `http://127.0.0.1:8000/` in your browser.

## Future Enhancements
- Online payment integration
- Order tracking
- Restaurant ratings and reviews
- Improved responsive design
- Email notifications for orders

## Author
**Ganesh**

## License
This project is available for educational purposes. Add a suitable open-source license if you intend to distribute it for reuse.
