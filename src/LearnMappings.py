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
        
    
    