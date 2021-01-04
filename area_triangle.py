#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: January 2021
# this program calculates the area of a triangle

def calculate_area(base, height):
    # calculates area

    # process & output
    area_of_triangle = (1/2 * base) * height
    print("The area of the triangle is {:,.2f}cm²".format(area_of_triangle))


def main():
    # this program calculates the area of a triangle
    while True:
        # input
        base_from_user = input("Enter the base of the triangle (cm):")
        print("\n", end="")
        height_from_user = input("Enter the height of the triangle (cm):")
        print("\n", end="")
        try:
            base_from_user = float(base_from_user)
            height_from_user = float(height_from_user)
            if base_from_user < 0 or height_from_user < 0:
                print("{0} or {1} was not above 0."
                      "Please ensure both height and base are higher then 0"
                      .format(base_from_user, height_from_user))
                print("\n", end="")
            else:
                break
        except Exception:
            print("{0} or {1} is not an integer. Please enter a number."
                  .format(base_from_user, height_from_user))
            print("\n", end="")
    # call function
    calculate_area(base_from_user, height_from_user)


if __name__ == "__main__":
    main()
