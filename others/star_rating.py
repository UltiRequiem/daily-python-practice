"""
Have the function StarRating(str) take the str parameter being passed which will be an average rating between 0.00 and 5.00,
and convert this rating into a list of 5 image names to be displayed in a user interface to represent the rating as a list of stars and half stars.
Ratings should be rounded to the nearest half.
There are 3 image file names available: "full.jpg", "half.jpg", "empty.jpg".
The output will be the name of the 5 images (without the extension), from left to right, separated by spaces.
For example: if str is "2.36" then this should be displayed by the following image:


Examples
Input: "0.38"
Output: half empty empty empty empty
Input: "4.5"
Output: full full full full half
"""

# def main(string):
#    rate = float(string)
#    stars = ""
#    for item in range(5):
#        if rate >= item:
#            stars = stars + str(item)
#
#    print(stars)

# TODO: This
def rate_the_string(string):
    return round(float(string), 1)


def main(string):
    rate = rate_the_string(string)
    output = []

    for item in range(5):
        if item <= rate and rate:
            output.append("full")

    print(output)


if __name__ == "__main__":
    main("4.7777")
