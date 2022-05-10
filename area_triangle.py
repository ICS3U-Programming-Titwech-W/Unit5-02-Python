#!/usr/bin/env python3

# Created by: Titwech Wal
# Created on: May.9.2022
# the program tells the area of a triangle
# with the user input


def calc_area(base, height):

    # calaculae area
    area = (base * height)/2

    # show the area
    print("The area of the triangle is {:,.2f} cm².". format(area))


def main():

    # get the input from the user
    base_str = input("Enter the base of a triangle(cm): ")
    height_str = input("Enter the height of a triangle(cm): ")
    print("")

    try:
        # input to int
        base_float = float(base_str)
        height_float = float(height_str)

        if base_float > 0 and height_float > 0:

            # call the function above
            calc_area(base_float, height_float)
        else:
            print("Enter a postive number")

    except Exception:
        print("Please enter a vaild number.")


if __name__ == "__main__":
    main()
