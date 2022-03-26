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

# This function sums the data and store it in list and then return the list
# The map() function is a built-in function that calls the specified function
# for each item of an iterable (such as string, list, tuple or dictionary) and
# returns a list of results.


def process_data(data):
    count = 0
    sum_list = [0 for i in range(4)]
    item = 0
    for record in data:
        count += 1
        item = 0
        for datum in record:
            sum_list[item] += int(datum)
            item += 1

    newList = list(map(lambda x: x/count, sum_list))
    return newList


def create_html_table_with_data(data):
    # concatenating the string in html format for the html page
    html_string = "<style>\n"
    html_string += "table, th, td {\n border: 1px solid black;\n"
    html_string += "border-collapse: collapse;\n"
    html_string += "}\n"
    html_string += "</style>\n"
    html_string += "<table>\n"
    html_string += "<tr>\n"
    html_string += "<th> Subject 1</th>\n"
    html_string += "<th> Subject 2</th>\n"
    html_string += "<th> Subject 3</th>\n"
    html_string += "<th> Subject 4</th>\n"
    html_string += "</tr>\n"

    # read all data items in data and formatting it with html tags
    # str(datum) converts the data items to string format for diplay in html
    html_string += "<tr>\n"
    for datum in process_data(data):
        html_string += "<td>" + str(datum) + "</td>\n"
    html_string += "<tr>\n\n"
    html_string += "</table>\n\n"

    return html_string


# This is an example data for demo.
# For your coursework, you are required to extract data from a CSV file.
# Note that if you have a fixed data format, you may hardcode the
# field headings ("Subject 1", "Subject 2", "Subject 3", "Subject 4") in
# the html_string.

MARKS_DATA = [
        [10, 20, 20, 10],
        [20, 30, 30, 10],
        [30, 20, 40, 10],
        [40, 50, 50, 10],
    ]

# Test the function create_html_table with FRIEND_DATA
create_html_table("Marks", MARKS_DATA, "marks.html")
