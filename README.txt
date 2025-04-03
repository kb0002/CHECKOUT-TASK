Project Setup & Execution
1️⃣ Install Dependencies
Ensure you have Python installed, then install the required packages:

sh
Copy
Edit
pip install flask flask-sqlalchemy
2️⃣ Run the Flask Application
Execute the following command to start the server:

sh
Copy
Edit
python app.py
The application will start at http://127.0.0.1:5000/.

 API Usage & Testing
3️⃣ Checkout API
The API calculates the total price of scanned items while applying bulk discounts.

🔹 Endpoint
http
Copy
Edit
POST /checkout
🔹 Request Body (JSON)
json
Copy
Edit
{
  "items": "AAABBD"
}
🔹 Response (JSON)
json
Copy
Edit
{
  "total_price": 190
}
Test the API
You can test the API using:

Postman (Send a POST request to http://127.0.0.1:5000/checkout)

cURL Command

sh
Copy
Edit
curl -X POST http://127.0.0.1:5000/checkout -H "Content-Type: application/json" -d '{"items": "AAABBD"}'
 Expected Test Cases
Input	Expected Output
"" (empty)	{"total_price": 0}
"A"	{"total_price": 50}
"AA"	{"total_price": 100}
"AAA"	{"total_price": 130} (bulk discount applied)
"AAABBD"	{"total_price": 190}
"DABABA"	{"total_price": 190}
 Features Implemented
✅ SQLite Database for storing product pricing
✅ Bulk discount handling for items
✅ REST API with Flask
✅ Auto-seeding of products on startup
✅ Error handling for invalid inputs

