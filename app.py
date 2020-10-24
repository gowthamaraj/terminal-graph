"""Program to print a graph based on the given sequence of input"""

# test inputs
# vengatesh@cybersecurityworks.com
seq1 = [
    3, 1, 2, 3, 6, 2,
    3, 6, 2, 3, 6, 3, 2, 3,
    6, 2, 3, 4, 3, 2, 5, 4,
    2, 1, 2, 1, 2, 3, 1, 2,
    6, 2, 3, 6, 2, 3, 6, 3,
    2, 3, 1, 5, 3, 2, 1, 2,
    4, 2, 1, 8, 1, 2]
seq2 = [
    10, 7, 12, 2, 4, 7, 2, 4, 1, 2, 6, 6, 3, 2, 1,
    4, 7, 2, 7, 3, 1, 3, 11, 4, 2, 1, 5, 2, 3, 3,
    3, 6, 1, 3, 9, 5, 2, 1, 2, 11, 9, 2, 3, 8, 2,
    5, 1, 2, 7, 2, 4, 11, 2, 12
]


def display(banner: list, peak: dict, plot_height: int,rising: bool) -> None:
    """function to turn the 2-d array given into a nice plot in the terminal """

    if(not rising):
        # customizing the peak
        banner[peak["count"]][peak["y"]+1] = "<"
        banner[peak["count"]][peak["y"]+2] = "/"
        banner.insert(peak["count"]+1, [" " for i in range(plot_height)])
        banner[peak["count"]+1][peak["y"]+2] = "|"
        banner[peak["count"]+2][peak["y"]+1] = ">"
        banner[peak["count"]+2][peak["y"]+2] = "\\"
        banner[peak["count"]+1][peak["y"]+3] = "o"
    else:
        banner.insert(peak["count"]+1, [" " for i in range(plot_height)])
        banner.insert(peak["count"]+2, [" " for i in range(plot_height)])
        banner[peak["count"]][peak["y"]+1] = "<"
        banner[peak["count"]+2][peak["y"]+1] = ">"
        banner[peak["count"]][peak["y"]+2] = "/"
        banner[peak["count"]+2][peak["y"]+2] = "\\"
        banner[peak["count"]+1][peak["y"]+2] = "|"
        banner[peak["count"]+1][peak["y"]+3] = "o"


    # transpose the array
    banner = [['_']+item for item in banner]
    banner = [[banner[j][i]
               for j in range(len(banner))] for i in range(len(banner[0]))]
    for item in banner[::-1]:
        print('|', ' '.join(item))


def make_banner(seq: list) -> tuple:
    """function to make a 2-d array with " " string. This 2-d array will be manipulated to generate the plot"""
    # calculate the height for the plot
    plot_height = 0
    bias = 0
    sum_plot = 0
    toggler = 1
    for item in seq:
        sum_plot = sum_plot + item*toggler
        toggler = -1 * toggler
        if sum_plot < bias:
            bias = sum_plot
        if sum_plot > plot_height:
            plot_height = sum_plot
    plot_height = plot_height + bias + 10 + \
        sum([seq[i] for i in range(0, len(seq), 2)]) - \
        sum([seq[i] for i in range(1, len(seq), 2)])
    # defining a banner
    total = sum(seq)
    banner = [[" " for i in range(plot_height)] for j in range(sum(seq))]
    return (banner, plot_height, bias)


def generate_plot(banner: list, seq: list, plot_height: int, bias: int):
    """generate the plot for the given sequence"""
    # start position
    x = 0
    y = -1 * bias
    # to know whether it graph has to move up or down
    up_down = 1
    # to find the peak
    peaks = []
    peak = {"y": 0, "count": 0}
    count = 0

    for point in seq:
        if count != 0 and up_down != 1:
            y = y - 1
        if count != 0 and up_down == 1:
            y = y + 1
        for _ in range(point):
            peaks.append((x,y))
            if peak["y"] < y:
                peak["count"] = count
                peak["y"] = y
            if up_down == 1:
                banner[x][y] = '/'
                x = x + 1
                y = y + 1
            else:
                banner[x][y] = '\\'
                x = x + 1
                y = y - 1
            count = count + 1
        up_down = up_down * -1
    min_peak = plot_height
    min_row = 0
    for i in range(len(peaks)-2):
        if peaks[i][1] == peaks[i+1][1] and peaks[i+2][1] < peaks[i+1][1]:
            if(peaks[i][1] < min_peak):
                min_peak = peaks[i][1]
                min_row = peaks[i][0]
    peak["y"] = min_peak
    peak["count"] = min_row
    rising = False
    # if peak["count"] == sum(seq)-1:
    #     rising = True
    display(banner, peak, plot_height,rising)


def run():
    """run script"""
    while True:
        print("""
    1. Run program for the test sequence.
    2. Run program for the custom sequence.
    3. Exit
    """)
        inp = int(input("Kindly select your choice > "))

        if inp == 1:
            # plot seq1
            seq1_banner, seq1_plot_height, bias = make_banner(seq1)
            generate_plot(seq1_banner, seq1, seq1_plot_height, bias)

            print("\n")

            # plot seq2
            seq2_banner, seq2_plot_height, bias = make_banner(seq2)
            generate_plot(seq2_banner, seq2, seq2_plot_height, bias)

        elif inp == 2:
            # plot seq
            # Get the input sequence from the user
            seq = list(map(int, str(input()).split(' ')))
            if 0 in seq:
                raise Exception("0 is not a valid number!!!. Kindly give positive numbers as sequence.")
            check_negative = [1 if i<0 else 0 for i in seq]
            if 1 in check_negative:
                raise Exception("Negative numbers do not make sense here!!!. Kindly give positive numbers as sequence.")
            seq_banner, seq_plot_height,bias = make_banner(seq)
            generate_plot(seq_banner, seq, seq_plot_height,bias)

        elif inp == 3:
            print("Thank you")
            break

        else:
            print("Invalid Input")


if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        print(e)
