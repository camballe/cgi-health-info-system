#!/usr/bin/env python3
import cgi
import cgitb
import mysql.connector
from datetime import datetime


cgitb.enable()


def calculate_age(born):
    today = datetime.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


connection = mysql.connector.connect(
    host="localhost", user="root", password="mrKEN@21411", database="health_info_system")

cursor = connection.cursor(dictionary=True)

query = "SELECT * FROM patients ORDER BY id"
cursor.execute(query)

patients = []
for row in cursor:
    row['age'] = calculate_age(row['dob'])
    patients.append(row)

cursor.close()
connection.close()

print("Content-type:text/html\r\n\r\n")
print("""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Health Information System</title>
    <link rel="stylesheet" href="../assets/css/style.css" />
    <link
      rel="shortcut icon"
      href="../assets/images/hospital-logo.png"
      type="image/x-icon"
    />
    <script defer src="../assets/js/script.js"></script>
  </head>

  <body>
    <section class="upper-section">
      <header class="header">
        <img
          src="../assets/images/hospital-logo.png"
          alt="Hospital Logo"
          class="nav-logo"
        />
      </header>
      <nav class="nav">
        <ul class="nav-links">
          <li><a href="/">Home</a></li>
          <li><a href="/registration.html">Registration</a></li>
          <li><a href="/cgi-bin/records.py">Records</a></li>
          <li><a href="/about-us.html">About Us</a></li>
          <li><a href="/contacts.html">Contacts</a></li>
        </ul>
      </nav>
    </section>
    <main class="main">
      <aside class="sidebar">
        <ul class="sidebar-links">
          <li><a href="/registration.html">Registration</a></li>
          <li><a href="/cgi-bin/records.py">Records</a></li>
        </ul>
      </aside>
      <section class="main-content">
        <h1>Patient Records</h1>
        <table>
          <thead>
            <tr>
              <th>Patient ID</th>
              <th>First Name</th>
              <th>Last Name</th>
              <th>Gender</th>
              <th>County</th>
              <th>Age</th>
            </tr>
          </thead>
          <tbody>
""")
for patient in patients:
    print("""
            <tr>
              <td>{}</td>
              <td>{}</td>
              <td>{}</td>
              <td>{}</td>
              <td>{}</td>
              <td>{} years</td>
            </tr>
    """.format(patient['id'], patient['firstname'], patient['surname'], patient['gender'], patient['county'], patient['age']))
print("""
          </tbody>
        </table>
      </section>
    </main>
    <footer class="footer">&copy; Kambale Enoch Nyambu | P15/1921/2022</footer>
  </body>
</html>
""")
