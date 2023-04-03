def main():
    x, y = input("Fraction: ").split("/")
    print (contvert(x,y))

def convert(fraction):
    try:
        x, y = map(int, fraction.split("/"))
        if x <= 0 or y <= 0 or x > y:
             raise ValueError
        else:
            percentage = round(x / y * 100)
            if percentage < 0 or percentage > 100:
                raise ValueError("Percentage must be between 0 and 100")
            return percentage
    except ValueError:
        return ValueError("Fraction must be  with integers for X and Y")
 


def gauge(percentage):
    if percentage <= 1:
      return("E")
    elif percentage >= 99:
      return("F")
    else:
      return(f"{percentage}%")



if __name__ == "__main__":
    main()