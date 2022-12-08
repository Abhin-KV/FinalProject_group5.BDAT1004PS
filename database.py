import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "123456789@aA"
)

mycursor = mydb.cursor()

mycursor.execute("create database testdbcheck")
mycursor.execute('Show Database')
for db in mycursor:
    print(db[0])


# create table
# id
# title
# url
# is_paid
# num_subscribers
# avg_rating
# avg_rating_recent
# rating
# num_reviews
# is_wishlisted
# num_published_lectures
# num_published_practice_tests
# created
# published_time
# discount_price__amount
# discount_price__currency
# discount_price__price_string
# price_detail__amount
# price_detail__currency
# price_detail__price_string