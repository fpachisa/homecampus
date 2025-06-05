'''
Created on 30-Aug-2016

@author: Riyaz Ali
'''

'''
Name-Mapping Structure
----------------------
<Grade> = {                    0            1                2            3
        "sub-topic-url": [ <Filename>, <PracticeURL>, <WorksheetURL>, <VideoID>,
                               4            5           6
                           <Heading>, <Group ID>, <Self Index>]
    }

Object-format Mapping
---------------------
obj = {
    "url": [< 1 >, < 2 >],
    "videoID": < 3 >
    "heading": < 4 >,
    "LinkMap": < LinkMap corrs. to the Grade >,
    "GroupID": < 5 >,
    "selfAtPosition": < 6>
}

Link-Map Structure
------------------
LinkMap_<grade> = {
    "GroupID": ( "Group Title",
            [    -> List Containing Topic Name - URL mapped as Tuples
             (Topic Name, URL),
            ]
        ),
    .
    .
    .
}


'''

# LearnMappings for PRIMARY - 3
#------------------------------
Primary3 = {
        
        # Chapter - 1 WHOLE NUMBER
        "Multiplication-Tables-of-6-7-8-9": [
                "/WholeNumbers/Multiplication_Tables_Of_6_7_8_9.html", "", "", "",
                "Tips to Remember Multipication Tables", "P3WN", 1
            ],
        "Number-Notations-Place-Values-Up-to-10000": [
                "/WholeNumbers/Whole_Numbers_Upto_10000.html", "/Whole_Numbers_Number_Notation_Place_Values", "/Whole_Numbers_Number_Notation_Place_Values", "",
                "Number Notation and Place Values Up To 10000", "P3WN", 2
            ],
        "Writing-Numbers-from-Figures-to-Words-Up-to-10000": [
                "/WholeNumbers/Figures_To_Words_Upto_10000.html", "/Whole_Numbers_Figures_to_Words", "/Whole_Numbers_Figures_to_Words", "",
                "Writing Numbers from Figures to Words (Up To 10000)", "P3WN", 3
            ],
        "Writing-Numbers-from-Words-to-Figures-Up-to-10000": [
                "/WholeNumbers/Words_To_Figures_Upto_10000.html", "/Whole_Numbers_Words_to_Figures", "/Whole_Numbers_Words_to_Figures", "",
                "Writing Numbers from Words to Figures (Up To 10000)", "P3WN", 4
            ],
        "Number-Patterns": [
                "/WholeNumbers/Number_Patterns.html", "/Whole_Numbers_Patterns", "/Whole_Numbers_Patterns", "",
                "Number Patterns", "P3WN", 5
            ],
        "Comparing-Ordering": [
                "/WholeNumbers/Comparing_Ordering.html", "/Whole_Numbers_Comparing_Ordering", "/Whole_Numbers_Comparing_Ordering", "",
                "Comparing and Ordering Numbers", "P3WN", 6
            ],
        "Addition": [
                "/WholeNumbers/Addition_Of_Numbers_Within_10000.html", "/Whole_Numbers_Addition", "/Whole_Numbers_Addition", "",
                "Addition of Numbers Within 10000", "P3WN", 7
            ],
        "Subtraction": [
                "/WholeNumbers/Subtraction_Of_Numbers_Within_10000.html", "/Whole_Numbers_Subtraction", "/Whole_Numbers_Subtraction", "",
                "Subtraction of Numbers Within 10000", "P3WN", 8
            ],
        "Whole-Numbers-Multiplication": [
                "/WholeNumbers/Multiplication_Of_Numbers_Within_10000.html", "/Whole_Numbers_Multiplication", "/Whole_Numbers_Multiplication", "",
                "Multiplication of Numbers Within 10000", "P3WN", 9
            ],
        "Whole-Numbers-Division": [
                "/WholeNumbers/Division_Of_Numbers_Within_1000.html", "/Whole_Numbers_Division", "/Whole_Numbers_Division", "",
                "Division of Numbers Within 1000", "P3WN", 10
            ],        
        "2-Step-Word-Problems": [
                "/WholeNumbers/Whole_Numbers_Word_Problems.html", "/Whole_Numbers_Word_Problems", "/Whole_Numbers_Word_Problems", "",
                "2-Step Word Problems Involving the Four Operations (&plus;, &minus;, &times; and &divide;)", "P3WN", 11
            ],
        #----- END of CH - 1 -----#

        # Chapter - 2 MONEY
        "Addition-of-Money": [
                "/Money/Addition_Of_Money.html", "/Money_Addition", "/Money_Addition", "",
                "Addition of Money", "P3MO", 1
            ],
        "Subtraction-of-Money": [
                "/Money/Subtraction_Of_Money.html", "/Money_Subtraction", "/Money_Subtraction", "",
                "Subtraction of Money", "P3MO", 2
            ],
        "Money-Word-Problems": [
                "/Money/Money_Word_Problems.html", "/Money_Word_Problems", "/Money_Word_Problems", "",
                "Money Word Problems", "P3MO", 3
            ],

        # Chapter - 3 TIME
        "Telling-Time": [
                "/Time/Telling_Time.html", "/Telling_Time", "/Telling_Time", "",
                "Telling Time", "P3TI", 1
            ],
        "Time-Conversion-Hours-Minutes": [
                "/Time/Hours_and_Minutes.html", "/Time_Conversion_Hours_Minutes", "/Time_Conversion_Hours_Minutes", "",
                "Hours and Minutes", "P3TI", 2
            ],
        "Time-Addition": [
                "/Time/Time_Addition.html", "/Time_Addition", "/Time_Addition", "",
                "Addition of Time", "P3TI", 3
            ],
        "Time-Subtraction": [
                "/Time/Time_Subtraction.html", "/Time_Subtraction", "/Time_Subtraction", "",
                "Subtraction of Time", "P3TI", 4
            ],
        "Time-Finding-Duration-Start-Finish": [
                "/Time/Time_Duration.html", "/Time_Duration", "/Time_Duration", "",
                "Duration, Start and Finish Times", "P3TI", 5
            ],
        "Time-Problem-Sums": [
                "/Time/Time_Word_Problems.html", "/Time_Word_Problems", "/Time_Word_Problems", "",
                "Time Word Problems", "P3TI", 6
            ],

        # Chapter - 4 LENGTH, MASS AND VOLUME
        "Metres-Centimetres": [
                "/LengthMassVolume/Metres_Centimetres.html", "/Metres_Centimetres", "/Metres_Centimetres", "",
                "Metres and Centimetres", "P3LMV", 1
            ],
        "KiloMetres-Metres": [
                "/LengthMassVolume/KiloMetres_Metres.html", "/Kilometres_Metres", "/Kilometres_Metres", "",
                "Kilometres and Metres", "P3LMV", 2
            ],
        "Kilograms-Grams": [
                "/LengthMassVolume/Kilograms_Grams.html", "/Kilograms_Grams", "/Kilograms_Grams", "",
                "Kilograms and Grams", "P3LMV", 3
            ],
        "Litres-Millilitres": [
                "/LengthMassVolume/Litres_Millilitres.html", "/Litres_Millilitres", "/Litres_Millilitres", "",
                "Litres and Millilitres", "P3LMV", 4
            ],
        "Length-Mass-Volume-1-Step-Story-Sums": [
                "/LengthMassVolume/1_Step_Story_Sums.html", "/Length_Mass_Volume_1-Step_Word_Problems", "/Length_Mass_Volume_1-Step_Word_Problems", "",
                "1-Step Word Problems", "P3LMV", 5
            ],
        "Length-Mass-Volume-2-Step-Story-Sums": [
                "/LengthMassVolume/2_Step_Story_Sums.html", "/Length_Mass_Volume_2-Step_Word_Problems", "/Length_Mass_Volume_2-Step_Word_Problems", "",
                "2-Step Word Problems", "P3LMV", 6
            ],

        # Chapter - 5 FRACTIONS
        "Equivalent-Fractions": [
                "/Fractions/Equivalent_Fractions.html", "/Equivalent-Fraction", "/Equivalent-Fraction", "",
                "Equivalent Fractions", "P3FR", 2
            ],
        "Simplifying-Fractions": [
                "/Fractions/Simplifying_Fractions.html", "/Simplifying-Fractions", "/Simplifying-Fractions", "",
                "How to Simplify Fractions?", "P3FR", 3
            ],
        "Comparing-and-Ordering-Fractions": [
                "/Fractions/Comparing_Ordering_Fractions.html", "/Comparing-and-Ordering-Fractions", "/Comparing-and-Ordering-Fractions", "",
                "Comparing and Ordering Fractions", "P3FR", 4
            ],
        "Adding-Fractions": [
                "/Fractions/Addition_Fractions.html", "/Adding-Fractions", "/Adding-Fractions", "",
                "How to Add Fractions?", "P3FR", 5
            ],
        "Subtracting-Fractions": [
                "/Fractions/Subtracting_Fractions.html", "/Subtracting-Fractions", "/Subtracting-Fractions", "",
                "How to Subtract Fractions?", "P3FR", 6
            ],

        # Chapter - 6 AREA AND PERIMETER
        "Area-in-Square-Units": [
                "/AreaPerimeter/Area_Square_Units.html", "/Area_in_Square_Units", "/Area_in_Square_Units", "",
                "Area in Square Units", "P3AP", 1
            ],
        "Area-in-Square-Centimetres-Square-Metres": [
                "/AreaPerimeter/Area_Square_CM_Square_M.html", "/Area_in_Square_cm_Square_m", "/Area_in_Square_cm_Square_m", "",
                "Area in Square cm and Square m", "P3AP", 2
            ],
        "Area-of-Squares-and-Rectangles": [
                "/AreaPerimeter/Area_Square_Rectangle.html", "/Area_of_Squares_Rectangles", "/Area_of_Squares_Rectangles", "",
                "Area of Squares and Rectangles", "P3AP", 3
            ],
        "Perimeter-of-Squares-and-Rectangles": [
                "/AreaPerimeter/Perimeter_Square_Rectangle.html", "/Perimeter_of_Squares_Rectangles", "/Perimeter_of_Squares_Rectangles", "",
                "Perimeter of Squares and Rectangles", "P3AP", 4
            ],
        "Area-Perimeter-Problem-Sums": [
                "/AreaPerimeter/Area_Perimeter_Word_Problems.html", "/Area_Perimeter_Word_Problems", "/Area_Perimeter_Word_Problems", "",
                "Area and Perimeter Word Problems", "P3AP", 5
            ],

        # Chapter - 7 ANGLES
        "Identifying-Angles-in-Figures": [
                "/Angles/Identifying_Angles.html", "/Identifying_Angles_in_Figures", "/Identifying_Angles_in_Figures", "",
                "Identifying Angles in a Figure", "P3AN", 1
            ],
        "Right-Angles": [
                "/Angles/Right_Angles.html", "/Right_Angles", "/Right_Angles", "",
                "Right Angles", "P3AN", 2
            ],

        # Chapter - 8 BAR GRAPHS
        "Bar-Graphs": [
                "/BarGraphs/Bar_Graphs.html", "/Bar_Graphs", "/Bar_Graphs", "",
                "Reading and Interpreting Bar Graphs", "P3BG", 1
            ],

        # Chapter - 9 PERPENDICULAR & PARALLEL LINES
        "Identifying-Perpendicular-Parallel-Lines": [
                "/PerpendicularParallel/Perpendicular_Parallel.html", "/Identifying_Perpendicular_Parallel_Lines", "/Identifying_Perpendicular_Parallel_Lines", "",
                "Perpendicular and Parallel Lines", "P3PP", 1
            ],
        
        
    }


# End of LearnMappings for PRIMARY - 3
#------------------------------

# Link Mapping for Sidebar PRIMARY - 3
#---------------------------------
LinkMap_P3 = [
        ( "P3WN", "Whole Numbers",
          [
           ("Multiplication Table of 6, 7, 8, 9", "/Learn/Primary-Grade-3/Whole-Numbers/Multiplication-Tables-of-6-7-8-9"),
           ("Numbers up to 10 000", "/Learn/Primary-Grade-3/Whole-Numbers/Number-Notations-Place-Values-Up-to-10000"), ("Figures to Words up to 10 000", "/Learn/Primary-Grade-3/Whole-Numbers/Writing-Numbers-from-Figures-to-Words-Up-to-10000"),
           ("Words to Figures up to 10 000", "/Learn/Primary-Grade-3/Whole-Numbers/Writing-Numbers-from-Words-to-Figures-Up-to-10000"), ("Number Patterns", "/Learn/Primary-Grade-3/Whole-Numbers/Writing-Numbers-from-Words-to-Figures-Up-to-10000"),
           ("Comparing and Ordering", "/Learn/Primary-Grade-3/Whole-Numbers/Comparing-Ordering"), ("Addition", "/Learn/Primary-Grade-3/Whole-Numbers/Addition"),
           ("Subtraction", "/Learn/Primary-Grade-3/Whole-Numbers/Subtraction"), ("Multiplication", "/Learn/Primary-Grade-3/Whole-Numbers-Multiplication"),
           ("Division", "/Learn/Primary-Grade-3/Whole-Numbers-Division"), ("2 - Step Word Problems", "/Learn/Primary-Grade-3/Whole-Numbers/2-Step-Word-Problems")
          ]
        ),
        ( "P3MO", "Money",
          [
           ("Addition", "/Learn/Primary-Grade-3/Addition-of-Money"), ("Subtraction", "/Learn/Primary-Grade-3/Subtraction-of-Money"),
           ("Word Problems", "/Learn/Primary-Grade-3/Money-Word-Problems")
          ]
        ),
        ( "P3TI", "Time",
          [
           ("Telling Time", "/Learn/Primary-Grade-3/Telling-Time"), ("Hours and Minutes", "/Learn/Primary-Grade-3/Time-Conversion-Hours-Minutes"),
           ("Addition", "/Learn/Primary-Grade-3/Time-Subtraction"), ("Subtraction", "/Learn/Primary-Grade-3/Time-Subtraction"),
           ("Duration, Start and Finish Times", "/Learn/Primary-Grade-3/Time-Subtraction"), ("Word Problems", "/Learn/Primary-Grade-3/Time-Subtraction")
          ]
         ),
        ( "P3LMV", "Length, Mass and Volume",
          [
           ("Metres and Centimetres", "/Learn/Primary-Grade-3/Metres-Centimetres"),
           ("Kilometres and Metres", "/Learn/Primary-Grade-3/KiloMetres-Metres"),
           ("Kilograms and Grams", "/Learn/Primary-Grade-3/Kilograms-Grams"),
           ("Litres and Millilitres", "/Learn/Primary-Grade-3/Litres-Millilitres"),
           ("1-Step Word Problems", "/Learn/Primary-Grade-3/Length-Mass-Volume-1-Step-Story-Sums"),
           ("2-Step Word Problems", "/Learn/Primary-Grade-3/Length-Mass-Volume-2-Step-Story-Sums")
          ]
        ),
        ( "P3FR", "Fractions",
          [
           ("Equivalent Fractions", "/Learn/Primary-Grade-3/Equivalent-Fractions"),
           ("Simplifying Fractions", "/Learn/Primary-Grade-3/Simplifying-Fractions"),
           ("Comparing and Ordering", "/Learn/Primary-Grade-3/Comparing-and-Ordering-Fractions"),
           ("Addition", "/Learn/Primary-Grade-3/Adding-Fractions"),
           ("Subtraction", "/Learn/Primary-Grade-3/Subtracting-Fractions")
          ]
        ),
        ( "P3AP", "Area and Perimeter",
          [
           ("Square Units", "/Learn/Primary-Grade-3/Area-in-Square-Units"),
           ("Square cm and Square m", "/Learn/Primary-Grade-3/Area-in-Square-Centimetres-Square-Metres"),
           ("Area of Squares and Rectangles", "/Learn/Primary-Grade-3/Area-of-Squares-and-Rectangles"),
           ("Perimeter of Squares and Rectangles", "/Learn/Primary-Grade-3/Perimeter-of-Squares-and-Rectangles"),
           ("Word Problems", "/Learn/Primary-Grade-3/Area-Perimeter-Problem-Sums")
          ]
        ),
        ( "P3AN", "Angles",
          [
           ("Identifying Angle", "/Learn/Primary-Grade-3/Identifying-Angles-in-Figures"),
           ("Right Angles", "/Learn/Primary-Grade-3/Right-Angles")
          ]
        ),
        ( "P3BG", "Bar Graphs",
          [
           ("Reading and Interpreting Bar Graphs", "/Learn/Primary-Grade-3/Bar-Graphs")
          ]
        ),
        ( "P3PP", "Perpendicular & Parallel Lines",
          [
           ("Indentifying Perpendicular Lines", "/Learn/Primary-Grade-3/Identifying-Perpendicular-Parallel-Lines")
          ]
        )
    ]
# End of Link Mapping for Sidebar PRIMARY - 3
#---------------------------------


class Grade3Mapper:
    @classmethod
    def getMapping(cls, subTopic, topic=""):
        #param topic is reserved for future use
        # 1) Get the data
        try:
            data = Primary3[subTopic]
        except KeyError:
            raise
        
        # 2) Parse into an object @see Line 15 for structure
        obj = {
            'url': [data[1], data[2]],
            'videoID': data[3],
            'heading': data[4],
            'LinkMap': LinkMap_P3,
            'GroupID': data[5],
            'selfAtPosition': data[6]
        }        
        return data[0], obj #data[0] is filename

