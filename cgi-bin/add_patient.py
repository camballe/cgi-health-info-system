#!/usr/bin/env python3
import mysql.connector
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()

firstname = form.getvalue('firstname')
middlename = form.getvalue('middlename')
surname = form.getvalue('surname')
dob = form.getvalue('dob')
gender = form.getvalue('gender')
county = form.getvalue('county')

connection = mysql.connector.connect(
    host="localhost", user="root", password="mrKEN@21411", database="health_info_system")

cursor = connection.cursor()

# perform db operations
add_patient = ("INSERT INTO patients "
               "(firstname, middlename, surname, dob, gender, county) "
               "VALUES (%s, %s, %s, %s, %s, %s)")
data_patient = (firstname, middlename, surname, dob, gender, county)

cursor.execute(add_patient, data_patient)

connection.commit()

cursor.close()
connection.close()

# Send the Location header for redirection
print("Status: 303 See Other")
print("Location: /cgi-bin/records.py")
print("Content-Type: text/html")
print()  # Blank line to indicate the end of the HTTP headers

# HTML response with JavaScript redirect
print("""
<html>
<head>
    <title>Redirecting...</title>
    <script>
        window.location.href = "/cgi-bin/records.py";
    </script>
</head>
<body>
    <h1>Redirecting...</h1>
</body>
</html>
""")
