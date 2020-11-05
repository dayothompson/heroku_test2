from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import psycopg2


app = Flask(__name__)
# mongo = PyMongo(app, uri="mongodb://localhost:27017/realestate_db")


db = SQLAlchemy()


# connect to the db
con = psycopg2.connect(
            host="ec2-100-25-100-81.compute-1.amazonaws.com",
            database="dd84gatn2dg7pv",
            user="gtqpiclsgecqkw",
            password="793202fe1da2aa142deb488d82115a6d2e7991946b60c581838fb932dca4ec73"
)


# connect to db
# conn = sql.connect("test.sqlite")
# print("Opened database successfully")


def listings():
    # con = sql.connect("test.sqlite")
    # con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM calgary")
    # cur.execute("SELECT json_agg(t) FROM (SELECT * FROM calgary)t")
    # cur.execute("SELECT json_agg(t) FROM (SELECT cl.price, cl.address, cl.postal_code, cl.bed, cl.full_bath, cl.half_bath, cl.property_area, cl.property_type, s.walk_score, s.bike_score, s.transit_score, coord.lat, coord.long FROM calgary_df AS cl JOIN score_df AS s ON cl.postal_code = s.postal_code JOIN coordinates_df AS coord ON s.postal_code = coord.postal_codes WHERE cl.price < 1000000 AND cl.property_area < 4000 AND s.walk_score > 5 AND s.bike_score > 0 AND s.transit_score > 0)t")


    list_data = cur.fetchall()
    # print(list_data)
    return list_data


@app.route('/')
def home():
    rows = listings()
    print(rows)
    return render_template("index.html", row=[i for i in rows])


# @app.route('/')
# def home():
#     con = sql.connect("test.sqlite")
#     # con.row_factory = sql.Row
#
#     cur = con.cursor()
#     cur.execute("select * from calgary")
#
#     rows = cur.fetchall()
#     # print(rows)
#     return render_template("index.html", row=[i for i in rows])


if __name__ == '__main__':
   app.run(debug = True)

#
# # def calgary_data_fun():
# #     cur = con.cursor()
# #
# #     # execute query
# #     cur.execute("SELECT json_agg(t) FROM (SELECT cl.price, cl.address, cl.postal_code, cl.bed, cl.full_bath, cl.half_bath, cl.property_area, cl.property_type, s.walk_score, s.bike_score, s.transit_score, coord.lat, coord.long FROM calgary AS cl JOIN score AS s ON cl.postal_code = s.postal_code JOIN coordinates AS coord ON s.postal_code = coord.postal_codes)t")
# #
# #     calgary_data = cur.fetchall()
# #     # print(calgary_data)
# #
# #     # close cursor
# #     cur.close()
# #
# #     # close the connection
# #     con.close()
# #
# #     return calgary_data
#
# @app.route("/")
# def home():
#
#     # create cursor
#     cur = con.cursor()
#
#     # execute query
#     #cur.execute("SELECT json_agg(t) FROM (SELECT cl.price, cl.address, cl.postal_code, cl.bed, cl.full_bath, cl.half_bath, cl.property_area, cl.property_type, s.walk_score, s.bike_score, s.transit_score, coord.lat, coord.long FROM calgary AS cl JOIN score AS s ON cl.postal_code = s.postal_code JOIN coordinates AS coord ON s.postal_code = coord.postal_codes)t")
#
#     cur.execute("SELECT cl.price, cl.address, cl.postal_code, cl.bed, cl.full_bath, cl.half_bath, cl.property_area, cl.property_type, s.walk_score, s.bike_score, s.transit_score, coord.lat, coord.long FROM calgary AS cl JOIN score AS s ON cl.postal_code = s.postal_code JOIN coordinates AS coord ON s.postal_code = coord.postal_codes WHERE cl.price < 1000000 AND cl.property_area < 4000")
#
#     calgary_data = cur.fetchall()
#     # print(calgary_data)
#
#     # close cursor
#     # cur.close()
#
#
#     # close the connection
#     # con.close()
#
#     # Return template and data
#     return render_template("index.html", calgary=[i for i in calgary_data])
#
#
# @app.route("/jsonified")
# def calgary_data():
#     """Return the Calgary data as json"""
#     calgary = home()
#     # calgary = calgary[:15]
#     return jsonify(calgary)
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
#
