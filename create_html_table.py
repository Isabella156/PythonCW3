#  create_html_table.py (Template file)

#  This function makes an html file to display some data.
#  title: for the title and heading of the html page.
#  data: a list of data records.
#  htmlfile: the name of the html file to be created.


def create_html_table(title, data, htmlfile):
    print("Creating html file:", htmlfile)
    with open(htmlfile, 'w') as html:
        html.write('<html>\n')
        html.write('<title>' + title + '</title>\n')
        html.write('<center>\n')
        html.write('<H1>' + title + '</H1>\n')
        html_table = create_html_table_with_data(data)
        html.write(html_table)
        html.write('</center>\n')
        html.write('</html>\n')


def create_html_table_with_data(data):
    # concatenating the string in html format for the html page
    html_string = "<style>\n"
    html_string += "table, th, td {\n border: 1px solid black;\n"
    html_string += "border-collapse: collapse;\n"
    html_string += "}\n"
    html_string += "</style>\n"
    html_string += "<table>\n"

    # read all data items in data and formatting it with html tags
    # str(datum) converts the data items to string format for diplay in html
    for record in data:
        html_string += "<tr>\n"
        for datum in record:
            html_string += "<td>" + str(datum) + "</td>\n"
        html_string += "<tr>\n\n"
    html_string += "</table>\n\n"
    return html_string

# This is an example data for demo.
# For your coursework, you are required to extract data from a CSV file.
# Note that if you have a fixed data format, you may hardcode the
# field headings ("NAME", "AGE", "PLACE OF BIRTH") in the html_string.


FRIEND_DATA = [
        ["NAME", "AGE", "PLACE OF BIRTH"],
        ["Susan Sarandon", 30, "London"],
        ["James Lee", 20, "Chicago"],
        ["Robert Cult", 50, "Sabah"],
    ]

# Test the function create_html_table with FRIEND_DATA
create_html_table("Friends", FRIEND_DATA, "my_friend.html")
